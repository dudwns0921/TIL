---
type: card
title: val / var
tags: [kotlin]
---

# val / var


- **`val`**: 재할당 불가능 (TS `const`와 동일).
- **`var`**: 재할당 가능 (TS `let`과 동일).
- **함정**: "재할당 불가능" ≠ "내용이 안 바뀜". `val`이어도 내부 상태가 변경 가능한 타입(예: `MutableList`)이면 내용물은 바뀔 수 있음.
  ```kotlin
  val list = mutableListOf(1, 2, 3)
  list.add(4)  // OK, list 자체를 재할당한 게 아니라 내용만 변경
  // list = mutableListOf(5, 6)  // 에러: 재할당이라 안 됨
  ```
  JS의 `const arr = [1,2,3]; arr.push(4)`와 동일한 원리.
- 실전 예: `private val _todos = MutableStateFlow<List<String>>(emptyList())`에서 `_todos`는 `val`(컨테이너 자체는 안 바뀜)이지만, `_todos.value`(담긴 리스트)는 계속 새 값으로 교체됨.
- **실전 규칙**: 기본은 `val` 우선, 정말 필요할 때만 `var`. 불변성이 버그를 줄인다는 철학은 TS/함수형 프로그래밍과 동일.
