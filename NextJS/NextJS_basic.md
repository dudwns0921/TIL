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

## 사전 렌더링과 데이터페칭

- 기존 리액트 앱은 FCP 이후 **컴포넌트 마운트** 이후에 API 요청이 이루어졌기 때문에 사용자가 백엔드 서버의 데이터를 확인하기까지 오랜 시간이 걸림
- NextJS은 **사전 렌더링** 때 API 요청을 해 사용자에게 추가적인 로딩 없이 데이터가 로드된 HTML을 한 번에 보여줄 수 있다는 장점
- 사전 렌더링 때 백엔드 상태에 따라 사용자 경험이 저하될 수도 있어 NextJs에서는 빌드타임 사전 렌더링 등 다양한 사전 렌더링 설정(SSG)도 가능

## SSR

- getServerSideProps 함수가 있는 파일은 SSR로 동작됨

- 페이지 컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터 불러오는 함수

- ```js
  export const getServerSideProps = () => {
    const data = "hello";
  
    return {
      props: {
        data,
      },
    };
  };
  
  export default function Home(props: InferGetServerSidePropsType<typeof getServerSideProps>) {
  ```

- 위와 같이 사용 가능

- NextJs에서는 컴포넌트가 서버에서 실행되기 때문에 window 객체에 접근하면 오류가 발생할 수 있으므로 주의!

- useEffect를 사용하면 마운트 이후 시점에 window 접근 가능

## SSG

- ssr의 경우 요청이 들어올 때마다 백엔드 서버에 필요한 데이터를 받아오기 때문에 데이터가 최신이라는 장점

- 서버 상태 안 좋다거나 데이터 용량이 너무 크면, 사용자 경험이 저하됨

- 이 단점을 해결하기 위한 방법이 SSG

- 빌드 타임에 페이지를 사전 렌더링해두고 다시는 js를 실행(렌더링)하지 않음

- 사전 렌더링에 많은 시간이 소요되는 페이지더라도 사용자 요청에는 매우 빠른 속도로 응답 가능

- 최신 데이터 반영은 어려움

- ```js
  export const getStaticProps = () => {
    const data = "hello";
      
    if(!data) {
        return {
            notFound: true
        }
      // 사전 렌더링 이후에도 데이터가 없다면, 404 페이지로 보내는 옵션
    }
  
    return {
      props: {
        data,
      },
    };
  };
  
  export default function Home(props: InferGetStaticPropsType<typeof getStaticProps>) {
  ```

- 동적인 경로를 가질 경우 getStaticPath라는 함수가 추가로 필요

- ```js
  export const getStaticPaths = () => {
    return {
      paths: [
      	{ params: { id:"1" } },
      	{ params: { id:"2" } },
          { params: { id:"3" } },
      ],
      fallback: false
    };
  };
  ```

- 정의되지 않은 경로에 대한 대비책이 fallback 옵션

  - false일 경우 404 페이지가 렌더링됨
  - blocking
    - 즉시 생성, SSR
    - 빌드 타임에 사전에 생성해두지 않았었던 페이지까지 렌더링해줄 수 있음
  - true
    - 즉시 생성 + 페이지만 미리 반환
    - props에서 전달되는 데이터가 없는 상황이므로 로딩 컴포넌트 등을 띄움
    - 이후 Props을 계산해 Props만 따로 반환

- fallback 상태란 페이지 컴포넌트가 아직 서버로부터 데이터를 전달받지 못한 상태

  - useRouter 객체에 isFallback이라는 flag를 통해 fallback 상태임을 판별 가능

## ISR

- 증분 정적 재생성

- SSG 방식으로 생성된 정적 페이지를 일정 주기로 다시 생성하는 방식

- 매우 빠른 속도로 응답이 가능한 SSG 방식의 장점과 최신 데이터 반영이라는 SSR 방식의 장점을 결합한 방식

- ```js
  export const getStaticProps = () => {
    const data = "hello";
    ...
    return {
      props: {
        data,
      },
      revalidate: 3,
      // 3초마다 재생성
    };
  };
  ```

- nextJS 빌드시 revalidate props를 보고 ISR임을 판단

## On Demand ISR

- 요청을 받을 때마다 페이지를 재생성하는 ISR 방식

- 실제로 사용자가 게시글을 수정해서 데이터 업데이트가 필요할 때 revalidate 요청을 보내 페이지를 재생성하는 방식

- API Routes 기능을 활용

  - ```js
    import { NextApiRequest, NextApiResponse } from "next";
    
    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse
    ) {
      try {
        await res.revalidate("/");
        return res.json({ revalidation: true });
      } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Revalidation Error" });
      }
    }
    
    ```

## SEO

- ```tsx
  export default function Page({
    book,
  }: InferGetServerSidePropsType<typeof getServerSideProps>) {
    const router = useRouter();
    if (router.isFallback) {
      return (
        <>
          <Head>
            <title>한입 북스</title>
            <meta property="og:image" content="/thumbnail.png" />
            <meta property="og:title" content="한입 북스" />
            <meta
              property="og:description"
              content="한입 북스의 등록된 도서들을 만나보세요"
            />
          </Head>
          <div>로딩중...</div>;
        </>
      );
    }
    if (book === null) {
      return <div>책 정보가 없습니다.</div>;
    }
    return (
      <>
        <Head>
          <title>{book.title}</title>
          <meta property="og:image" content={book.coverImgUrl} />
          <meta property="og:title" content={book.title} />
          <meta property="og:description" content={book.description} />
        </Head>
        <div>
          <div
            style={{
              backgroundImage: `url('${book?.coverImgUrl}')`,
            }}
            className={style.cover_img_container}
          >
            <img src={book?.coverImgUrl} />
          </div>
          <div className={style.info_container}>
            <div className={style.title}>{book?.title}</div>
            <div className={style.sub_title}>{book?.subTitle}</div>
            <div className={style.author}>
              {book?.author} | {book?.publisher}
            </div>
            <div className={style.description}>{book?.description}</div>
          </div>
        </div>
      </>
    );
  }
  
  ```

- Head 태그 안에 title, meta 태그 등을 통해  SEO 설정

- props를 받아오지 못하면 book 관련 데이터가 없기 때문에 SEO 설정 자체가 되지 않음

- props를 받아오지 못했을 때는 isFallback flag를 통해 fallback 상태임을 확인하고 기본 meta 정보들을 반환하도록 설정

## Page Router 단점

- 페이지별 레이아웃 설정이 번거롭다
- 데이터 페칭이 페이지 컴포넌트에 집중된다
- 불필요한 컴포넌트들도 JS 번들에 포함된다
  - 상호작용이 없는 리액트 컴포넌트들은 JS 번들로 다시 전달될 필요가 없음
  - 하지만 페이지 라우터에서는 상호작용 유무에 상관없이 JS 번들로 모든 컴포넌트를 전달
