# Vue

## Composable

- 정의
  - Vue Composition API를 활용하여 stateful한 로직을 캡슐화하고 재사용하는 함수

### Best Practice

#### Parameter	

- ```js
  const title = useTitle('Product Page', { observe: true, 
                                           titleTemplate: '%s | Socks Store' })
  ```

  - Best Practice
    - 필수 인자들은 개별로 작성, 선택 인자들은 하나의 options 객체에 담아 작성
  - 내부에서 사용 시 구조 분해 할당 사용

#### Flexible Arguments

- composable에 ref, 원시 타입 어떤 걸 input으로 넣어도 Ref를 반환하도록 구성하기
- vueUse 참조하기
  - useTitle
  - useCssVar

#### Dynamic Return Values

- controls option을 통해 return 값을 동적으로 설정하기

#### Start with the Interface

- composable에 어떤 인자를 전달할 것인가?
- options 객체에는 어떤 값들이 있어야 하는가?
- composable이 반환하는 값은 어떤 것인가?

#### Async Without Await

- setup에서 모든 비동기 코드들은 reactive와 관련된 로직 이후에 실행되어야 함
- 그렇지 않으면 reactivity에 문제가 생길 수 있음
- 이를 해결하기 위해 async 함수를 await 없이 사용해 비동기 로직을 처리하더라도 reactivity에는 문제가 없도록 함