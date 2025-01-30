# NextJS

## 개요

- 리액트 전용 앱 프레임워크
- 리액트의 확장판 정도로 이해
  - 페이지 라우팅
  - 빌트인 최적화 기능
  - 다이나믹 HTML 스트리밍
- vercel에서 개발, 오픈소스로 운영중

## 사전 렌더링

- 개요
  - 브라우저 요청에 사전에 렌더링이 완료된 HTML을 응답하는 렌더링 방식
- 렌더링 과정
  - 사전 렌더링의 경우 서버에서 JS를 실행(리액트 컴포넌트를 렌더링)해 렌더링이 완료된 HTML을 사용자에게 전달
  - 이 때는 사용자 상호작용이 불가능
  - 서버에서 JS 번들을 전달해주고 Hydration이 일어나야 상호작용이 가능해짐
  - 이 때 상호작용이 가능한 시점까지의 시간을 TTI라고 함
- 페이지 이동
  - CSR 방식으로 처리
  - JS를 실행해 컴포넌트를 교체하는 방식
- NextJS 장점
  -  사전 렌더링을 통해 FCP 개선
  - 기존 CSR의 장점인 빠른 페이지 이동은 그대로 승계

## Page Router

- pages 폴더 기반으로 라우팅 제공
- 파일명 기반의 페이지 라우팅
- 폴더명으로도 라우팅을 적용할 수 있음
- 동적 경로의 경우 파일명을 대괄호로 묶어주면 됨
- nextjs 프로젝트 생성시
  - pages 하위의 _[파일명]
  - 기본 설정을 확장하거나 커스터마이징할 때 사용
  - _app.tsx
    - 루트 컴포넌트의 역할
  - _document.tsx
    - 기본 HTML 문서 커스터마이징

## 페이지 라우팅 설정하기

- useRouter
  - next/Router의 hook을 사용해서 페이지 라우터 기능 사용 가능
- 동적 경로
  - 연속된 id에 대한 처리
    - [...id].tsx
    - catch all segment
    - 인덱스 경로에 대해서는 catch할 수 없음
      - 대괄호로 한 번 더 감싸줄 경우 인덱스까지도 대응할 수 있음
      - [[...id]].tsx
      - optional catch all segment
- 404
  - pages 폴더 아래 404.tsx 파일 생성

## 네비게이팅

- 자체적으로 제공하는 내장 컴포넌트인 Link 컴포넌트로 네비게이팅을 제공
- useRouter hook을 통해 반환받는 router 객체의 push 메서드를 통해서 네비게이팅도 가능
  - replace
    - 뒤로가기를 방지하면서 이동하는 메서드
  - back
    - 뒤로가기

## 프리페칭

- 현재 사용자가 보고 있는 페이지내에서 이동 가능한 페이지들을 미리 불러오는 기능

- 빠른 페이지 이동을 위해 제공되는 기본 기능

- NextJS에서는 페이지별로 JS 번들, 즉 리액트 컴포넌트를 스플리팅해서 저장해둠

  - 현재 페이지에 필요한 JS 번들만 전달됨

- NextJS에서는 현재 페이지에 대한 JS번들만 받아오기 때문에 매 페이지 이동마다 데이터 요청이 필요

- 이로 인해 페이지 이동이 느려질 수 있기 때문에 프리페칭을 사용

- 링크 컴포넌트로 명시된 경우가 아니라면 프리페칭이 일어나지 않음

- ```js
  useEffect(()=>{
  router.prefetch("test")
  }, [])
  ```

- router.prefetch 메서드로 프리페칭 가능

## API Routes

- 풀스택 개발이 가능하게 해주는 기능
- pages/api
  - api routes로서 응답을 정의하는 파일
  - 파일명으로 경로가 정해짐

## 스타일링

- 글로벌 css 파일은 App 컴포넌트에서만 import 가능
- css 모듈 방식으로 import 가능

## 글로벌 레이아웃 설정하기

- 글로벌 레이아웃을 설정할 때는 App 컴포넌트에서 헤더, 푸터등을 적용해 구조를 설정

- ```tsx
  import { ReactNode } from "react";
  
  export default function GlobalLayout({ children }: { children: ReactNode }) {
    return (
      <div>
        <header>헤더</header>
        <main>{children}</main>
        <footer>푸터</footer>
      </div>
    );
  }
  
  ```

- 글로벌 레이아웃이라는 별도의 컴포넌트를 작성

- ```tsx
  import GlobalLayout from "@/components/global-layout";
  import "@/styles/globals.css";
  import type { AppProps } from "next/app";
  
  export default function App({ Component, pageProps }: AppProps) {
    return (
      <>
        <GlobalLayout>
          <Component {...pageProps} />
        </GlobalLayout>
      </>
    );
  }
  
  ```

- 위와 같이 정의

## 페이지 레이아웃 설정

- 자바스크립트 함수는 Function 객체의 인스턴스로 메서드를 추가할 수 있음

- getLayout이라는 메서드를 추가해 해당 페이지에 적용되어야 할 레이아웃 컴포넌트를 반환

- ```tsx
  import SearchableLayout from "@/components/SearchableLayout/searchable-layout";
  import { ReactNode } from "react";
  
  export default function Home() {
    return <h1>인덱스</h1>;
  }
  
  Home.getLayout = (page: ReactNode) => {
    return <SearchableLayout>{page}</SearchableLayout>;
  };
  
  ```

- 루트 컴포넌트에서 getLayout 메서드를 실행해 반환받은 레이아웃 안에 page 컴포넌트를 전달

-  ```tsx
   import GlobalLayout from "@/components/GlobalLayout/global-layout";
   import "@/styles/globals.css";
   import { NextPage } from "next";
   import type { AppProps } from "next/app";
   import { ReactNode } from "react";
   
   type NextPageWithLayout = NextPage & {
     getLayout: (page: ReactNode) => ReactNode;
   };
   
   export default function App({
     Component,
     pageProps,
   }: AppProps & {
     Component: NextPageWithLayout;
   }) {
     const getLayout = Component.getLayout ?? ((page: ReactNode) => page);
   
     return (
       <>
         <GlobalLayout>{getLayout(<Component {...pageProps} />)}</GlobalLayout>
       </>
     );
   }
   
   ```

- 레이아웃을 별도로 사용하지 않는 컴포넌트들을 위해 ?? 연산자를 사용해 getLayout 메서드가 없을 경우 인자로 전달받은 page를 그대로 반환하는 함수로 설정
- NextPage type에는 getLayout이 없기 때문에 해당 타입을 확장해서 적용
