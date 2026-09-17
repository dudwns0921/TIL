---
type: card
title: Box vs Row / Column
tags: [android]
---

# Box vs Row / Column


`Box`는 CSS `<div>`보다 정확히는 `position: relative` 컨테이너 + 자식 `position: absolute` 조합에 가까움.

- 평범한 `<div>`: 자식이 세로로 쌓이는 블록 레이아웃(`display: block`)
- `Box`: 자식들이 기본적으로 **겹쳐서(layered)** 배치. `contentAlignment`로 겹친 상태의 정렬 지정, 개별 자식은 `Modifier.align(...)`으로 위치 지정 가능.
- "그냥 감싸는 컨테이너"가 필요하면 `Column`(세로, `flex-direction: column`) / `Row`(가로, `flex-direction: row`)를 훨씬 자주 씀.
- `Box`는 "화면 중앙에 뭔가 하나만 놓기"처럼 자식이 하나뿐이라 겹칠 게 없는 경우에 적합.
