---
track: concepts
type: reference
title: 번외 - 개발 환경과 빌드 시스템
---

# 번외 - 개발 환경과 빌드 시스템


## 디바이스 설정

**에뮬레이터**: Android Studio → Device Manager → Create Device → Pixel 모델 선택 → System Image(API 레벨) 다운로드 → 실행.

**실제 기기**: 설정 → 휴대전화 정보 → 빌드 번호 7번 탭(개발자 모드) → 개발자 옵션 → USB 디버깅 켜기 → USB 연결 → 팝업에서 허용. 데이터 전송 지원 케이블 필요.

## Logcat 필터

로그캣 레벨 필터는 "이 레벨 **이상**"이다. `-s TAG:D`는 D·I·W·E 전부.

- 터미널, 특정 태그 D 이상: `adb logcat -s MyApp:D`
- 터미널, 정확히 D만: `adb logcat -s MyApp | grep " D MyApp"`
- Android Studio Logcat 창, 정확히 D만: `tag:MyApp level:DEBUG -level:INFO` (D 이상에서 I 이상을 뺀다). 자주 쓰면 필터 저장.
- 크래시는 앱 태그가 아니라 `AndroidRuntime` 태그에 찍힌다: `adb logcat -s AndroidRuntime`

## 트러블슈팅: `protoc-gen-grpc-java ... program not found or is not executable`

Apple Silicon 맥에서 gRPC 코드 생성(`generateDebugProto`)이 실패하는 경우. 원인은 `protoc-gen-grpc-java`의 `osx-aarch_64` 아티팩트가 이름과 달리 **x86_64 바이너리**라서(1.63~1.75 전부 동일), Rosetta 없는 맥에서는 실행이 안 된다. 진단: `file <exe>`가 `x86_64`, `pgrep oahd`가 비어 있음.

해결은 Rosetta 설치 하나뿐이다. 버전 업으로는 안 된다.

```bash
softwareupdate --install-rosetta --agree-to-license
```

`protoc` 자체는 진짜 arm64라 문제없다. 새 맥에서 처음 빌드할 때 한 번 겪는 문제.

## 의존성 관리 (Gradle vs npm)

| npm | Gradle |
|---|---|
| `package.json` | `app/build.gradle.kts` |
| `npm install` | Gradle Sync (자동/Sync Now) |
| npm 레지스트리 | Maven Central, Google's Maven repo |
| `node_modules` | `~/.gradle` 캐시 |

```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.11.0")
}
```

- **Jetpack (구글 공식, 기본 내장은 아님)**: Compose, ViewModel, Room, WorkManager, Navigation — 필요할 때마다 dependency 추가.
- **서드파티**: Retrofit, OkHttp, Coil, Hilt 등.

## 프로젝트/모듈 구조 (멀티모듈)

웹의 모노레포(Yarn/npm workspaces, Turborepo)와 동일한 구조.

- **`settings.gradle.kts` (루트)**: 어떤 모듈들로 구성되는지 선언. `include(":app", ":core-network", ":feature-login")`
- **루트 `build.gradle.kts`**: 모든 모듈 공통 설정 (플러그인 버전 등). 모노레포 루트 `package.json`의 공통 devDependencies와 유사.
- **`app/build.gradle.kts` (모듈 레벨)**: 그 모듈 전용 설정 — `applicationId`, 버전, 이 모듈만의 dependencies.

멀티모듈로 나누는 이유: (1) 재사용성 — 네트워크/디자인 시스템 등을 라이브러리 모듈로 분리해 다른 프로젝트에서도 재사용, (2) 빌드 속도 — 모듈 단위 병렬 컴파일·캐싱 (Turborepo의 "바뀐 패키지만 재빌드"와 동일 원리), (3) 관심사 분리 — 팀/기능 단위로 모듈 분리.

## Gradle 자체의 정체

번들러(Vite)라기보다 **빌드 시스템 전체**. webpack(번들링) + npm scripts(빌드/테스트 명령) + make(태스크 의존성 그래프)를 합친 것에 가까움. Kotlin/Java 컴파일, 리소스 병합, 의존성 관리, 최종 APK/AAB 패키징까지 담당.

- **R8**(구 ProGuard): 코드 축소·난독화로 APK 용량 절감. Vite/Rollup의 프로덕션 minify와 같은 역할.
- Gradle엔 HMR 개념이 없음. 대신 Live Edit / Apply Changes로 비슷하게 흉내냄.

## IDE 단축키

- 레이아웃 XML을 코드로 보기: 에디터 우측 상단 Code / Split / Design 버튼. 순환 단축키 `Ctrl+Shift+→`. 기본 모드는 Settings > Editor > Design Editors > Default Editor Mode에서 Code 또는 Split으로.
- 레이아웃 파일 생성: `res/layout` 우클릭 > New > Layout Resource File. 이름은 소문자+밑줄(`activity_detail.xml` → `ActivityDetailBinding`).

- **Import 자동 추가**: 빨간 줄에 커서 놓고 `Option + Enter`(맥) / `Alt + Enter`(윈도우). 파일 전체 한번에 정리: `Cmd + Option + O`(맥) / `Ctrl + Alt + O`(윈도우).
- **코드 포맷팅**: `Cmd + Option + L`(맥) / `Ctrl + Alt + L`(윈도우). 저장할 때 자동 포맷: `Settings → Tools → Actions on Save → Reformat code` 체크.

---
