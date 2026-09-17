---
track: concepts
lesson: 4
title: 4강 - 아키텍처: MVVM
status: done
---

# 4강 - 아키텍처: MVVM


## 개념

역할 분리 구조. 세 조각으로 나뉨.

- **Model**: 데이터 계층 (API 응답, DB 엔티티). 순수 데이터 + 데이터를 가져오는 로직.
- **View**: Composable 함수들. 상태를 받아서 그리기만 함, 로직은 없음.
- **ViewModel**: 화면의 상태(state)와 비즈니스 로직을 들고 있는 계층. View가 이벤트(버튼 클릭 등)를 보내면 ViewModel이 상태를 바꾸고, View는 바뀐 상태를 관찰해서 다시 그림.

웹 개발 매핑: View는 React 자체(컴포넌트가 상태 받아서 렌더링), ViewModel은 React 자체엔 없는 개념 — React의 커스텀 훅 + 상태 관리 라이브러리(Zustand/Redux/Context)가 그 역할을 대신함.

가장 중요한 차이: **ViewModel은 화면 회전 같은 Activity 재생성 상황에서도 살아남는다**. 일반 Compose 상태(`remember`)는 화면 회전하면 날아가지만, ViewModel 안의 상태는 유지됨.

데이터 흐름은 단방향(Unidirectional): View → 이벤트 → ViewModel → 상태 갱신 → View 리컴포지션. Flux/Redux 패턴이랑 사실상 동일한 철학.

## 실습: remember 상태 → ViewModel로 이전

```kotlin
class CounterViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow<Int> = _count

    fun increment() {
        _count.value++
    }
}

@Composable
fun CounterDemo(
    modifier: Modifier = Modifier,
    viewModel: CounterViewModel = viewModel()
) {
    val count by viewModel.count.collectAsState() // val 필수: State는 읽기 전용

    Column(
        modifier = modifier.fillMaxSize().padding(24.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Count: $count")
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = { viewModel.increment() }) {
            Text("증가")
        }
    }
}
```

결과: 회전해도 count 유지됨 확인. `remember`는 화면(Composable)에 상태가 묶여있고, ViewModel은 Activity 재생성과 무관하게 살아남는 별도 객체라서 생기는 차이.

## State Hoisting (상태 끌어올리기)

자식 Composable이 상태를 직접 소유하지 않고, 부모가 상태를 들고 있다가 값 + 콜백을 내려주는 패턴.

```kotlin
// 자식: 상태를 직접 소유하지 않음, props처럼 값과 콜백만 받음
@Composable
fun TodoInputRow(
    input: String,
    onInputChange: (String) -> Unit,
    onAddClick: () -> Unit
) { ... }
```

React 비유:
```jsx
// 나쁜 예: 자식이 상태를 직접 소유
function InputRow() {
  const [input, setInput] = useState('');
}

// 좋은 예: 부모가 상태 소유, 자식은 props로만 받음
function InputRow({ input, onInputChange, onAddClick }) { ... }
```

이 패턴의 장점: 나중에 상태 소유자를 `remember`에서 `ViewModel`로 바꿔도, 자식 Composable 코드는 한 줄도 안 바뀜. 값 받고 콜백 호출만 하니까 상태가 어디 있든 몰라도 됨 — 리팩토링 비용이 크게 줄어듦.

## 핵심 API 정리

- `MutableStateFlow` = 관찰 가능한 상태 컨테이너, RxJS의 `BehaviorSubject`나 Zustand 스토어랑 유사.
- `collectAsState()` = View 쪽에서 StateFlow를 구독해서 Compose 상태로 변환 (`useSyncExternalStore`나 Zustand의 `useStore`와 비슷한 역할).
- View는 상태를 직접 못 바꾸고 ViewModel의 함수(`increment()` 등)를 호출해서만 바꿈 — 단방향 흐름이 코드 레벨에서 강제됨.
- ViewModel 안에 비즈니스 로직을 몰아두면 UI 코드는 순수 렌더링만 담당 → 테스트하기 쉬움 (View 없이 ViewModel 단독 유닛 테스트 가능).

---
