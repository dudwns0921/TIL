# ๐งฉ์ปดํฌ๋ํธ

์ปดํฌ๋ํธ๋ ํ๋ฉด์ ์์ญ์ ๊ตฌ๋ถํ์ฌ ๊ฐ๋ฐํ  ์ ์๋ ๋ทฐ์ ๊ธฐ๋ฅ์ด๋ค. ์ปดํฌ๋ํธ ๊ธฐ๋ฐ์ผ๋ก ํ๋ฉด์ ๊ฐ๋ฐํ๊ฒ ๋๋ฉด ์ฝ๋์ ์ฌ์ฌ์ฉ์ฑ์ด ์ฌ๋ผ๊ฐ๊ณ  ๋น ๋ฅด๊ฒ ํ๋ฉด์ ์ ์ํ  ์ ์๋ค.

## ๐์ฑ๊ธ ํ์ผ ์ปดํฌ๋ํธ

Vue์์ ์ปดํฌ๋ํธ๋ฅผ ๋ง๋ค ๋๋ ์ฑ๊ธ ํ์ผ ์ปดํฌ๋ํธ๋ผ๋ ๋ฐฉ์์ ์ฌ์ฉํ๋ค. ์ฑ๊ธ ํ์ผ ์ปดํฌ๋ํธ๋ ํ๋ฉด์ ํน์  ์์ญ์ ๋ํ HTML, CSS, JS ์ฝ๋๋ฅผ ํ ํ์ผ์์ ๊ด๋ฆฌํ๋ ๋ฐฉ๋ฒ์ด๋ค. ๋ทฐ CLI๋ก ํ๋ก์ ํธ๋ฅผ ์์ฑํ๊ณ  ๋๋ฉด App.vue๋ผ๋ ํ์ผ์ ํ์ธํ  ์ ์๋ค. ์ด์ฒ๋ผ vue ํ์ฅ์๋ฅผ ๊ฐ์ง ํ์ผ์ ๋ชจ๋ ์ฑ๊ธ ํ์ผ ์ปดํฌ๋ํธ๋ผ๊ณ  ํ๋ค.

์ฑ๊ธ ํ์ผ ์ปดํฌ๋ํธ๋ ๋ทฐ ๋ก๋์ ์ํด HTML, CSS, JS์ ๊ฐ์ ์น ์์์ผ๋ก ๋ถ๋ฆฌ๋์ด ์คํ๋๋ค.ย [๋ทฐ ๋ก๋ย (opens new window)](https://vue-loader.vuejs.org/guide/)๋ ์นํฉ์ ๋ก๋ ์ข๋ฅ ์ค ํ๋์ด๊ณ  ๋ทฐ CLI๋ก ํ๋ก์ ํธ๋ฅผ ์์ฑํ๋ฉด ๊ธฐ๋ณธ์ ์ผ๋ก ์ค์ ์ด ๋์ด ์๋ค.

## ๐์ปดํฌ๋ํธ ์ฌ์ฉํด๋ณด๊ธฐ

๊ธฐ๋ณธ์ ์ผ๋ก App.vue๋ผ๋ ๋ฐํ์ด ๋๋ ์ปดํฌ๋ํธ์ ์ฌ๋ฌ ์ปดํฌ๋ํธ๋ฅผ ๋ถํ์ฒ๋ผ ๋ผ์ ๋ฃ์ด์ ํ๋์ ํฐ ํ๋ก์ ํธ๋ฅผ ๋ง๋ ๋ค๊ณ  ์๊ฐํ๋ฉด ๋๋ค. ๊ทธ๋ฌ๋ฉด ๊ฐ๋จํ ์ปดํฌ๋ํธ๋ฅผ ๋ง๋ค๊ณ  App.vue์์ ํด๋น ์ปดํฌ๋ํธ๋ฅผ ์ฌ์ฉํ๋ ๋ฐฉ๋ฒ์ ๋ํด์ ์์๋ณด์.

```html
<!-- HeaderComponent.vue -->

<template>
  <>header</div>
</template>

<script>
export default {
  name: 'HeaderComponent',
};
</script>

<style></style>
```

vue ํ์ฅ์๋ฅผ ๊ฐ์ง ๊ฐ๋จํ ํค๋ ์ปดํฌ๋ํธ๋ฅผ ๋ง๋ค์ด๋ณด์๋ค. 

```html
<!-- App.vue -->

<template>
  <div>Hi</div>
  <header-component></header-component>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

 App.vue์์ ์ปดํฌ๋ํธ๋ฅผ importํ๊ณ  script ๋ถ๋ถ์ components์๋ค๊ฐ ํด๋น ์ปดํฌ๋ํธ ์ด๋ฆ์ ์๋ ฅํด์ค๋ค. ๊ทธ๋ฆฌ๊ณ  template์ ํด๋น ์ปดํฌ๋ํธ๋ฅผ ๋ฃ์ด์ฃผ๋ฉด ๋๋๋ฐ, ์ ์ฝ๋์์ importํ ์ปดํฌ๋ํธ์ template์ ์๋ ์ปดํฌ๋ํธ์ ์ด๋ฆ์ด ๋ค๋ฅธ ๊ฑด ํ์ธํ  ์ ์์ ๊ฒ์ด๋ค.

 Vue.js๋ ๋์๋ฌธ์๋ฅผ ์์ด ์ฐ๋ PascalCase์ ์๋ฌธ์ ์ค๊ฐ์ ๋์๋ฅผ ๋ฃ์ด ๊ตฌ๋ถํ๋ kebab-case๋ฅผ ์ง์ํ๋ค. ๋ฐ๋ผ์ Todo๋ก ๋ฑ๋กํ ์ปดํฌ๋ํธ๋ todo๋ก ์ฌ์ฉ ๊ฐ๋ฅํ๊ณ , ์์ ๊ฒฝ์ฐ์๋ HeaderComponent ๋์ ์ header-component๋ก ์ฌ์ฉ ๊ฐ๋ฅํ ๊ฒ์ด๋ค.

## ๐๋ถ๋ชจ-์์ ์ปดํฌ๋ํธ๊ฐ ํต์ 

๋ทฐ ์ปดํฌ๋ํธ๋ ๊ฐ๊ฐ ๊ณ ์ ํ ๋ฐ์ดํฐ ์ ํจ ๋ฒ์๋ฅผ ๊ฐ๋๋ค. ๋ฐ๋ผ์, ์ปดํฌ๋ํธ ๊ฐ์ ๋ฐ์ดํฐ๋ฅผ ์ฃผ๊ณ  ๋ฐ๊ธฐ ์ํด์  ์๋์ ๊ฐ์ ๊ท์น์ ๋ฐ๋ผ์ผ ํ๋ค.

![๋ทฐ ์ปดํฌ๋ํธ ํต์  ๋ฐฉ์](https://joshua1988.github.io/vue-camp/assets/img/component-communication.2bb1d838.png)

## Props

Props ์์ฑ์ ์ปดํฌ๋ํธ ๊ฐ์ ๋ฐ์ดํฐ๋ฅผ ์ ๋ฌํ  ์ ์๋ ์ปดํฌ๋ํธ ํต์  ๋ฐฉ๋ฒ์ด๋ค. Props ์์ฑ์ ๊ธฐ์ตํ  ๋๋ ๋ถ๋ชจ ์ปดํฌ๋ํธ์์ ์์ ์ปดํฌ๋ํธ๋ก ๋ด๋ ค๋ณด๋ด๋ ๋ฐ์ดํฐ ์์ฑ์ผ๋ก ๊ธฐ์ตํ๋ฉด ์ฝ๋ค.

```html
<!--๋ถ๋ชจ ์ปดํฌ๋ํธ-->

<template>
  <!-- ์ ์  ๋ฐ์ดํฐ ์ ๋ฌ -->
  <ChildComponent message="์๋ํ์ธ์! vue"></ChildComponent>
  <!-- ๋์  ๋ฐ์ดํฐ ์ ๋ฌ -->
  <ChildComponent v-bind:message="message"></ChildComponent>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue';

export default {
  name: 'App',
  components: {
    ChildComponent,
  },
  data() {
    return {
      message: '์๋ํ์ธ์! vue',
    };
  },
};
</script> },
};
</script>
```

```html
<!--์์ ์ปดํฌ๋ํธ ChildComponent.vue-->

<template>
  <h1>{{ message }}</h1>
</template>

<script>
export default {
  props: {
    message,
  },
};
</script>

<style></style>
```

๋ถ๋ชจ ์ปดํฌ๋ํธ์์ ์ ์๋ message๋ผ๋ ๋ฐ์ดํฐ๋ฅผ prop์ผ๋ก ChildComponent๋ก ๋ณด๋ด์ฃผ๊ณ  ์๋ค.

์ ์ฝ๋์์๋ ๋ฌธ์์ด์ ์ ๋ฌํ๊ณ  ์์ง๋ง ์ค์ ๋ก ๋ชจ๋  ํ์์ ๋ณ์๊ฐ prop์ผ๋ก ์ ๋ฌ๋  ์ ์๋ค. ์๋๋ฅผ ํ์ธํด๋ณด์.

```html
<ChildComponent v-bind:number="456"></ChildComponent>
```

์์ ๊ฐ์ด v-bind๋ฅผ ํตํด ํด๋น ๊ฐ์ด ๋ฌธ์์ด์ด ์๋ Javascript ํํ์์์ ์๋ ค์ฃผ๊ณ , Boolean, Array, Object ๋ฑ ๋ชจ๋  ํ์์ ์ ๋ฌํ  ์ ์๋ค.

## ์ด๋ฒคํธ ๋ฐ์

์ด๋ฒคํธ ๋ฐ์์ ์ปดํฌ๋ํธ์ ํต์  ๋ฐฉ๋ฒ ์ค ์์ ์ปดํฌ๋ํธ์์ ๋ถ๋ชจ ์ปดํฌ๋ํธ๋ก ํต์ ํ๋ ๋ฐฉ์์ด๋ค. ์์ ์ปดํฌ๋ํธ์์ ์ด๋ฒคํธ๋ฅผ ๋ฐ์ ํ๊ณ  ๋ถ๋ชจ์์ ์์ ํ๋ ๊ฐ๋จํ ์์๋ฅผ ํ ๋ฒ ๋ง๋ค์ด๋ณด๊ฒ ๋ค.

```html
<!--์์ ์ปดํฌ๋ํธ-->

<template>
  <button @click="$emit('sendWarn')">๋๋ฅด๋ฉด ์๋ฆผ ๋ฐ์</button>
</template>

<script>
export default {};
</script>

<style></style>
```

```html
<!--๋ถ๋ชจ ์ปดํฌ๋ํธ-->

<template>
  <child-component v-on:sendWarn="receiveWarn"></child-component>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue';

export default {
  name: 'App',
  components: {
    ChildComponent,
  },
  data() {
    return {};
  },
  methods: {
    receiveWarn: function () {
      alert('์์ ์ปดํฌ๋ํธ์ ์ด๋ฒคํธ ๋ฐ์');
    },
  },
};
</script>

<style>
</style>
```

๋จผ์  ์ ์ฒด์ ์ธ ํ๋ฆ์ ์ดํด๋ณด์.

1. ์์ ์ปดํฌ๋ํธ์ ๋ฒํผ์ ๋๋ฅด๋ฉด ๋ถ๋ชจ ์ปดํฌ๋ํธ๋ก sendWarn์ด๋ผ๋ ์ด๋ฒคํธ๋ฅผ ๋ฐ์ ํ๋ค.

2. ๋ถ๋ชจ ์ปดํฌ๋ํธ์์ ํด๋น ์ด๋ฒคํธ๋ฅผ ์์ ํ๊ณ  receiveWarn์ด๋ผ๋ ๋ฉ์๋๋ฅผ ์คํ์ํจ๋ค.

```vue
<button @click="$emit('sendWarn')">๋๋ฅด๋ฉด ์๋ฆผ ๋ฐ์</button>
```

๊ฐ๊ฐ์ ๊ณผ์ ์ ์ฝ๋๋ฅผ ๋ณด๋ฉฐ ์ข ๋ ์์ธํ ์ดํด๋ณด์.

v-on ๋๋ ํฐ๋ธ๋ฅผ ํตํด ๋ฒํผ์ ํด๋ฆญ ์ด๋ฒคํธ๊ฐ ๋ฐ์ํ  ๋ sendWarn ์ด๋ฒคํธ๋ฅผ ๋ฐ์ ํ๋ค. ์ ์ฝ๋์์๋ button ํ๊ทธ ์์ ์ธ๋ผ์ธ์ผ๋ก ์์ฑํ์ง๋ง, ๋ฉ์๋์ ๋ฐ๋ก ์์ฑํ  ์๋ ์๋ค.

```html
<template>
  <button v-on:click="sendWarn">๋๋ฅด๋ฉด ์๋ฆผ ๋ฐ์</button>
</template>

<script>
export default {
    methods: {
    sendWarn: function() {
        this.$emit('sendWarn');
}
}
};
</script>

<style></style>
```

 ์ด์ ๊ฐ์ด ์ ๋ฆฌํ  ์๋ ์๋ค. ๊ฐ์ธ์ ์ผ๋ก๋ ํ์๊ฐ ์ข ๋ ๊น๋ํ ์ฝ๋๋ผ๊ณ  ์๊ฐํ๋ค.

```html
<template>
  <child-component v-on:sendWarn="receiveWarn"></child-component>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue';

export default {
  name: 'App',
  components: {
    ChildComponent,
  },
  data() {
    return {};
  },
  methods: {
    receiveWarn: function () {
      alert('์์ ์ปดํฌ๋ํธ์ ์ด๋ฒคํธ ๋ฐ์');
    },
  },
};
</script>
```

๋ถ๋ชจ ์ปดํฌ๋ํธ์์๋ `v-on:์์ ์ปดํฌ๋ํธ์์ ๋ฐ์ ํ ์ด๋ฒคํธ๋ช`์ ์๋ ฅํด์ ์ด๋ฒคํธ๋ฅผ ์์ ํ  ์ ์๋ค. ํด๋น ๋๋ ํฐ๋ธ์ ๊ฐ์ผ๋ก ๋ฉ์๋๋ ์ฐ์ฐ์ ํ ๋นํด์ ์ด๋ฒคํธ๊ฐ ๋ฐ์ํ๋ฉด ์์ฑํ ๋ฉ์๋๋ ์ฐ์ฐ์ ์คํ์ํฌ ์ ์๋ค.

### ๋ฐ์ดํฐ ์ ์ก

๋ถ๋ชจ ์ปดํฌ๋ํธ์์ prop์ ํตํด ๋ฐ์ดํฐ๋ฅผ ์ ๋ฌํ๋ฏ์ด ์์ ์ปดํฌ๋ํธ์์๋ ์ด๋ฒคํธ์ ํจ๊ป ๋ฐ์ดํฐ๋ฅผ ์ ์กํ  ์ ์๋ค. ์์ ์์์์๋ ๋จ์ํ ์ด๋ฒคํธ๋ง ๋ฐ์์์ผฐ๋ค๋ฉด, ์ด๋ฒ์๋ ์์ ์ปดํฌ๋ํธ์์ ๊ฒฝ๊ณ ์ฐฝ์ ๋์ธ ๋ฉ์์ง๋ ํจ๊ป ์ ๋ฌํด๋ณด๊ฒ ๋ค.

```vue
<!--์์ ์ปดํฌ๋ํธ-->

<template>
  <div>
    <input v-model="message" type="text" />
    <button @click="sendWarn">๋๋ฅด๋ฉด ์๋ฆผ ๋ฐ์</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
    };
  },
  methods: {
    sendWarn() {
      this.$emit('sendWarn', this.message);
    },
  },
};
</script>

<style></style>
```

์์ ์ปดํฌ๋ํธ๋ ๊ธฐ์กด ์์์ ํฌ๊ฒ ๋ฌ๋ผ์ง ๋ถ๋ถ์ ์๋ค. ๋ค๋ง ์ด๋ฒ์๋ emit ๋ฉ์๋์ ๋ ๋ฒ์งธ ์ธ์๋ก ๊ฒฝ๊ณ ์ฐฝ์ ๋์ธ ๋ฉ์์ง๋ ํจ๊ป ์ ๋ฌํ๊ณ  ์๋ค.

> All extra arguments passed to `$emit()` after the event name will be forwarded to the listener. For example, with `$emit('foo', 1, 2, 3)` the listener function will receive three arguments.

emit ๋ฉ์๋๋ ์ฒซ ๋ฒ์งธ ์ธ์๋ก ์ด๋ฒคํธ๋ช์ ๋ฐ๊ณ , ๊ทธ ์ดํ์ ์ถ๊ฐ๋๋ ๋ชจ๋  ์ธ์๋ค์ ๋ฆฌ์ค๋์ ์ธ์๋ก ์ ๋ฌ๋๋ค. ์์ ์์์์๋ input์ ์์ฑ๋ ๋ฉ์์ง๋ง์ ์ ๋ฌํ๊ณ  ์์ง๋ง, ์ฌ๋ฌ ๊ฐ์ ์ธ์๋ฅผ ์ ๋ฌํ๋ ๊ฒ๋ ๊ฐ๋ฅํ๋ค.

```vue
<!--๋ถ๋ชจ ์ปดํฌ๋ํธ-->

<template>
  <child-component @sendWarn="receiveWarn"></child-component>
</template>

<script>
import ChildComponent from './components/ChildComponent.vue';

export default {
  name: 'App',
  components: {
    ChildComponent,
  },
  data() {
    return {};
  },
  methods: {
    receiveWarn(message) {
      alert(message);
    },
  },
};
</script>
```

```vue
  methods: {
    receiveWarn(message) {
      alert(message);
    },
  },
```

๋ถ๋ชจ ์ปดํฌ๋ํธ์์ ๋ฌ๋ผ์ง ๋ถ๋ถ์ receiveWarn ๋ฉ์๋์ message๊ฐ ์ธ์๊ฐ ์ถ๊ฐ๋์๋ค๋ ์ ์ด๋ค. ์์์ ๋งํ๋ฏ์ด ์ด๋ฒคํธ๋ช์ ์ ์ธํ๊ณ  emit ๋ฉ์๋์ ์ถ๊ฐ๋ ์ธ์๋ค์ ๋ฆฌ์ค๋์ ์ธ์๋ก ์ ๋ฌ๋๊ธฐ ๋๋ฌธ์ ์์ ์ปดํฌ๋ํธ์์ ์์ฑ๋ message ๋ฐ์ดํฐ์ ๊ฐ์ ์ฌ์ฉํ  ์ ์๋ค.

![image-20220608143604704](md-images/image-20220608143604704.png)



์ ์์ ์ผ๋ก ์๋ํ๋ค.

## ๋น ๋ถ๋ชจ-์์ ์ปดํฌ๋ํธ๊ฐ ํต์ 

๋๋ก๋ ๋ ์ปดํฌ๋ํธ๊ฐ ์๋ก ํต์  ํ  ํ์๊ฐ ์์ง๋ง ์๋ก ๋ถ๋ชจ/์์์ด ์๋ ์๋ ์๋ค. ๊ฐ๋จํ ์๋๋ฆฌ์ค์์๋ ๋น์ด์๋ Vue ์ธ์คํด์ค๋ฅผ ์ค์ ์ด๋ฒคํธ ๋ฒ์ค๋ก ์ฌ์ฉํ  ์ ์๋ค.

```js
var bus = new Vue()

// ์ปดํฌ๋ํธ A์ ๋ฉ์๋
bus.$emit('id-selected', 1)

// ์ปดํฌ๋ํธ B์ created hook
bus.$on('id-selected', function (id) {
  console.log(id) // 1
})
```

# :books:์ฐธ๊ณ ์๋ฃ

- [Props โ Vue.js](https://kr.vuejs.org/v2/guide/components-props.html#Prop-%EC%9C%A0%ED%9A%A8%EC%84%B1-%EA%B2%80%EC%82%AC)
- [Components | Cracking Vue.js](https://joshua1988.github.io/vue-camp/vue/components.html#%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%A9%E1%84%82%E1%85%A5%E1%86%AB%E1%84%90%E1%85%B3-%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC-%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3-%E1%84%92%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%86%A8)
- https://joshua1988.github.io/vue-camp/vue/components.html#%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%A9%E1%84%82%E1%85%A5%E1%86%AB%E1%84%90%E1%85%B3-%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC-%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3-%E1%84%92%E1%85%A7%E1%86%BC%E1%84%89%E1%85%B5%E1%86%A8)
