---
type: card
title: 메서드 레퍼런스 (::)
tags: [kotlin]
---

# 메서드 레퍼런스 (`::`)


함수를 콜백으로 넘길 때 람다로 감싸지 않고 바로 참조하는 축약 문법.
```kotlin
onInputChange = viewModel::onInputChange   // 아래와 완전히 동일
onInputChange = { viewModel.onInputChange(it) }

onAddClick = viewModel::addTodo
onAddClick = { viewModel.addTodo() }
```
JS의 `onClick={handleClick}`(화살표 함수로 안 감싸고 함수 자체를 바로 넘기는 것)와 같은 이유로 관례상 선호됨 — 불필요한 람다 래핑 한 겹 제거.
