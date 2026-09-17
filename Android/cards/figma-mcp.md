---
type: card
title: Figma → 코드 (MCP 연동, 참고)
tags: [android]
---

# Figma → 코드 (MCP 연동, 참고)


공식 Figma MCP 서버가 있어 Figma 파일에 직접 접근 가능. 주요 도구: `get_design_context`(레이아웃/스타일 추출), `get_screenshot`, `get_variable_defs`(디자인 토큰), `create_design_system_rules`.

흐름: Figma에서 프레임 링크 전달 → 디자인 컨텍스트/스크린샷 추출 → Compose 코드로 변환.

- Figma의 Auto Layout ↔ Compose의 `Row`/`Column` + `Modifier` 체이닝 구조가 유사해 변환 품질 괜찮은 편.
- 디자인 토큰(색상/간격/폰트)을 `Color.kt`, `Typography.kt` 초안으로 뽑을 때 특히 유용.
- 한계: Compose 특유의 상태 관리(`remember`, ViewModel 연결)나 접근성 속성은 Figma가 정적 디자인이라 알 수 없어 사람이 다시 손봐야 함.
