---
type: card
title: 화면 이동: Intent(XML View) vs Navigation Compose
tags: [android]
---

# 화면 이동: Intent(XML View) vs Navigation Compose


| | XML View | Compose |
|---|---|---|
| 화면 단위 | Activity 하나 = 화면 하나 | Activity 하나, 화면은 Composable |
| 이동 | `Intent` + `startActivity` | `navController.navigate(...)` |
| 데이터 | `putExtra` / `getStringExtra` | route 인자 또는 `@Serializable` 객체 |
| 뒤로가기 | 시스템 Activity 스택 | `NavController` 백스택, `popBackStack()` |
| 화면 등록 | 매니페스트 | `NavHost { composable(...) }` |

Compose는 Single Activity 구조라 앱 안 이동은 라우터(Navigation Compose)로 한다. `NavHost` = `<Routes>`, `composable("detail/{name}")` = `<Route path>`, `navigate` = `navigate()`, `popBackStack` = `history.back()`.

```kotlin
@Serializable data class Detail(val name: String)   // Navigation 2.8+ 타입 안전 route

NavHost(navController, startDestination = Main) {
    composable<Main> { MainScreen(onDetail = { navController.navigate(Detail(it)) }) }
    composable<Detail> { entry -> DetailScreen(entry.toRoute<Detail>().name) }
}
```

Intent는 **앱 경계를 넘을 때**만: 다른 앱(전화, 브라우저, 공유), 시스템 설정 화면, 외부 딥링크 수신, 레거시 Activity와 Compose Activity 사이 이동. "Intent = OS에게 부탁, NavController = 내 앱 안 화면 교체". Navigation 3(2025~)는 백스택을 리스트로 직접 다루는 새 방식이나 아직 2.x가 주류.
