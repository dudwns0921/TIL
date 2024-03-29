# JWT

## 쿠키를 이용한 토큰 관리

포털 사이트를 이용하다보면 로그인 상태가 여러 웹 페이지에 걸쳐서 계속 유지되는 것을 볼 수 있다. 하지만 실제 HTTP 프로토콜 방식으로 통신하는 웹 페이지들은 서로 어떤 정보도 공유하지 않는다(stateless 방식). 그래서 사용자 입장에서 웹 페이지 사이의 상태나 정보를 공유하려면 프로그래머가 세션 트래킹이라는 웹 페이지 연결 기능을 구현해야 한다.

세션 트래킹을 구현하는 방법에는 여러 가지가 있지만 이번에는 클라이언트의 쿠키 파일에 정보를 저장하는 방식을 통해 구현해보도록 하겠다.

## 기존 코드

```javascript
// src/store/index.js

import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      username: '',
      token: '',
    };
  },
```

```javascript
// LoginForm.vue

methods: {
  async submitForm() {
    try {
      const userData = {
        username: this.username,
        password: this.password,
      };
      const { data } = await loginUser(userData);
      this.$store.commit('setToken', data.token);
// loginUser 메서드를 통해 서버에 Post 요청을 보낸다.
// 이를 통해 받아온 data에서 토큰 값을 store의 state에 할당하는 과정이다.
```

vue 프로젝트를 예시로 들어 설명해보겠다. 먼저 vue에는 state를 관리할 수 있는 vuex라는 라이브러리가 존재한다. 이 라이브러리로 store라는 저장소를 만들어 state를 관리하는 것이다. 위 코드에서는 토큰값, 즉 세션 트래킹을 해야하는 데이터가 Store에만 저장되어 있기 때문에 새로고침이나 페이지 이동이 일어날 때마다 해당 값은 초기화되버린다.

## Cookies

위의 문제를 쿠키를 사용해 해결해보자.

```js
// src/utils/cookies.js

function saveAuthToCookie(value) {
  document.cookie = `auth=${value}`;
}

function saveUserToCookie(value) {
  document.cookie = `user=${value}`;
}

function getAuthFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)auth\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getUserFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)user\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function deleteCookie(value) {
  document.cookie = `${value}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

export {
  saveAuthToCookie,
  saveUserToCookie,
  getAuthFromCookie,
  getUserFromCookie,
  deleteCookie,
};
```

```js
// LoginForm.vue

<script>
    ...
    import { saveAuthToCookie, saveUserToCookie } from '@/utils/cookies';

    export default {
        ...
        methods: {
            async submitForm() {
                try {
                    ...
                    const { data } = await loginUser(userData);
                    this.$store.commit('setToken', data.token);
                    this.$store.commit('setUsername', data.user.username);
                    saveAuthToCookie(data.token);
                    saveUserToCookie(data.user.username);
                    this.$router.push('/main');
                } catch (error) {
                    ...
                } finally {
                    ...
                }
            }
        }
    }
</script>
```

loginUser메서드를 통해 서버로부터 가져오는 `token` 값과 `user.username` 값을 Cookies 에 저장한다.

```js
// src/store/index.js

...
import { getAuthFromCookie, getUserFromCookie } from '@/utils/cookies';
...
export default new Vuex.Store({
    state: {
        username: getUserFromCookie() || '',
        token: getAuthFromCookie() || '',
    },
    getters: {
      ...
    },
    mutations: {
        ...
    },
});
```

Cookies 에 저장되어 있는 값이 있으면 가져와서 Store 에 저장하고, 그렇지 않으면 빈 문자열로 저장한다. 페이지를 새로고침 하더라도 Cookies 에 있는 값으로 Store의 token 에 다시 저장하기 때문에 로그인 상태가 유지됨을 확인할 수 있다. 

# :books:참고자료

인프런 - Vue.js 끝장내기 수업 내용
