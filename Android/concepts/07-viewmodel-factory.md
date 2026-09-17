---
track: concepts
lesson: 7
title: 7강 - ViewModelFactory (의존성 수동 주입)
status: done
---

# 7강 - ViewModelFactory (의존성 수동 주입)


## 문제 상황

`viewModel()` Composable은 기본적으로 **파라미터 없는 생성자**만 만들 줄 안다. `TodoViewModel(repository: TodoRepository)`처럼 생성자에 의존성이 있으면, "이 ViewModel을 어떻게 만들지" 알려주는 별도 객체(Factory)가 필요.

웹 비유: DI 컨테이너(InversifyJS)나 Context로 서비스 주입하는 패턴과 유사한 문제. 안드로이드는 이를 `ViewModelProvider.Factory` 인터페이스로 표준화.

Hilt 같은 DI 라이브러리 없이 **수동으로** 구현 — 원리를 알아야 나중에 Hilt가 뭘 대신해주는지 감이 옴.

## Step 1. Factory 작성

```kotlin
class TodoViewModelFactory(
    private val repository: TodoRepository
) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        @Suppress("UNCHECKED_CAST")
        return TodoViewModel(repository) as T
    }
}
```

**코드 상세 분석**

- **`: ViewModelProvider.Factory`**: 인터페이스 구현 (TS `implements`와 동일). `create(modelClass)` 하나만 요구하는 계약.
- **`<T : ViewModel>`**: 제네릭 타입 파라미터 + 상한 제약(upper bound). "T는 ViewModel을 상속한 타입이어야 한다". TS `<T extends ViewModel>`과 동일 개념.
- **`modelClass: Class<T>`**: 리플렉션 개념. `Class<T>`는 "타입 T 자체를 값으로 표현한 객체". JS/TS는 컴파일 시 타입 정보가 사라지지만(erasure), JVM은 런타임에도 클래스 정보가 객체로 남아있음 — 그게 `Class<T>`. `TodoViewModel::class.java`로 얻음.
  - 여러 종류의 ViewModel을 하나의 Factory가 다뤄야 할 때 분기 처리 가능:
    ```kotlin
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        return when {
            modelClass.isAssignableFrom(TodoViewModel::class.java) ->
                TodoViewModel(repository) as T
            else -> throw IllegalArgumentException("Unknown ViewModel class")
        }
    }
    ```
- **`@Suppress("UNCHECKED_CAST")` + `as T`**: 사람은 "이 Factory는 항상 TodoViewModel만 만든다"는 걸 알지만 컴파일러는 증명 못 함 → 캐스팅 경고 발생 → 억제. TS의 `as unknown as T` 강제 캐스팅과 심리적으로 동일한 상황("타입 시스템은 모르지만 나는 안전함을 안다").

## Step 2. Application에서 Repository 싱글톤 준비

```kotlin
class MyApplication : Application() {
    val database: AppDatabase by lazy {
        Room.databaseBuilder(applicationContext, AppDatabase::class.java, "app-database").build()
    }

    val repository: TodoRepository by lazy {
        TodoRepository(api = RetrofitInstance.api, dao = database.todoDao())
    }
}
```
`repository`도 `by lazy`로 앱 전체 싱글톤화. Retrofit/Room 배선 과정을 View 계층이 몰라도 되게 하는 게 핵심.

## Step 3. Compose에서 Factory 사용

```kotlin
@Composable
fun TodoScreen(
    modifier: Modifier = Modifier,
    viewModel: TodoViewModel = viewModel(
        factory = run {
            val app = LocalContext.current.applicationContext as MyApplication
            TodoViewModelFactory(app.repository) // MyApplication의 싱글톤 재사용 (직접 새로 만들지 않기)
        }
    )
) { ... }
```

**주의(실제 실습에서 겪은 실수)**: `TodoViewModelFactory(TodoRepository(...))`처럼 Repository를 직접 새로 만들면, `TodoScreen`이 호출될 때마다 새 인스턴스가 생겨서 앱 전체 싱글톤 원칙이 깨짐. 반드시 `app.repository`(이미 조립된 싱글톤)를 재사용.

- `LocalContext.current`: 현재 Composable의 `Context`를 얻는 CompositionLocal.
- `.applicationContext as MyApplication`: Application 인스턴스로 캐스팅.
- `viewModel(factory = ...)`: Compose ViewModel 헬퍼가 factory 파라미터를 받을 수 있음.

## 실무에서는 더 간단한 방법도 있음

```kotlin
val factory = viewModelFactory {
    initializer {
        TodoViewModel(app.repository)
    }
}
```
`viewModelFactory { initializer { } }` DSL이 위의 리플렉션/캐스팅 코드를 대신 감춰줌.

## 전체 아키텍처 요약 (5~7강 종합)

```
TodoScreen (Compose)
  └─ viewModel(factory = TodoViewModelFactory(app.repository))
       └─ TodoViewModel
            ├─ repository.todos (Flow 구독) → 캐시 즉시 표시
            └─ repository.refresh() → 네트워크 성공 시 Room에 insert
                 └─ TodoRepository
                      ├─ ApiService (Retrofit) → 서버
                      └─ TodoDao (Room) → 로컬 SQLite
```

MyApplication이 Retrofit/Room/Repository를 조립해서 싱글톤으로 보관 → Factory가 그걸 꺼내 ViewModel에 주입 → View는 최종 상태(uiState)만 구독.

---
