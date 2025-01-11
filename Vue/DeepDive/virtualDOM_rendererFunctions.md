# Deep Dive

## VirtualDOM & Renderer Functions

### Virtual DOM

- 렌더링 로직을 실제 DOM과 분리
- 브라우저 환경이 아닌 곳에서 재사용하기 쉬워짐
- SSR, canvas, WebGL, 네이티브 모바일
- 렌더링 전에 원하는 형태의 DOM을 js를 활용해서 만들 수 있음

### Renderer Function

- Vue3 API
  - 인자 평면화
  - h helper가 기본 인자가 아닌 전역에서 import되어 사용

- slot

  - ```js
    const App = {
    	render() {
    		const slot = this.$slots.default && this.$slots.default()
    	}
    }
    ```

  - vue3에서는 render function의 slots.default는 항상 함수

- ```html
  // index.html
  
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  
  <div id="app"></div>
  
  <script>
  const { createApp, h } = Vue
  
  const HelloWorld = {
      render() {
          return h('div', {innerText: 'Hello World'})
      }
  }
  
  const App = {
      components: {
          HelloWorld
      },
      template: `<HelloWorld />`
  }
  createApp(App).mount('#app')
  </script>
  ```

# :books:참고자료

- https://www.vuemastery.com/courses/vue3-deep-dive-with-evan-you/virtual-dom-and-render-functions
- https://www.vuemastery.com/courses/vue3-deep-dive-with-evan-you/how-to-use-render-functions



