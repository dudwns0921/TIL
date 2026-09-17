---
track: concepts
lesson: 5
title: 5강 - 데이터: 네트워킹(Retrofit)
status: done
---

# 5강 - 데이터: 네트워킹(Retrofit)


## 개념

axios/fetch에 대응. Retrofit은 **인터페이스에 어노테이션만 붙이면** 실제 HTTP 호출 코드를 런타임에 자동 생성해주는 라이브러리.

| 웹 (axios/fetch) | 안드로이드 (Retrofit) |
|---|---|
| `axios.get('/api/todos')` | `interface` + `@GET` + `suspend fun` |
| axios 인스턴스 생성 (baseURL) | `Retrofit.Builder()` |
| JSON → JS 객체 자동 파싱 | Gson/Moshi 컨버터가 JSON → data class 자동 변환 |

## 실습: JSONPlaceholder API로 할 일 목록 가져오기

**1. 의존성 추가** (`app/build.gradle.kts`)
```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.11.0")
    implementation("com.squareup.retrofit2:converter-gson:2.11.0")
}
```

`AndroidManifest.xml`의 `<manifest>` 태그 안(`<application>` 밖)에 인터넷 권한 추가:
```xml
<uses-permission android:name="android.permission.INTERNET" />
```

**2. 데이터 모델** (`Todo.kt`)
```kotlin
data class Todo(
    val userId: Int,
    val id: Int,
    val title: String,
    val completed: Boolean
)
```
TypeScript `interface`와 거의 동일. JSON key와 프로퍼티명이 같으면 Gson이 자동 매핑, 다르면 `@SerializedName("...")` 사용.

**3. API 인터페이스** (`ApiService.kt`)
```kotlin
interface ApiService {
    @GET("todos")
    suspend fun getTodos(): List<Todo>

    @GET("todos/{id}")
    suspend fun getTodo(@Path("id") id: Int): Todo
}
```
`suspend fun`이라 코루틴 스코프 안에서만 호출 가능 (3강 내용 재활용).

**4. Retrofit 싱글톤 인스턴스** (`RetrofitInstance.kt`)
```kotlin
object RetrofitInstance {
    val api: ApiService by lazy {
        Retrofit.Builder()
            .baseUrl("https://jsonplaceholder.typicode.com/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
}
```
- `object` = Kotlin 싱글톤 키워드. `class` 대신 쓰면 앱 전체에서 인스턴스 하나만 존재 (JS `export default { ... }`와 유사).
- `by lazy { }` = 처음 접근하는 시점에 한 번만 계산, 이후 캐시된 값 재사용.
- `.create(ApiService::class.java)` = 인터페이스(구현체 없음)를 넘기면 Retrofit이 런타임에 프록시 객체를 만들어 HTTP 호출 코드를 채워줌.

**5. UI 상태 표현** (`TodoUiState.kt`)
```kotlin
sealed interface TodoUiState {
    object Loading : TodoUiState
    data class Success(val todos: List<Todo>) : TodoUiState
    data class Error(val message: String) : TodoUiState
}
```
TypeScript의 discriminated union과 동일 개념. `when`으로 분기 시 컴파일러가 모든 케이스 처리를 강제.

**6. ViewModel** (`TodoViewModel.kt`)
```kotlin
class TodoViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<TodoUiState>(TodoUiState.Loading)
    val uiState: StateFlow<TodoUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            try {
                val todos = RetrofitInstance.api.getTodos()
                _uiState.value = TodoUiState.Success(todos)
            } catch (e: Exception) {
                _uiState.value = TodoUiState.Error(e.message ?: "알 수 없는 오류")
            }
        }
    }
}
```
`_uiState`(private, 수정 가능) / `uiState`(public, 읽기 전용) 분리는 관례 — React 커스텀 훅이 `setState`는 안 넘기고 `state`만 리턴하는 캡슐화와 동일.

**7. Compose UI** (`TodoScreen.kt`)
```kotlin
@Composable
fun TodoScreen(
    modifier: Modifier = Modifier,
    viewModel: TodoViewModel = viewModel()
) {
    val uiState by viewModel.uiState.collectAsState()

    when (val state = uiState) {
        is TodoUiState.Loading -> {
            Box(modifier = modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        }
        is TodoUiState.Success -> {
            LazyColumn(modifier = modifier.fillMaxSize()) {
                items(state.todos) { todo ->
                    Text(text = todo.title, modifier = Modifier.padding(16.dp))
                }
            }
        }
        is TodoUiState.Error -> {
            Box(modifier = modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                Text(text = "에러: ${state.message}")
            }
        }
    }
}
```
- `when (val state = uiState)` → 스마트 캐스팅: 각 분기 안에서 `state`가 해당 서브타입으로 자동 캐스팅됨 (TS 타입 narrowing과 동일).
- `LazyColumn` = 가상 스크롤 리스트 (`react-window`와 유사, 화면에 보이는 아이템만 렌더링).
- `items(state.todos) { todo -> ... }` = `list.map(item => <Row key .../>)`에 대응. 실무에서는 `items(state.todos, key = { it.id })`로 key 지정 권장 (리컴포지션 최적화).

## 핵심 API 정리

- `interface` + `@GET`/`@Path`: 선언적 API 정의, 실제 구현은 Retrofit이 생성
- `object ... by lazy { }`: 싱글톤 + 지연 초기화
- `sealed interface`: discriminated union, exhaustive `when` 분기 강제

---
