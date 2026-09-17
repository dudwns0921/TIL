---
type: card
title: SharedFlow vs StateFlow
tags: [android]
---

# SharedFlow vs StateFlow


- `StateFlow`: 초기값 필수, 마지막 값 보관, 같은 값 연속 발행은 무시. **화면 상태**용.
- `SharedFlow`: 초기값 없음, 기본은 보관 안 함(`replay = 0`), 같은 값도 매번 전달. **1회성 이벤트**(화면 전환, 토스트)용.
- 구독자가 없을 때 `emit`한 값은 사라진다. `extraBufferCapacity`는 이미 구독 중인 느린 구독자용 버퍼이고, 늦게 온 구독자에게 주려면 `replay`를 켜야 한다.
- `tryEmit`은 non-suspend, `emit`은 suspend. 일반 함수에서는 `tryEmit`.
