# Pinia

## state 접근하기

state에 접근하는 방법은 총 3가지로 정리할 수 있다.

- setup store
- option store
- component

### Option Store

Setup Store와의 차이를 보기 위해 먼저 Option Store을 살펴보겠다.

```js
import { defineStore } from "pinia";

type Todo = {
  id: number;
  title: string;
  done: boolean;
};

export const useTodoStore = defineStore("TodoStore", {
  state: () => ({
    todos: [] as Todo[],
  }),
  actions: {
    addTodo(todo: string) {
      const todoObject: Todo = {
        id: new Date().getTime(),
        title: todo,
        done: false,
      };

      this.todos.push(todoObject);
    },
  },
  getters: {
    doneTodos(state): Todo[] {
      return state.todos.filter((v) => v.done === true);
    },
  },
});
```

option store의 actions에서 state에 접근하기 위해서는 action 내에서 this를 사용하면 된다.

getters에서는 첫 번째 인자로 state를 정의해 state에서 접근하면 된다. 

### Setup Store

```js
// TodoStore.ts

import { defineStore } from "pinia";
import { ref, computed } from "vue";

type Todo = {
  id: number;
  title: string;
  done: boolean;
};

export const useTodoStore = defineStore("TodoStore", () => {
  const todos = ref([] as Todo[]);
    
  const doneTodos = computed(() => {
      return todos.filter((v) => v.done === true);
  })

  function addTodo(todo: string) {
    const todoObject: Todo = {
      id: new Date().getTime(),
      title: todo,
      done: false,
    };

    todos.value.push(todoObject);
  }

  return { todos, addTodo };
});
```

setup store에서는 getters든 actions든 상위에서 정의된 state에 바로 접근하면 된다.

### component

```vue
<script setup lang="ts">
import { storeToRefs } from "pinia";
import { ref } from "vue";
import { useTodoStore } from "../store/TodoStore";

const todoTitle = ref("");

const todoStore = useTodoStore();
const { todos } = storeToRef(todoStore);

function addTodo() {
  todoStore.addTodo(todoTitle.value);
  todoTitle.value = "";
}
</script>

<template>
  <input type="text" v-model="todoTitle" />
  <button @click="addTodo">todo 추가하기</button>

  <ul>
    <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
  </ul>
</template>

<style scoped></style>

```

component에서 사용할 때는 위와 같이 hook을 사용해 store을 반환받아 사용하면 된다.

이 때 주의할 점은 destructing을 사용할 경우 state의 반응성이 사라진다는 점이다.

알다시피 Vue에서는 반응성 시스템이 객체의 속성을 추적하는 방식 때문에 destructing을 사용하면 반응성이 사라진다. 

Vue는 객체의 속성을 정의할 때 `Object.defineProperty`를 사용하여 getter와 setter를 설정한다.

이를 통해 속성이 변경될 때마다 Vue가 이를 감지하고 반응성을 유지할 수 있다.

그러나 객체를 destructing하면 이러한 반응성 속성들이 새로운 변수에 복사되는데, 이 과정에서 Vue의 반응성 시스템과의 연결이 끊어지게 되는 것이다. 

따라서 composition api에서는 toRefs 메서드를 사용하는 것과 마찬가지로 pinia에서는 storeToRef를 사용한다.



# :books:참고자료

- https://www.vuemastery.com/courses/proven-pinia-patterns/accessing-state



