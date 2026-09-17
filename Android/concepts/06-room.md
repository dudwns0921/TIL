---
track: concepts
lesson: 6
title: 6강 - 데이터: 로컬 저장(Room)
status: done
---

# 6강 - 데이터: 로컬 저장(Room)


## 개념

Room = SQLite 위에 얹은 ORM. Prisma/TypeORM에 대응.

| 웹 (Prisma/TypeORM) | 안드로이드 (Room) |
|---|---|
| `schema.prisma`의 `model` | `@Entity` 붙은 data class |
| Prisma Client 쿼리 메서드 | `@Dao` 인터페이스 |
| `PrismaClient` 인스턴스 | `@Database` 추상 클래스 |
| IndexedDB | SQLite (Room이 타입 안전 레이어를 얹음) |

Retrofit과 동일한 패턴: 인터페이스/어노테이션만 선언하면 라이브러리가 실제 구현체를 생성. 차이는 Retrofit은 런타임에 프록시 생성, Room은 **KSP로 빌드 타임에 코드 생성**.

## 실습: 네트워크 + 로컬 캐시 조합 (오프라인 우선)

**1. 의존성 추가**

루트 `build.gradle.kts` (plugins 선언만, apply 안 함):
```kotlin
plugins {
    id("com.google.devtools.ksp") version "2.0.21-1.0.28" apply false
}
```

`app/build.gradle.kts`:
```kotlin
plugins {
    id("com.google.devtools.ksp") version "2.0.21-1.0.28"
}

dependencies {
    implementation("androidx.room:room-runtime:2.6.1")
    implementation("androidx.room:room-ktx:2.6.1")
    ksp("androidx.room:room-compiler:2.6.1")
}
```
KSP(Kotlin Symbol Processing) = 어노테이션 읽어서 코드 생성하는 컴파일러 플러그인.

**2. Entity 정의** (`TodoEntity.kt`)
```kotlin
@Entity(tableName = "todos")
data class TodoEntity(
    @PrimaryKey val id: Int,
    val userId: Int,
    val title: String,
    val completed: Boolean
)
```
API 응답용 `Todo`(DTO)와 DB 저장용 `TodoEntity`를 분리하는 이유: 관심사 분리. 서버 스키마와 로컬 DB 스키마가 독립적으로 진화할 수 있게(예: `cachedAt` 같은 로컬 전용 필드 추가 가능).

**3. DAO** (`TodoDao.kt`)
```kotlin
@Dao
interface TodoDao {
    @Query("SELECT * FROM todos")
    fun observeTodos(): Flow<List<TodoEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertAll(todos: List<TodoEntity>)
}
```
- `Flow<List<TodoEntity>>` 반환 (suspend 아님): 테이블 변경을 자동 감지해 새 값을 emit하는 "살아있는 쿼리". 한 번 조회하고 끝나는 게 아니라 계속 구독.
- `@Insert(onConflict = OnConflictStrategy.REPLACE)`: 있으면 덮어쓰기.
- SQL 문법은 컴파일 타임에 검증됨 (오타 내면 빌드 실패).

**4. Database 클래스** (`AppDatabase.kt`)
```kotlin
@Database(entities = [TodoEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun todoDao(): TodoDao
}
```

**5. 싱글톤으로 생성** (`MyApplication.kt`)
```kotlin
class MyApplication : Application() {
    val database: AppDatabase by lazy {
        Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "app-database"
        ).build()
    }
}
```
`AndroidManifest.xml`의 `<application android:name=".MyApplication" ...>`로 등록 필요.

DB 인스턴스를 싱글톤으로 만드는 이유(Retrofit과 다른 점): 인스턴스가 여러 개 생기면 같은 DB 파일에 대한 락 충돌로 크래시 가능.

`Context`/`Application` 개념: 안드로이드 시스템 안에서 리소스·파일시스템 등에 접근하는 핸들. Node.js `process` 객체에 비유 가능. `Application`은 앱 전체 생명주기 동안 살아있는 최상위 Context.

**6. Repository 패턴** (`TodoRepository.kt`)
```kotlin
class TodoRepository(
    private val api: ApiService,
    private val dao: TodoDao
) {
    val todos: Flow<List<TodoEntity>> = dao.observeTodos()

    suspend fun refresh() {
        val networkTodos = api.getTodos()
        val entities = networkTodos.map { todo ->
            TodoEntity(
                id = todo.id,
                userId = todo.userId,
                title = todo.title,
                completed = todo.completed
            )
        }
        dao.insertAll(entities)
    }
}
```
ViewModel이 "데이터가 어디서 오는지" 몰라도 되게 캡슐화. React Query의 `queryFn` 안에서 fetch+캐시 로직을 감싸는 것과 유사한 역할.

**오프라인 우선 전략**:
1. 화면 진입 시 Room의 Flow를 구독 → 캐시 있으면 즉시 표시
2. 동시에 네트워크 호출 → 성공하면 Room에 insert
3. insert되는 순간 Flow가 자동으로 새 값 emit → 화면 자동 갱신
4. **DB 자체가 single source of truth**, 네트워크 요청은 그걸 갱신하는 부수효과일 뿐

**7. ViewModel** (`TodoViewModel.kt`)
```kotlin
class TodoViewModel(private val repository: TodoRepository) : ViewModel() {
    private val _uiState = MutableStateFlow<TodoUiState>(TodoUiState.Loading)
    val uiState: StateFlow<TodoUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            repository.todos.collect { entities ->
                _uiState.value = TodoUiState.Success(entities.map { it.toTodo() })
            }
        }

        viewModelScope.launch {
            try {
                repository.refresh()
            } catch (e: Exception) {
                // 이미 캐시로 Success 상태면 에러로 덮어쓰지 않음 (버그로 실제로 겪은 부분)
                if (_uiState.value !is TodoUiState.Success) {
                    _uiState.value = TodoUiState.Error(e.message ?: "알 수 없는 오류")
                }
            }
        }
    }
}

private fun TodoEntity.toTodo() = Todo(
    userId = userId, id = id, title = title, completed = completed
)
```

**실전에서 잡은 버그**: Flow 구독(캐시 표시)과 refresh(네트워크)가 별도 코루틴으로 동시에 도는데, refresh 실패 시 무조건 `Error`로 덮어쓰면 캐시가 잘 떠 있던 화면이 이유 없이 에러 화면으로 바뀌어버림. `_uiState.value !is TodoUiState.Success`로 가드 처리 → 캐시 있으면 에러 무시, 캐시 없을 때(Loading)만 진짜 에러 표시.

한계: 캐시 있으면 네트워크 실패를 사용자가 아예 모름. 실무에서는 `Success(data, isRefreshing, errorMessage)`처럼 상태를 확장해서 데이터는 보여주되 에러 배너/토스트를 별도로 띄우는 방식을 더 많이 씀 (추후 개선 여지로 남김).

## 핵심 API 정리

- `@Entity` / `@Dao` / `@Database`: Room의 3대 어노테이션, Retrofit과 동일한 "선언 → 라이브러리가 구현" 패턴
- `Flow` 반환 쿼리: DB 변경을 자동 반영하는 리액티브 쿼리
- Repository 패턴: 네트워크 + 로컬 DB를 하나의 데이터 소스처럼 추상화
- DTO(API 모델)와 Entity(DB 모델) 분리, 그 사이 변환 함수(`toTodo()`, `toEntity()`류)가 계층 경계

---
