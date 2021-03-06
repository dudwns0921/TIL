# Prototype

Java, C++과 같은 클래스 기반 객체지향 프로그래밍 언어와 달리 자바스크립트는 프로토타입 기반 객체지향 프로그래밍 언어이다. 따라서 자바스크립트의 동작 원리를 이해하기 위해서는 프로토타입의 개념을 잘 이해하고 있어야 한다.

클래스 기반 객체지향 프로그래밍 언어는 객체 생성 이전에 클래스를 정의하고 이를 통해 객체(인스턴스)를 생성한다. 하지만 프로토타입 기반 객체지향 프로그래밍 언어는 클래스 없이도 객체를 생성할 수 있다.

## 자바스크립트의 객체 생성 방법

자바스크립트의 모든 객체는 자신의 부모 역할을 담당하는 객체와 연결되어 있다. 그리고 이것은 마치 객체 지향의 상속 개념과 같이 부모 객체의 프로퍼티 또는 메소드를 상속받아 사용할 수 있게 한다. 이러한 부모 객체를 **Prototype(프로토타입) 객체** 또는 줄여서 Prototype(프로토타입)이라 한다.

Prototype 객체는 생성자 함수에 의해 생성된 각각의 객체에 공유 프로퍼티를 제공하기 위해 사용한다.

객체를 생성할 때 프로토타입은 결정된다. 결정된 프로토타입 객체는 다른 임의의 객체로 변경할 수 있다. 이것은 부모 객체인 프로토타입을 동적으로 변경할 수 있다는 것을 의미한다. 이러한 특징을 활용하여 객체의 상속을 구현할 수 있다.

```javascript
const Human = {brain: 1, eyes: 2};
const elio = {};
// 기존에 elio는 객체로 정의되었기 때문에 elio의 프로토타입은 Object이다.
elio.__proto__= Human;
// 이를 Human 객체로 변경해주었다.
elio.brain
1
// 그 결과 Human 객체의 속성을 elio에서도 접근할 수 있게 되었다.
```

## :bulb:Tip

ES6부터 객체 지향 프로그래밍에 익숙한 사람들을 위해 클래스 문법이 추가되어 자바스크립트에서도 클래스 문법을 사용할 수 있다.

# :books:참고자료

[Prototype | PoiemaWeb](https://poiemaweb.com/js-prototype)
