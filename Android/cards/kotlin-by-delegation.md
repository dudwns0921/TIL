---
type: card
title: by 위임 프로퍼티와 by viewModels()
tags: [kotlin]
---

# `by` 위임 프로퍼티와 `by viewModels()`


`val x by delegate`는 x의 get/set을 delegate 객체에 맡긴다. `by lazy { }`가 가장 흔한 예. View 시스템에서 Activity 안의 ViewModel은 `private val vm: MyViewModel by viewModels()`로 얻고, 처음 접근할 때 생성되며 회전 후에도 같은 인스턴스가 돌아온다. Compose의 `viewModel()`과 같은 역할.
