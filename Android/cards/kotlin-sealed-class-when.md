---
type: card
title: sealed class + when
tags: [kotlin]
---

# `sealed class` + `when`


하위 타입을 같은 파일 안으로 제한한 클래스. `when`에서 모든 하위 타입을 다루지 않으면 컴파일 에러라 TS의 discriminated union + exhaustive `never` 체크를 언어가 강제한다. 이벤트/결과 타입(`Action.Toast`, `Action.NormalAlert`) 정의에 자주 쓴다.
