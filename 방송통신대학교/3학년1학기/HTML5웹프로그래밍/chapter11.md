# HTML5웹프로그래밍

## 11강. 문서 객체 모델 & 브라우저 객체 모델

### 문서 객체 모델

- DOM
  - 문서 객체
    - HTML 문서의 각 요소를 자바스크립트에서 사용할 수 있도록 객체로 만든 것
  - DOM
    - 브라우저가 HTML 문서에 접근할 수 있도록 정의해 놓은 표준 모델
    - HTML 문서를 분석하고 표시하는 방식
    - 웹 문서를 각 요소를 객체로 만들어서 그 문서를 분석하고 조작할 수 있도록 하는 모델 
  - 문서가 적재되면 브라우저는 정적으로 DOM 생성
    - 계층적인 구조를 갖는 트리로 표현
    - DOM 트리
    - 자바스크립트를 이용하면 프로그램 실행 중에 웹 문서의 내용, 구조 및 스타일에 대한 작업 가능
      - 결과가 즉각적으로 화면에 반영됨

- DOM 트리

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>
  <body>
      <h1 id="title">
          HTML DOM
      </h1>
  </body>
  </html>
  ```

  - 트리 구조
    - document
      - head, body - 요소 노드
        - h1 - 요소 노드
          - id="title" - 속성 노드
          - HTML DOM - 텍스트 노드

#### DOM 객체의 접근 방법

- id 속성을 이용한 방법
- 요소명을 이용한 방법
- 클래스명을 이용한 방법

#### 요소의 내용 수정

- innerHTML 속성
  - HTML 형식으로 요소 내용을 다룰 때 사용
- textContent 속성
  - HTML 요소와 속성을 제외하고 텍스트 내용만 가져오는 경우
- 요소의 속성 수정
  - imgElement.src 등으로 접근 가능
- 요소의 스타일 수정
  - style.CSS속성명
  - CSS 속성명은 카멜케이스로

#### 기존 HTML 문서에 새로운 요소의 삽입

- 삽입하려는 요소의 텍스트 내용 완성
  - createTextNode 메서드 사용
  - 요소가 생성되지 않고 텍스트 내용만 생성이 됨

#### 기존 HTML 요소의 삭제

- 삭제 과정
  - DOM 구조에서 삭제하려는 노드의 부모 노드를 찾은 후
  - removeChild() 메서드 적용

### 브라우저 객체 모델

- BOM
  - 브라우저를 객체로 표현한 것
  - window : 표준이 존재하지 않음. 브라우저마다 객체나 메서드가 다를 수 있음
    - document : DOM 객체의 최상위 객체
    - history :  사용자가 방문한 URL을 저장, 관리
    - location : 현재 URL에 대한 정보를 유지
    - navigator : 현재 사용 중인 브라우저에 대한 정보를 관리
    - screen : 스크린 장치에 대한 정보 관리

#### window 객체

- 창에 대한 전반적인 모든 상황을 제어하는 최상위 객체
  - 각 윈도우마다 하나의 window 객체가 생성
  - 주요 메서드
    - open, close
      - open
        - HTML 문서의 URL
        - HTML 문서가 열릴 창
          - _blank, _self
        - 윈도우 속성 리스트
    - setInterval
      - 일정한 시간 간격으로 주어진 함수를 무한히 반복 호출
    - setTimeout
      - 함수 안에  setTimeout을 사용해 해당 함수를 다시 호출하면, 재귀적 사용으로 반복해서 실행시킬 수 있다.
      - 일정한 시간이 지난 후 한 번만 호출
    - alert
    - confirm
    - prompt
    - moveBy, moveTo
    - resizeBy, resizeTo
