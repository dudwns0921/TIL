# Vanilla Extract

# Basic

### Getting Started

- 번들러 통합
  - Vanilla-Extract를 사용하기 위해서는 CSS를 처리할 수 있는 번들러가 있어야 함
- 스타일 만들기
  - .css.ts로 스타일시트 생성 가능
    - 로컬 범위 클래스 생성
    - 생성된 클래스를 export 함

### Styling

- 스타일 적용

  - 자바스크립트 객체 형태로 스타일을 정의

  - 타입스크립트 활용 가능

  - camelCase 사용

  - number는 px로 casting

  - 속성값에 단위가 없는 경우 그대로 사용

  - ```ts
    // App.css.ts
    
    import { globalStyle, style } from "@vanilla-extract/css";
    
    export const helloWorld = style({
      color: "red",
      fontSize: 32,
    });
    
    globalStyle("body", {
      margin: 0,
    });
    ```

  - ```ts
    // App.tsx
    
    import { helloWorld } from "./App.css.ts";
    
    function App() {
      return (
        <>
          <div className={helloWorld}>Hello World</div>
        </>
      );
    }
    
    export default App;
    
    ```

- Vendor Prefix

  - 특정 브라우저에 대한 속성 사용하려면 시작 부분에서 '-' 제거

- CSS 변수

  - vars 키 내에 정의

  - createVar API를 통해 scoped된 css 변수 생성 가능

  - ```ts
    // App.css.ts
    
    const myVar = createVar();
    
    export const helloWorld = style({
      color: "var(--my-global-variable)",
      // color: myVar,
      vars: {
        "--my-global-variable": "purple",
      },
    });
    ```

- Media Query

  - @media key 안에 미디어 쿼리 스타일 정의

  - 코드를 CSS로 처리할 때 미디어 쿼리는 파일 끝에 렌더링

  - @media 키 내부의 스타일은 다른 스타일보다 우선순위가 높음

  - ```ts
    export const helloWorld = style({
    ...
      "@media": {
        "screen and (min-width: 768px)": {
          padding: 10,
        },
      },
    ...
    });
    ```

- 가상 선택자

  - simple

    - ':hover'

    - 매개변수를 취하지 않아 쉽게 감지하고 정적으로 입력 가능

    - ```ts
      const myStyle = style({
        ':hover': {
          color: 'pink'
        },
      });
      ```

  - complex

    - 복잡한 규칙은 선택자 key를 사용해 작성 가능

    - 유지보수성을 위해 하나의 요소에만 적용 가능

    - 이걸 적용하기 위해서는 &를 사용, 현재 요소를 뜻함

    - 선택자는 다른 scoped된 클래스 이름을 참조 가능

    - 현재 요소가 아닌 다른 요소에 선택자 적용은 불가

    - 현재 요소 아래서 전역적으로 자식 node를 타깃으로 한다면 globalStyle을 사용

    - ```ts
      const myStyle = style({
        selectors: {
          '&:hover:not(:active)': {
            border: '2px solid aquamarine'
          }
        }
      });
      
      export const parent = style({});
      
      export const child = style({
        selectors: {
          [`${parent}:focus &`]: {
            background: '#fafafa'
          }
        }
      });
      
      globalStyle(`${parent} a[href]`, {
        color: 'pink'
      });
      ```

  - circular

    - 선택자가 서로 종속적이면 getter을 사용해 구현 가능

      - ```ts
        import { style } from '@vanilla-extract/css';
        
        export const child = style({
          background: 'blue',
          get selectors() {
            return {
              [`${parent} &`]: {
                color: 'red'
              }
            };
          }
        });
        
        export const parent = style({
          background: 'yellow',
          selectors: {
            [`&:has(${child})`]: {
              padding: 10
            }
          }
        });
        ```

# :books:참고자료

https://vanilla-extract.style/documentation/getting-started