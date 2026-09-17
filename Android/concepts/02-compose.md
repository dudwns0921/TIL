---
track: concepts
lesson: 2
title: 2강 - UI 시스템: Jetpack Compose
status: done
---

# 2강 - UI 시스템: Jetpack Compose


## 기본 개념

- `@Composable` 어노테이션 붙은 함수 = React 함수형 컴포넌트와 거의 동일. 파라미터 = props.
- `Text(...)` = JSX의 `<p>{...}</p>` 같은 존재.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!")
}
```

## 상태(State)

- `remember` + `mutableStateOf` ↔ React `useState`.

```kotlin
var count by remember { mutableStateOf(0) }
```

- 주의: `remember` 상태는 Activity가 재생성되는 상황(예: 화면 회전)에서 초기화됨. 회전 시 `onDestroy → onCreate`가 다시 돌면서 날아감 → 유지하려면 ViewModel 필요 (4강 참고).
- `collectAsState()`로 받은 값은 `val`로 받아야 함 (읽기 전용 `State<T>`라서 `var` 쓰면 컴파일 에러).

## Modifier

CSS 인라인 스타일이 메서드 체이닝으로 바뀐 것. **체이닝 순서가 결과에 영향을 줌** (`.padding().background()` vs `.background().padding()`은 다른 결과).

자주 쓰는 것: `padding()`, `fillMaxWidth()`/`fillMaxSize()`, `size()`, `background()`, `clickable{}`, `safeDrawingPadding()`(시스템 바 침범 방지).

**기본값 컨벤션**: `modifier` 파라미터의 기본값은 항상 빈 `Modifier`여야 함. `fillMaxSize()` 같은 스타일을 기본값에 박으면 재사용성이 깨짐(호출하는 쪽에서 커스텀 못 함). 대신 함수 본문에서 체이닝.

```kotlin
@Composable
fun MyComposable(modifier: Modifier = Modifier) { // 기본값은 빈 Modifier
    Column(modifier = modifier.fillMaxSize().padding(24.dp)) { ... }
}
```

## Scaffold와 innerPadding

```kotlin
Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
    CounterDemo(modifier = Modifier.padding(innerPadding))
}
```

`Scaffold`는 화면 골격(상단바/하단바 등 슬롯)을 정의하는 컴포저블. `innerPadding`은 그 바들이 차지하는 공간만큼의 여백값 — 콘텐츠에 적용 안 하면 lint 경고("Content padding parameter is not used") 뜨고, 상단바에 컨텐츠가 가려질 수 있음. React Native의 `SafeAreaView`와 목적이 비슷.

## 후행 람다 (Trailing Lambda)

코틀린 문법: 함수의 **마지막 파라미터가 함수 타입(람다)**이면 괄호 밖으로 빼서 `{ }`로 쓸 수 있음 (Compose 전용 문법 아니고 코틀린 일반 규칙).

```kotlin
fun doSomething(name: String, action: () -> Unit) {
    action()
}

doSomething("test", action = { println("실행!") }) // 기본형
doSomething("test") { println("실행!") } // 후행 람다로 축약
```

`Scaffold`도 마지막 파라미터가 `content: @Composable (PaddingValues) -> Unit`이라 `{ innerPadding -> ... }` 형태로 쓸 수 있는 것. `innerPadding`은 직접 지정한 람다 파라미터 이름, `->`는 JS 화살표 함수의 `=>`와 동일 개념.

거의 모든 Composable이 "마지막 파라미터로 content 람다를 받는" 구조라서 Compose 코드가 UI 트리처럼 중첩되어 보임. `Button(onClick = {...}) { Text("증가") }`처럼 람다가 여러 개면, 이름 있는 건 괄호 안에 남고 마지막(content)만 밖으로 빠짐.

## 리컴포지션 vs React 리렌더링 vs Vue 반응성

- **React**: 상태 바뀌면 컴포넌트 함수 전체 재실행 → Virtual DOM diff. 매크로(서브트리) 단위.
- **Compose**: "리컴포지션" — 컴파일러가 `State` 읽는 지점을 추적해서, 그 값을 실제로 읽은 부분만 다시 실행. 마이크로 단위.
- **Vue 3**: `reactive()`/`ref()`가 Proxy로 get/set을 가로채서 런타임에 의존성 추적 → 그 값 읽은 부분만 재렌더링. Compose와 철학 유사.
- 차이는 구현 방식: Vue는 런타임 Proxy 기반, Compose는 컴파일 타임에 컴파일러 플러그인이 추적 코드 삽입 + `Snapshot` 상태 시스템으로 관리.

## 실용 팁

- Import 자동 추가: 빨간 줄에 커서 놓고 `Option + Enter`(맥)/`Alt + Enter`(윈도우). 전체 정리는 `Cmd+Option+O` / `Ctrl+Alt+O`.

---
