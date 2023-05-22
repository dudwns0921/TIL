# jsDoc

회사에서 typescript를 사용하지 않는 프로젝트 관련 작업을 진행하다가 '이래서 typescript를 사용해야 하는구나' 라는 생각이 들 정도로 불편한 점들이 꽤 많이 느껴졌다. 그래서 비슷한 효과를 낼 수 있는 방법이 없을까 고민하다가 jsDoc을 사용한다면 프로젝트 자체에는 전혀 영향을 주지 않으면서 간단한 타입 체크와 자동 완성 정도는 가능하겠다는 생각이 들었다.

## jsDoc 작성

```js
// @ts-check 이 주석을 통해 내장 typescript-parser에게 타입 체크를 수행하도록 지시할 수 있다.

/**
 * @typedef Person - person object data
 * @property {string} name - name of person
 * @property {number} age - age of person
 */

/**
 *
 * @param {Person} person - person
 */
function printPerson(person) {
  console.log(person.name, person.age, person.sex);
}

```

이렇게만 작성해도 vsc의 내장된 typescript-parser가  자동으로 타입 체크를 수행한다. 결과적으로 sex 라는 속성이 없기 때문에 아래와 같이 빨간선이 생기며 타입 체크에서 오류가 발생한 것을 확인할 수 있다. 

![image-20230520202138435](.\md-images\image-20230520202138435.png)	

그런데 jsDoc을 계속 동일 파일 내에서 작성할 수는 없는 노릇이다. 특히나 파일에서 필요한 typedef를 모두 작성한다면 jsDoc으로 뒤덮인 파일이 되버릴 것이다. 그러니까 여기서는 typedef를 별도로 정의하는 것이 필요하다.

## typedef 별도 정의

위에서 간단한 주석만으로 타입 체크가 이루어진 것은 vsc의 덕분이었다. 이와 마찬가지로 typedef를 별도로 정의하기 위해서는 vsc의 도움이 필요하다.

```js
// person.js

/**
 * @typedef Person - person object data
 * @property {string} name - name of person
 * @property {number} age - age of person
 */

export default {}
```

```js
// main.js

// @ts-check

/**
 * @typedef {import('./types/person').Person} Person
 */

/**
 *
 * @param {Person} person - person
 */
function printPerson(person) {
  console.log(person.name, person.age, person.sex);
}
```

위와 같이 Person typedef를 별도의 파일에 정의하고 그 파일을 모듈로서 export한다. 그리고 해당 typedef가 필요한 파일에서 import 구문을 통해 typedef를 가져와 사용하면 된다. 이 방법이 가능한 이유는 vsc의 jsDoc parser가 import 구문을 인식하고 가져온 유형을 기반으로 유형 유추 및 자동 완성을 제공하기 때문이다. 

![image-20230520203417134](.\md-images\image-20230520203417134.png)	

그럼 아까와 같이 동일한 타입 체크가 이루어져 오류가 발생한 걸 확인할 수 있다. 

## 마무리

이번 작업을 통해 vsc가 정말 사용자를 위해 많은 걸 해주고 있다는 걸 새삼 느끼게 되었다. 사실상 내가 한 건 주석을 단 것밖에 없는데 타입스크립트와 비슷한 효과를 낼 수 있다니 말이다. 물론 실제로 타입스크립트를 사용하는 것과는 많은 차이가 있겠지만, 그래도 이미 만들어진 프로젝트에 영향을 주지 않으면서 일정 타입 체크를 수행할 수 있다는 건 꽤나 유용하다고 생각한다.
