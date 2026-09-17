---
track: concepts
lesson: 3
title: 3강 - 비동기 처리: Coroutine
status: done
---

# 3강 - 비동기 처리: Coroutine


## 개념

JS의 `async/await`, `Promise`에 대응. 네트워크 호출, DB 접근처럼 시간이 걸리는 작업을 블로킹 없이 처리.

```kotlin
// JS
async function fetchUser() {
    const res = await fetch("/user");
    return res.json();
}

// Kotlin
suspend fun fetchUser(): User {
    val res = api.getUser()
    return res
}
```

`suspend` 키워드 = `async` 함수 표시. "중간에 멈췄다가(스레드 양보) 나중에 재개될 수 있는 함수"라는 뜻.

**JS와의 차이**: JS는 싱글 스레드라 `await`이 이벤트 루프 콜백 등록 방식인데, 코틀린 Coroutine은 실제로 스레드를 오갈 수 있음. 네트워크 호출은 백그라운드 스레드, UI 반영은 메인 스레드로 — 이 전환을 코드 한 줄로 처리.

## CoroutineScope

Coroutine은 항상 "스코프" 안에서 실행되어야 함. ViewModel엔 `viewModelScope`가 기본 제공되고, ViewModel이 `onCleared()`될 때(화면 완전히 사라질 때) 그 안의 코루틴도 자동 취소됨. React `useEffect`의 cleanup(`abortController.abort()`)과 목적 동일 — 화면 나간 뒤 늦게 온 응답으로 없는 화면을 업데이트하는 버그 방지.

Composable 안에서 직접 코루틴을 써야 할 땐(ViewModel 없이) `rememberCoroutineScope()`로 스코프를 얻어서 `scope.launch { }`로 실행. 이 스코프는 해당 Composable이 컴포지션에서 빠지면 함께 취소됨.

## 실습: 1초 후 자동 증가

```kotlin
class CounterViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow<Int> = _count

    fun increment() {
        _count.value++
    }

    fun incrementAfterDelay() {
        viewModelScope.launch {
            delay(1000) // 1초 대기, 스레드 안 막음
            _count.value++
        }
    }
}
```

## 핵심 API

- `launch { }`: 결과값을 기다리지 않고 새 코루틴을 실행하는 빌더. JS의 `void async function(){...}()`와 유사.
- `delay(ms)` vs `Thread.sleep(ms)`: `sleep`은 스레드를 통째로 멈춰서 UI 스레드에서 쓰면 앱이 멈춤(ANR 위험). `delay`는 스레드를 양보만 해서 그 시간 동안 다른 작업(버튼 클릭 등)이 정상 처리됨.
- `viewModelScope`: ViewModel 생명주기에 묶인 스코프. 화면이 사라지면 진행 중이던 코루틴도 자동 취소.
- `rememberCoroutineScope()`: ViewModel 없이 Composable 안에서 코루틴을 실행해야 할 때 사용.

---
