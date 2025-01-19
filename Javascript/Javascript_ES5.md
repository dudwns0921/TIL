# Javascript

## ES5

### 개요

ECMAScript(ES5나 ES2015의 `ES`는 ECMAScript의 줄임말이다.)는 [Ecma 인터내셔널](http://www.ecma-international.org/)에서 정의한 **ECMA-262 기술 규격에 정의된 표준 스크립트 프로그래밍 언어**이다. ECMAScript는 1997년에 1판이 배포되고 그 뒤로 매년 2판, 3판이 배포되었다. 그 뒤 10년 뒤에 5판(ECMAScript 5 이하 ES5)가 배포되었다. 이전엔 배포 주기가 길었지만, 빠르게 변화하는 개발 환경을 반영하여 숫자 대신 연도를 붙여 배포된다.

ES5는 자바스크립트의 첫 메이저 버전이며 아래와 같은 기능들이 추가되었다.

- Strict Mode(엄격 모드)

  - 암묵적인 전역 변수 생성 금지.

  - 단순 함수 내부에서 `this`의 값이 `undefined`가 될 수 있도록 제한

  - 예약어 사용 제한(예: `arguments`, `eval` 등)

  - ```js
    "use strict";
    
    function showThis() {
      console.log(this);
    }
    
    showThis(); // undefined
    
    function myFunction() {
      // 암묵적 전역 변수 금지
      x = 10; // ReferenceError: x is not defined
    }
    myFunction();
    
    // 예약어 사용 금지
    var private = 42; // SyntaxError: Unexpected strict mode reserved word
    ```

- Object 관련 기능

- Array 관련 기능 추가

- JSON 객체 추가

- 객체 setter, getter 추가

- bind() 함수 추가

  - 함수의 `this` 값을 고정한 새로운 함수를 반환

- 오류 디버깅을 쉽게 하기 위해 오류 객체에 스택 추적 및 메시지 기능 추가

### ES5에서 ES6

ES5가 배포된 6년 뒤인 2015년에 6판(ECMAScript 2015)이 배포되었다. 6판의 정식 명칭은 ECMAScript 6가 아닌 **ECMAScript 2015**(이하 ES6)이다. ES6에서는 ES5에서 문제가 되었던 부분들이 해결되었고, 기존 코드를 더 간결하게 작성할 수 있는 새로운 문법이 추가되면서 더 가독성 및 유지 보수성이 향상되었다. 그 덕에 웹에서 사용하는 자바스크립트 유명 라이브러리들(lodash, React, Vue 등)의 개발 환경도 ES6로 바뀌었다.

### 개선된 기능들

여러 개선된 기능들이 있으나, 실제 ES6를 사용하면서 좋다고 느낀 기능들 위주로 정리했다.

#### 기능적인 부분

- 언어의 동작이나 새로운 가능성을 열어주는 부분

##### let, const

- ES5에서는 `var` 키워드를 이용해서 변수를 선언

- `var`로 선언한 변수의 값은 언제나 변경할 수 있기 때문에 변경 불가능한 상수 변수를 선언할 방법이 없었음

- 일반 변수와 구분하기 위해 상숫값에 대한 명명 규칙을 영문 대문자와 언더 스코어로만 제한하는 방식을 많이 사용

- 타 언어들과는 달리 자바스크립트에서 `var`로 선언한 변수는 함수 단위의 스코프를 갖기 때문에 `if`문이나 `for`문 블록 내에서 `var`를 선언한 변수들도 블록 외부에서 접근 가능

  - ```js
    function sayHello(name) {
      if (!name) {
        var errorMessage = '"name" parameter should be non empty String.';
        
        alert(errorMessage);
      }
      
      console.log('Hello, ' + name + '!');
      console.log(errorMessage); // '"name" parameter should be non empty String.'
    }
    ```

- `var`를 이용하면 선언 전에 변수의 사용이 가능한 호이스팅(hoisting)도 발생

  - 인터프리터가 코드를 실행하기 전에 함수, 변수, 클래스 또는 임포트(import)의 선언문을 해당 범위의 맨 위로 끌어올리는 것처럼 보이는 현상

  - ```js
    here = '여기야~';    // 변수 초기화가 먼저 되있지만 에러가 발생하지 않는다.
    
    console.log(here); // '여기야~'
    
    var here;          // 변수 선언은 이부분에 있다.
    ```

##### 클래스

- 클래스 기반의 언어와는 달리 자바스크립트에서는 프로토타입 객체를 재사용하면서 클래스와 유사한 형태의 API를 만들어서 사용해옴
- ES5 환경에서 클래스를 구현하는 방법은 라이브러리마다 달랐지만 ES6부터 자바스크립트에 클래스 문법이 추가되었고, 라이브러리들도 클래스 문법을 사용하면서 구현과 사용법도 한가지로 통일

**Rest 파라미터**

- 함수의 인자 개수를 가변적으로 받아 배열로 처리할 수 있도록 함.

- ```js
  function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
  }
  console.log(sum(1, 2, 3, 4)); // 10
  ```

**Spread 표현식**

- 배열 또는 객체를 펼쳐서 복사하거나, 병합할 때 사용.

- ```js
  const arr1 = [1, 2, 3];
  const arr2 = [...arr1, 4, 5];
  console.log(arr2); // [1, 2, 3, 4, 5]
  ```

**디스트럭처링**

- 배열 또는 객체의 값을 추출해 변수에 쉽게 할당할 수 있도록 함.

- ```js
  const [a, b] = [1, 2];
  const { x, y } = { x: 10, y: 20 };
  console.log(a, b, x, y); // 1 2 10 20
  ```

##### 프로미스

- 프로미스는 비동기 처리가 추상화된 객체

- 사용자가 작성한 비동기 처리가 완료되거나 실패되었는지 알려주고 비동기 처리 결괏값을 반환

- 이를 통해 성공 시 실행할 함수, 실패 시 실행할 함수를 등록해서 편리하게 비동기 처리 코드 작성이 가능

- 프로미스를 이용하면 비동기 처리를 위한 콜백 함수들로 여러 겹 감싸진 콜백 지옥 코드를 간결하게 작성할 수 있음

- ```js
  doSomething(function(result) {
    doSomethingElse(result, function(newResult) {
      doThirdThing(newResult, function(finalResult) {
        console.log('Got the final result: ' + finalResult);
      }, failureCallback);
    }, failureCallback);
  }, failureCallback);
  ```

- ```js
  doSomethingPromise
    .then((result) => doSomethingElse(result))
    .then((newResult) => doThirdThing(newResult))
    .then((finalResult) => console.log('Got the final result: ' + finalResult))
    .catch(failureCallback);
  ```

##### 모듈

- ES5에서는 모듈 시스템이 자바스크립트 언어 자체에 내장되어 있지 않았음
- 그 때문에 Node.js를 포함한 자바스크립트 생태계에서는 **CommonJS** 모듈 시스템이 사실상의 표준처럼 사용됨
- ES6(ES2015)부터 자바스크립트에 **ECMAScript Modules(ESM)**이라는 표준 모듈 시스템이 도입

###### CommonJS

- CommonJS는 서버사이드 환경(Node.js)에서 자바스크립트 파일을 모듈처럼 사용하기 위해 도입된 모듈 시스템

- 모든 모듈은 **`require`** 키워드를 사용해 가져오고, **`module.exports`** 또는 **`exports`** 키워드를 사용해 내보냄

- ```js
  // math.js (모듈 정의)
  module.exports.add = (a, b) => a + b;
  
  // main.js (모듈 사용)
  const math = require('./math');
  console.log(math.add(2, 3)); // 5
  ```

###### ECMAScript Modules (ESM, ES6에서 사용)

- **`import`**와 **`export`** 키워드를 사용해 모듈을 가져오거나 내보냄

- ```js
  // math.js (모듈 정의)
  export const add = (a, b) => a + b;
  
  // main.js (모듈 사용)
  import { add } from './math.js';
  console.log(add(2, 3)); // 5
  ```

#### 코드 작성시의 편의성

- 코드 작성과 가독성을 높이는 sugar syntax에 해당

##### 화살표 함수

- 화살표 함수는 `this` 바인딩 이슈를 해결해주고, 함수 표현식의 긴 문법을 좀 더 단축해줌

- ```js
  const numbers = [1, 2, 3];
  const doubled = numbers.map(num => num * 2);
  console.log(doubled); // [2, 4, 6]
  ```

##### 템플릿 리터럴

- 템플릿 리터럴은 내부에 표현식을 바로 작성하여 더욱더 간결한 문법으로 구현 가능

- ```js
  const name = 'Alice';
  console.log(`Hello, ${name}!`); // Hello, Alice!
  ```

##### async/await

- async 함수를 이용해서 비동기 처리를 더욱더 간결하게 작성 가능

- async 함수는 여러 개의 프로미스를 사용하는 코드를 동기 함수 실행과 비슷한 모습으로 사용할 수 있게 해줌

- async 키워드가 앞에 붙은 함수 선언문의 함수 본문에는 await 식이 포함될 수 있음

- 이 await 식은 async 함수 실행을 일시 중지하고 표현식에 전달된 프로미스의 해결을 기다린 다음 async 함수의 실행을 재개하고, 함수의 실행이 모두 완료된 뒤에 값을 반환

-  await 식은 async 함수 내에서만 유효

- ```js
  const fetchData = async () => {
    try {
      const data = await new Promise((resolve, reject) => {
        setTimeout(() => resolve("Data loaded"), 1000);
      });
      console.log(data); // Data loaded
    } catch (error) {
      console.error(error);
    }
  };
  
  fetchData();
  ```

### ES5에서 주의해야 할 점?

- 변수 선언
  - var로만 변수 선언이 가능하기 때문에 var가 함수 스코프인 점, 언제나 값이 변경 가능하다는 점을 유의
- 화살표 함수
  - this 바인딩에 주의
- 템플릿 리터럴
  - 문자열 연결 방식으로 변수와 문자열을 연결해야 함
- 클래스
  - 프로토타입 방식으로 클래스와 메서드를 정의해야 함
- 모듈 시스템
  - require, module.exports 사용해야 함
- 프로미스
  - 콜백 함수로 비동기 처리를 해야함

# :books:참고자료

- https://ui.toast.com/fe-guide/ko_ES5-TO-ES6#let-const%EC%9D%98-%EC%9E%A5%EC%A0%90
- https://www.w3schools.com/js/js_es5.asp
- https://developer.mozilla.org/ko/docs/Glossary/Hoisting

