---
type: card
title: StateFlow에 담긴 리스트 갱신
tags: [android]
---

# StateFlow에 담긴 리스트 갱신


`StateFlow<List<T>>`의 리스트는 불변(immutable)이라 `.add()` 같은 직접 변경이 안 됨. **새 리스트를 만들어 통째로 교체**해야 함:
```kotlin
_todos.value = _todos.value + newTodo
```
Compose의 `mutableStateListOf()`(`SnapshotStateList`, `.add()` 직접 가능)와 다른 점이니 헷갈리지 않도록 주의.
