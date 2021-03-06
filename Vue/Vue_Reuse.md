# πμ»΄ν¬λνΈ μ¬μ¬μ©μ±

Vueμλ μ»΄ν¬λνΈ μ¬μ¬μ©μ±μ λμ΄κΈ° μν΄ Slotκ³Ό λμ  μ»΄ν¬λνΈλ₯Ό μ¬μ©νλ€.

## Slot

μ¬λ‘―(slot)μ μ»΄ν¬λνΈμ μ¬μ¬μ©μ±μ λμ¬μ£Όλ κΈ°λ₯μ΄λ€. νΉμ  μ»΄ν¬λνΈμ λ±λ‘ν νμ μ»΄ν¬λνΈμ λ§ν¬μμ νμ₯νκ±°λ μ¬μ μν  μ μλ€.

```html
<!-- HeaderComponent.vue -->

<template>
  <div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'HeaderComponent',
};
</script>

<style></style>
```

```html
<!-- App.vue -->

<template>
  <header-component>λ©μΈ νμ΄μ§</header-component>
  <header-component>κ²μ νμ΄μ§</header-component>
  <header-component>λ‘κ·ΈμΈ νμ΄μ§</header-component>
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
</style>
```

App.vueμμ μμ±ν λ©μΈ νμ΄μ§ λ±μ μ½νμΈ  λ΄μ©μ΄ HeaderComponent.vueμ μμ±ν slot νκ·Έμ μ½μλλ€.

slotμλ λ¨μν λ¬Έμμ΄λΏλ§ μλλΌ HTML ν¬ν¨ν μ΄λ ν ννλ¦Ώ μ½λ, μ¬μ§μ΄ μ»΄ν¬λνΈλ₯Ό ν¬ν¨μν¬ μλ μλ€.

### Fallback μ½νμΈ 

λν΄νΈ κ°μ΄λΌκ³  μκ°νλ©΄ μ’ λ μλΏμ κ²μ΄λ€. slot μμλ€κ° κ°μ μ μνκ³  μμ μ»΄ν¬λνΈμμ slotμ κ°μ§ μ»΄ν¬λνΈμ μλ¬΄λ° μ»¨νμΈ λ μ κ³΅νμ§ μμμ λ, slotμ μ μλ κ°μ΄ λμ€κ² λλ€.

```html
<!-- HeaderComponent.vue -->

<template>
  <div>
    <slot>λΉ νμ΄μ§</slot>
  </div>
</template>
```

```html
<!-- App.vue -->

<template>
  <header-component>λ©μΈ νμ΄μ§</header-component>
  <header-component>κ²μ νμ΄μ§</header-component>
  <header-component>λ‘κ·ΈμΈ νμ΄μ§</header-component>
Β Β <header-component></header-component>
</template>
```

#### κ²°κ³Ό

![](md-images/2022-03-31-15-26-43-image.png)

### μ΄λ¦μ κ°λ Slot

μ¬λ¬ κ°μ μ¬λ‘―μ μ¬μ©νλ κ²μ΄ μ μ©ν κ²½μ°κ° μλ€. μλ₯Ό λ€μ΄, μλμ κ°μ ννλ¦Ώμ κ°μ§ μ»΄ν¬λνΈκ° μλ€κ³  ν΄λ³΄μ.

```html
<!--BaseLayoutComponent.vue -->

  <div class="container">
    <header>
      <!-- header μ»¨νμΈ λ₯Ό λκ³  μΆμ κ³³ -->
    </header>
    <main>
      <!-- main μ»¨νμΈ λ₯Ό λκ³  μΆμ κ³³ -->
    </main>
    <footer>
      <!-- footer μ»¨νμΈ λ₯Ό λκ³  μΆμ κ³³ -->
    </footer>
  </div>
```

```html
 <!--BaseLayoutComponent.vue -->

  <div class="container">
    <header>
      <slot name="header">
    </header>
    <main>
      <slot>
    </main>
    <footer>
      <slot name="footer">
    </footer>
  </div>
 ...
 <style>
main {
  color: blue;
}

footer {
  color: red;
}
</style>
```

slot νκ·Έμ name μμ±μ κ° slotμ νΉμ ν IDλ‘μ¨ κ°κ°μ μ½νμΈ κ° μνλ κ³³μ λ λλ§λλλ‘ νλ λ° μ¬μ©λλ€. nameμ΄ μλ κ²½μ°λ λ¬΅μμ μΌλ‘ defaultλΌλ nameμ κ°κ² λλ€.

```html
<!-- App.vue -->

<template>
  <base-layout-component>
    <template v-slot:header>
      <h1>μ¬κΈ°μλ ν€λ λ΄μ©</h1>
    </template>
    <template v-slot:default>
      <p>μ¬κΈ°μλ λ©μΈ μ»¨νμΈ  λ΄μ©</p>
    </template>
    <template v-slot:footer>
      <p>μ¬κΈ°λ νΈν°μ ν΄λΉνλ λ΄μ©</p>
    </template>
  </base-layout-component>
</template>
```

#### κ²°κ³Ό

![](md-images/2022-03-31-15-41-47-image.png)

μμ μ»΄ν¬λνΈμμ κ°κ°μ slotμ μ»¨νμΈ λ₯Ό μμ±ν  λλ template νκ·Έμ v-slot λλ ν°λΈμ κ°κ°μ slot nameμ μμ±ν΄μ£Όλ©΄ λλ€.

## :bulb:Tip

κ°λ¨ν νμΌλ‘ μ΄λ¦μ κ°λ Slotμ μΆμ½νμΌλ‘ λ°κΏ μ μλ€.

`v-slot:header -> #header` 

μμ κ°μ΄ λ°κΏ μ μλ€. νμ§λ§ μΆμ½νμ name μμ±μ μ μ΄μ€ κ²½μ°μλ§ κ°λ₯νλ€λ μ μ μ£Όμνμ.

## λμ  μ»΄ν¬λνΈ

λμ μΌλ‘ μ»΄ν¬λνΈλ₯Ό μ νν΄μΌνλ κ²½μ°λ λ€μνκ² μ§λ§, νΉν ν­ μΈν°νμ΄μ€λ₯Ό λ§λ€ λ μλΉν μ μ©νλ€.

λμ  μ»΄ν¬λνΈλ λ κ°μ§ κ°λμ λν΄μ μκ³  μμ΄μΌ νλ€.

- component

- is μμ±

**component**λ λμ  μ»΄ν¬λνΈλ₯Ό λ λλ§νκΈ° μν λ©ν μ»΄ν¬λνΈμ΄λ€. λ λλ§ν  μ€μ  μ»΄ν¬λνΈλ **is μμ±**μ μν΄ κ²°μ λλ€.λμ  μ»΄ν¬λνΈλ₯Ό νμ©ν΄μ κ°λ¨ν ν­ μΈν°νμ΄μ€λ₯Ό λ§λ€μ΄λ³΄κ² λ€.

![](md-images/2022-03-31-16-46-12-image.png)

![](md-images/2022-03-31-16-46-26-image.png)

```html
<template>
  <button
    :class="{ tab: true, active: activeTab === tab.name }"
    v-for="tab in tabs"
    :key="tab.id"
    @click="activeTab = tab.name"
  >
    {{ tab.name }}
  </button>
  <div>
    <component v-bind:is="activeTab"></component>
  </div>
</template>

<script>
import Home from './components/HomeComponent.vue';
import Posts from './components/Postomponent.vue';
import Archive from './components/ArchiveComponent.vue';

export default {
  name: 'App',
  components: {
    Home,
    Posts,
    Archive
  },
  data() {
    return {
      activeTab: 'Home',
      tabs: [
        {
          name: 'Home',
          id: 1,
        },
        {
          name: 'Posts',
          id: 2,
        },
        {
          name: 'Archive',
          id: 3,
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
.tab {
  width: 200px;
  height: 60px;
  font-size: 30px;
  font-weight: 700;
}
.active {
  background-color: blue;
}
</style>
```

```html
<!-- is μμ±μμ λ λλ§λ  κ°κ° μ»΄ν¬λνΈ -->

<template>
  <h1>νμ΄μ§λͺ</h1>
</template>
```

μ μ²΄μ μΈ νλ¦μ λ³΄μλ©΄,

1. κ°κ°μ νμ΄μ§ λ²νΌμ λλ₯΄λ©΄ activeTab λ°μ΄ν°κ° ν΄λΉ νμ΄μ§λͺμΌλ‘ λ°λλ€.

2. activeTabμ is μμ±μ λ°μΈλ©λμ΄μκΈ° λλ¬Έμ activeTabμ΄ λ°λ λλ§λ€ ν΄λΉ νμ΄μ§λͺμ κ°μ§ μ»΄ν¬λνΈλ₯Ό λ λλ§νκ² λλ€.

### Keep Alive

μ΄μ²λΌ μ»΄ν¬λνΈλ₯Ό μ νν  λ vue μΈμ€ν΄μ€λ μλ©Έ, μμ±μ λ°λ³΅νλ€. μ»΄ν¬λ¨ΌνΈμ μ νλ§λ€ νμ΄μ§λ₯Ό μ΄κΈ°νλμ΄μΌ νλ€λ©΄ λ¬Έμ κ° μμ§λ§ λ§μ½ μ»΄ν¬λνΈ μμ κ°μ μ μ§ν΄μΌ νκ±°λ μ±λ₯μμ μ΄μ λ‘ λ¦¬λ λλ§μ νΌνκ³  μΆμ λ `Keep-alive` μ»΄ν¬λνΈ μ¬μ©ν  μ μλ€. keep-alive λ‘ λλ¬μΌ μ»΄ν¬λνΈλ μ»΄ν¬λνΈκ° μ΅μ΄ μμ±λλ μμ μΒ **μΊμ**Β ν΄λλ€.

μ΄λ₯Ό νμΈνκΈ° μν΄ HomeComponentμ μΉ΄μ΄ν°λ₯Ό μΆκ°ν΄λ³΄κ² λ€.

```html
<template>
  <h1>ν</h1>
  <h2>How many people visited : {{ counter }}</h2>
  <button @click="counter += 1">Visit</button>
</template>

<script>
export default {
  data() {
    return {
      counter: 0,
    };
  },
};
</script>
```

visit λ²νΌμ λλ₯΄λ©΄ μΉ΄μ΄ν°κ° μ¬λΌκ°λ κ°λ¨ν κ΅¬μ‘°μ΄λ€. keep-alive μλ¦¬λ¨ΌνΈκ° μλ μν©μμλ μΉ΄μ΄ν°λ₯Ό μ¬λ¦¬κ³  λ€λ₯Έ ν­μΌλ‘ κ°λ€κ° μ€λ©΄ μΉ΄μ΄ν° κ°μ΄ μ΄κΈ°ν λμ΄μλ κ±Έ νμΈν  μ μλ€.

```html
<template>
  <button
    :class="{ tab, active: activeTab === tab.name }"
    v-for="tab in tabs"
    :key="tab.id"
    @click="activeTab = tab.name"
  >
    {{ tab.name }}
  </button>
  <div>
    <keep-alive>
      <component v-bind:is="activeTab"></component>
    </keep-alive>
  </div>
</template>
```

componentλ₯Ό keep-alive μλ¦¬λ¨ΌνΈλ‘ κ°μΈμ£Όλ©΄ ν­μ΄ μ νλκ³  λμλ μΉ΄μ΄ν°κ° μ μ§λλ κ²μ νμΈν  μ μλ€.

# :books: μ°Έκ³ μλ£

[Slots | Cracking Vue.js](https://joshua1988.github.io/vue-camp/reuse/slots.html)

[Slots | Vue.js](https://v3.ko.vuejs.org/guide/component-slots.html#slot-%E1%84%8F%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A6%E1%86%AB%E1%84%8E%E1%85%B3)

[λμ  &amp; λΉλκΈ° μ»΄ν¬λνΈ | Vue.js](https://v3.ko.vuejs.org/guide/component-dynamic-async.html#keep-alive%E1%84%85%E1%85%B3%E1%86%AF-%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB-%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8-%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%A9%E1%84%82%E1%85%A5%E1%86%AB%E1%84%90%E1%85%B3)

[(Vue.js) keep-alive, λμ  μ»΄ν¬λνΈμ λνμ¬ | Let's Sunny](https://sunny921.github.io/posts/vuejs-keep-alive/)
