# Vue Router

## 설치하기

> npm install vue-router --save

## 라우터 생성하기

아래 코드들은 vue cli를 사용해 만든 프로젝트의 일부임을 참고바란다.

먼저 라우터를 독립적으로 관리할 수 있도록 router.js 파일을 따로 생성해준다.

```javascript
// router.js

import HomePg from '../pages/HomePg.vue';
import SearchPg from '../pages/SearchPg.vue';
import { createWebHashHistory, createRouter } from 'vue-router';

const routes = [
  { path: '/', component: HomePg },
  { path: '/search', component: SearchPg }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```

```javascript
// main.js

import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router.js';

const myApp = createApp(App);
myApp.use(router);
myApp.mount('#app');
```

라우터를 사용하기 위해서는 총 4단계가 필요하다.

1. 렌더링할 컴포넌트를 임포트한다.

2. 라우트(경로)들을 작성한다.

각각의 경로는 객체로 이루어져있으며, path와 component 속성을 갖는다. path에는 url를, component에는 해당 주소에서 렌더링할 컴포넌트를 적어주면 된다.

3. createRouter() 메서드를 통해 라우터를 생성한다.

여러 옵션을 정의할 수 있지만 공식 문서에서 가장 기본적인 옵션인 history와 routes를 정의하고 있다. 

routes, 는 routes: routes을 줄인 것으로 객체의 속성과 값이 같을 때 축약해서 작성할 수 있다. 

4. main.js에서 router을 임포트하고 use() 메서드로 라우터를 사용한다.

이제 라우터는 정상적으로 만들어졌다. 해당 라우터를 사용하기 위해서 App.vue 파일로 가보자.

## 렌더링

```html
<!-- app.vue -->

<template>
  <div class="app">
    <router-view></router-view>
  </div>
</template>
```

use를 통해 라우터를 사용한 컴포넌트에서 router-view 태그를 선언하면 URL에 맞게 컴포넌트들이 맵핑된다.

## 라우터 링크

사용자에게 라우팅 된 경로로 이동하게끔 앵커태그를 생성하는 속성이다. `router-link`속성을 통해 앵커 태그 기능을 수행하게한다.

```html
<router-link to="/">Home</router-link>
```

## 스타일링

`scoped`속성을 통해 에서 해당 컴포넌트에서만 독립하게 사용하는 스타일을 입힐 수 있는데, 라우터 링크에서 사용되는 앵커태그의 기본 값은 `router-link-exact-active`이며, active-class속성을 통해 따로 정의할 수도 있다.

위에 작성한 코드를 스타일링한다고 가정해보자.

```html
<style>
.router-link-exact-active{
    text-decoration: none;
}    
</style>
```

## 코드 스플리팅

SPA는 웹 사이트의 전체 페이지를 하나의 페이지에 담아 동적으로 화면을 바꿔가며 표현하는 애플리케이션이다. SPA의 단점은 최초에 전체 페이지를 모두 받아오기 때문에 최초 로딩 시간이 오래 걸린다는 점이다. 이러한 단점을 코드 스플리팅을 통해 해결할 수 있다. 

```js
// src/router/index.js

...
routes: [
        {
            path: '/login',
            component: () => import ('@/views/LoginPage.vue'),
        },
        {
            path: '/signup',
            component: () => import ('@/views/SignupPage.vue'),
        },
    ]
...
```

component의 LoginPage를 바로 넣는 게 아니라 화살표함수를 이용해서 코드 스플리팅을 한다. 이렇게 하면 최초에 모든 파일을 다 들고오지 않고 해당 url 로 이동했을 때 필요한 JS 파일을 그 때 그 때 들고 오게 된다. (다이나믹 임포트)

## Navigation guard

네비게이션 가드는 특정 URL에 접근(Navigation) 하기 전에 불려지는 훅(Hook)의 일종으로, 다른 페이지로 우회 하거나 접근 자체를 취소시킬 수 있기 때문에 네비게이션 가드라고 불린다.

사용자의 권한에 따라 페이지 접근을 막거나 페이지를 로딩하기 전에 데이터를 미리 불러올 때 사용하기 좋은 기술이다. 

### 전역 가드

전역 가드는 모든 라우팅에 적용되는 네비게이션 가드이다. 라우터의 `beforeEach`라는 메소드를 통해 전역가드의 로직을 설정할 수 있다. 아래는 전역 가드를 설정하는 예시 코드이다.

```javascript
var router = new VueRouter();

router.beforeEach(function(to, from, next) {
  // ...
});
```

뷰 라우터 인스턴스를 하나 생성하고 해당 인스턴스를 참조하는 변수에 `beforeEach()` API를 호출한다. 인자로 받은 3개의 변수는 다음과 같은 역할을 합니다.

- to : 이동할 url
- from : 현재 url
- next : to에서 지정한 url로 이동하기 위해 꼭 호출해야 하는 함수

### :bulb:TIP

next 함수 인자에 따라서 라우팅 허용 여부가 달라진다.

- next() : 라우팅 승인

- next(false) : 라우팅 취소

- next(url) : 특정 라우트로 진입, route.push와 같은 역할을 한다고 생각하면 된다.

주의할 점은 어떠한 경우에도 next()를 호출해야한다는 점이다. 호출되지 않을 경우 라우팅이 진행되지 않고 대기 상태에 빠진다.

## Named Routes

route에는 path와 더불어 name 속성을 제공해줄 수 있다. name 속성은 다음과 같은 장점을 가진다.

- url 하드코딩 필요 없음
- url 오타 방지
- params에 대한 자동 인코딩 / 디코딩
- 경로 순위 우회 가능

```js
const routes = [
  {
    path: '/user/:username',
    name: 'user',
    component: User
  }
]
```

```vue
<router-link :to="{ name: 'user', params: { username: 'erina' }}">
  User
</router-link>
```

named route를  router-link에 사용하기 위해서는 router-link의 to 속성에다가 route 객체를 전달해주면 된다. 

```js
router.push({ name: 'user', params: { username: 'erina' } })
```

위와 같이 해당 route 객체를 push 메서드에 전달해 같은 결과를 얻을 수 있다.

# :books:참고자료

[Getting Started | Vue Router](https://router.vuejs.org/guide/)

[Vue 라우터 개념 및 사용방법](https://jinyisland.kr/post/vue-router/)
