# FlowType

## Settings

```json
  "javascript.validate.enable": false,
  "flow.useNPMPackagedFlow": true,
```

vsc의 설정에서 두 가지 옵션을 설정해주어야 한다.

### javascript.validate.enable

이 옵션은 VSC의 내장 언어 서비스에서 제공하는 내장 JavaScript 유효성 검사를 비활성화한다. 이 옵션을 비활성화하는 것은 프로젝트에서 JavaScript 유효성 검사 및 유형 검사를 처리하도록 구성된 Flow 또는 ESLint와 같은 별도의 도구가 있을 때 충돌이나 중복을 방지하기 위해서이다.

### flow.useNPMPackagedFlow

이 옵션은 VSC의 Flow  Language Support가 프로젝트에서 npm 패키지로 설치된 Flow 버전을 사용하도록 지시한다. 이렇게 하면 Flow 버전이 프로젝트의 종속성에 지정된 버전과 일치하고 프로젝트에서 작업하는 여러 환경 또는 팀 구성원 간에 일관성을 유지하는 데 도움이 된다.
