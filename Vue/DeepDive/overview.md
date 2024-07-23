# Deep Dive

## Overview

### DOM

- html 작성
- 브라우저가 노드들을 생성
- 웹페이지 로드

이 노드들이 html 태그들과 연결되어있기 때문에 js로 조작 가능

수천개의 DOM 노드들을 업데이트하는 것은 시간이 오래 걸림

이를 위해 Virtual DOM을 도입

### Virtual DOM

Virtual DOM은 단순 js 객체

Vue는 render function을 사용해 Virtual DOM을 반환

업데이트가 생기면 render function이 다시 실행되면서 새로운 Virtual DOM을 새롭게 생성

둘을 비교해서 가장 효율적인 방법으로 업데이트

### Core Engine

- reactivity module
  - 반응성 객체 만드는 데 사용
- compiler module
  - HTML 템플릿을 render function으로 만들어줌
  - 이 과정은 두 경우에 발생
    - 브라우저 런타임
    - Vue 프로젝트 빌드시
      - 거의 이 경우에 발생
      - 브라우저는 render function만 받음
- renderer module
  - render phase
    - render function으로 virtual DOM 노드 반환
  - mount phase
    - virtual DOM 노드로 웹페이지 생성
  - patch phase
    - 업데이트된 virtual DOM을 기존 virtual DOM과 비교해 웹페이지의 일부만 업데이트

# :books:참고자료

- https://www.vuemastery.com/courses/vue3-deep-dive-with-evan-you/vue3-overview



