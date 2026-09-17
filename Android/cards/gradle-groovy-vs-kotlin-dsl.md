---
type: card
title: Gradle Groovy DSL ↔ Kotlin DSL 대응
tags: [android]
---

# Gradle Groovy DSL ↔ Kotlin DSL 대응

오래된 프로젝트는 `build.gradle`(Groovy), 새 프로젝트는 `build.gradle.kts`(Kotlin DSL)를 쓰고, 두 문법이 섞인 저장소도 흔하다. Groovy 는 동적이라 괄호와 `=` 를 생략하고(`minifyEnabled true`, `dev { }`), Kotlin DSL 은 정적 타입이라 실제 API 가 드러난다(`isMinifyEnabled = true`, `create("dev") { }`, `flavorDimensions += "env"`).
