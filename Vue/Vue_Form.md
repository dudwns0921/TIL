# Vue

## Vue Form

### Base-Input

- 각 Input에 대해 재사용 가능한 컴포넌트를 만들면 이를 쉽게 복제, 수정, 확장 가능

- 이를 통해 애플리케이션 전반에 걸쳐 Form의 일관성을 보장 가능

### V-model

- 기본적으로 Vue 3에서 v-model은 v-model을 사용할 수 있는 컴포넌트에 modelValue라는 속성이 있기를 기대
- v-model을 사용할 수 있는 모든 컴포넌트는 부모가 해당 컴포넌트의 데이터 업데이트를 수신할 수 있도록 이벤트를 발생시켜야 함
- Vue 3에서는 v-model이 적용된 컴포넌트가 어떤 유형의 Input을 포함하든 관계없이 update:modelValue 이벤트 발생시키기를 기대

```vue
// child component
// BaseInput.vue
<template>
  <label v-if="label">{{ label }}</label>
  <input
    :value="modelValue"
    :placeholder="label"
    @input="$emit('update:modelValue', $event.target.value)"
    class="field"
  >
</template>

<script>
export default {
  props: {
    label: {
      type: 'String',
      default: ''
    },  
    modelValue: {
      type: [String, Number],
      default: ''
    }
  }
}
</script>

// parent component
  <BaseInput
    v-model="event.title"
    label="Title"
    type="text"
  />
...
  data () {
    return {
	...
      event: {		
		...
        title: '',
		...
      }
    }
  }
```

### auto-import

```js
import { createApp } from 'vue'
import App from './App.vue'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'

const requireComponent = require.context(
  './components',
  false,
  /Base[A-Z]\w+\.(vue|js)$/
)
// require.context로 components 폴더 안의 Base로 시작하는 모든 vue, js 파일을 동적 로드

const app = createApp(App)

requireComponent.keys().forEach(fileName => {
  // keys 메서드를 통해 파일 이름을 순회
  const componentConfig = requireComponent(fileName)
  const componentName = upperFirst(
    camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, '$1'))
  )
  // lodash 메서드로 첫 번째 문자를 대문자로 바꾸고 camelCase화시킴

  app.component(componentName, componentConfig.default || componentConfig)
  // Application API인 component를 사용해 전역 컴포넌트로 등록
})

app.mount('#app')
```

#### require.context

- 이 함수는 동적으로 모듈을 require/import 할 수 있게 해주는 함수

- 이 함수를 사용하면 지정된 디렉토리 내에서 특정 패턴을 가진 모든 파일을 한 번에 가져올 수 있음

#### context module API

- require.context로부터 반환된 함수로 하나의 인수를 가짐
- 하나의 인수는 파일명으로, 인자를 전달할 경우 해당 파일에서 export된 모듈을 반환
- resolve, keys, id의 3가지 속성을 가짐
- `resolve`는 파싱된 요청의 모듈 id를 반환하는 함수
- `keys`는 컨텍스트 모듈이 처리할 수 있는 가능한 모든 요청의 배열을 반환하는 함수

### Checkbox

```vue
<template>
        <input
          type="checkbox"
          :checked="modelValue"
            @change="$emit('update:modelValue', $event.target.checked)"
          class="field"
        />
        <label v-if="label">{{label}}</label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: ''
    },
    modelValue: {
      type: Boolean,
      default: false
    }
  }
}
</script>
```

### Radio

```vue
<template>
    <input
        type="radio"
        :checked="modelValue === value"
        :value="value"
        @change="$emit('update:modelValue', value)"
        v-bind="$attrs"
        />
    <label>{{label}}</label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: ''
    },
    modelValue: {
      type: [String, Number],
      default: ''
    },
    value: {
      type: [String, Number],
      required: true
    }
  }
}
</script>

```

- Radio 버튼은 그룹으로 사용되기 때문에 해당 Radio 버튼이 어떤 값을 나타내는지 알아야 함
- 이를 위해 value prop을 추가
- value prop은 required여야 함
- Checkbox와 마찬가지로 checked 속성을 사용
- 이 때 checked에 modelValue를 바로 전달하는 게 아니라, modelValue===value 그러니까 바인딩된 값과 실제 라디오 버튼이 가지는 값이 동일한지를 전달

### GroupRadio

```vue
<template>
    <component
        :is="vertical ? 'div' : 'span'"
        v-for="option in options"
        :key="option.value"
    >
        <BaseRadio
            :label="option.label"
            :value="option.value"
            :name="name"
            :modelValue="modelValue"
            @update:modelValue="$emit('update:modelValue', $event)"
        />
    </component>
</template>

<script>

export default {
  props: {
    options: {
      type: Array,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    modelValue: {
      type: [String, Number],
      required: ''
    },
    vertical: {
      type: Boolean,
      default: false
    }
  }
}
</script>

```

- Radio 컴포넌트를 그룹으로 가지는 컴포넌트
- BaseRadio에 binding된 value가 바뀌면 update:modelValue이벤트가 emit되고, 이 이벤트를 그대로 다시 v-model을 사용하고 있는 부모 컴포넌트에 전달
- 수평, 수직을 위해 component를 사용
- is prop은 실제 컴포넌트에 바인딩될 수도 있고, 문자열을 전달하면 해당 태그가 연결

### Form

- form 태그의 기본 동작은 브라우저의 navigation 이벤트를 실행시켜 특정 URL로 데이터를 보내는 것
- 이 때 form 태그의 기본 동작에 의해 브라우저는 완전히 새롭게 로드됨
- 하지만 full-reload 없이 유저에게 페이지 이동을 제공하는 SPA에서는 form의 기본 동작은 좋지 않음

```vue
<form @submit.prevent="sendForm">
```

- 위와 같이 작성함으로써 form의 기본동작을 막고 submit 이벤트에 리스너를 걸 수 있음

### a11y

- "a11y"는 접근성을 의미하는 "accessibility"의 약어
- 접근성은 장애가 있는 사람들이 웹 사이트와 애플리케이션을 사용할 수 있도록 하는 것을 목표

#### fieldset & legend

- 폼의 각 섹션을 항상 `<fieldset>` 요소로 감싸는 것이 좋음
- 이렇게 하면 내부의 입력 요소들을 논리적으로 그룹화할 수 있음
- 그리고 `<fieldset>`의 첫 번째 요소는 특정 필드셋에 대한 제목을 제공하는 `<legend>` 요소가 되어야 함

#### placeholder

- placeholder을 label 대신에 사용하는 경우도 있는데 지양해야 함
- placeholder는 어떤 값이 들어가야 하는지 보여주는 용도로 사용]

#### for & id

- label과 input이 연속되어 있다고 하더라도 screen reader는 두 태그가 연결된 것을 인식하지 못함
- label과 input을 연결하기 위해 for과 id를 사용
- 이 때 두 속성에 바인딩되는 값은 유일해야 함
- uuid 라이브러리 활용하기

#### error

- error 메시지가 input 바로 밑에 뜨더라도 screen reader는 해당 에러 메시지가 어디에 연결되있는지 인식하지 못함
- aria-describedby 속성을 사용하면 연결할 수 있음
- error 메시지가 나타났을 때 screen reader로 하여금 메시지를 읽도록 하기 위해서는 aria-live="assertive" 를 사용 가능

```vue
<template>
    <label :for="uuid">{{label}}</label>
      <input
        :placeholder="label"
        v-bind="$attrs"
        class="field"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :id="uuid"
        :aria-describedby="error ? `${uuid}-error` : null"
      >
      <p
      v-if="error"
      class="errorMessage"
      :id="`${uuid}-error`"
      aria-live="assertive"
      >{{error}}</p>
</template>

<script>
import UniqueID from '../features/UniqueID'
export default {
  props: {
    label: {
      type: String,
      default: ''
    },
    modelValue: {
      type: [String, Number],
      default: ''
    },
    error: {
      type: String,
      default: ''
    }
  },
  setup () {
    const { getID } = UniqueID()
    const uuid = getID()

    return { uuid }
  }
}
</script>
```

- Vue에서 속성값을 null에 바인딩하면 Vue는 해당 속성을 완전히 무시
- aria-invalid 속성을 error가 나타났을 때 추가하면 접근성을 더 높일 수 있음

### submit button disabled

- form이 완전히 입력되지 않았을 때 submit 버튼을 disabled 처리하는 경우가 있는데 이는 혼란을 일으킬 수 있음
- disabled가 적용되면 screen reader는 이 버튼을 아예 인지하지 못함

# :books:참고자료

- https://www.vuemastery.com/courses/vue3-forms
