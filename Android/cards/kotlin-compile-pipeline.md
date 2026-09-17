---
type: card
title: Kotlin 컴파일 파이프라인
tags: [kotlin]
---

# Kotlin 컴파일 파이프라인


```
.kt 소스 파일
  → Kotlin 컴파일러 (kotlinc / K2, 문법·타입 검사)
    → JVM 바이트코드 (.class 파일, Java와 동일 형식)
      → D8 / R8 (DEX 변환 + 코드 축소·난독화)
        → DEX 바이트코드 (classes.dex, 안드로이드 전용 형식)
          → APK/AAB 패키징 → 기기의 ART(Android Runtime)가 실행
```

웹과 비교:

| 웹 (TypeScript) | 안드로이드 (Kotlin) |
|---|---|
| `.ts` 파일 | `.kt` 파일 |
| `tsc` | `kotlinc` |
| `.js` (브라우저용) | `.class` (JVM용) |
| webpack/esbuild 번들링 | D8/R8이 번들링+압축 겸함 |
| 브라우저 JS 엔진(V8) 실행 | 기기의 ART가 실행 |

- **왜 두 번 변환하나(.class → DEX)**: `.class`는 서버/데스크톱용 범용 JVM 바이트코드. 모바일은 메모리·배터리 제약이 있어 구글이 더 압축된 전용 형식(DEX)을 따로 설계 → 한 단계 더 필요.
- **R8** = ProGuard 후속작. 안 쓰는 코드 제거 + 이름 난독화로 APK 용량 절감. Vite/Rollup의 프로덕션 minify와 목적 동일.
- **K2**: 최신 Kotlin 컴파일러 프론트엔드(2024년경부터 기본값). 문법 검사·타입 추론을 더 빠르고 정확하게 개선한 리라이트 버전.
- Gradle이 전체 파이프라인을 태스크 그래프로 오케스트레이션.
