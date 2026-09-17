---
track: concepts
lesson: 1
title: 1강 - 프로젝트 구조와 Activity 생명주기
status: done
---

# 1강 - 프로젝트 구조와 Activity 생명주기


- **Activity** = 웹의 페이지(라우트) 개념. 화면 단위.
- **생명주기**: `onCreate` → `onStart` → `onResume` → `onPause` → `onDestroy`. React의 `useEffect` 마운트/언마운트보다 훨씬 세분화됨.
- `onCreate(savedInstanceState: Bundle?)`: 화면이 처음 만들어질 때 한 번 호출. `savedInstanceState`는 화면 회전 등으로 재생성될 때 이전 상태 복원용.

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Greeting("Android")
        }
    }
}
```

`setContent { }` = React의 `ReactDOM.render(<App />)`와 역할 비슷. 이 안에 실제 화면 UI를 선언.

---
