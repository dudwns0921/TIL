# Query.gg

## Laying The Foundation

### Why React Query

- react는 사용자 인터페이스를 구축하기 위한 라이브러리
- v=f(s)
  - View는 앱의 state를 인자로 받는 함수
  - state가 어떻게 변경되는지에 대해서만 신경쓰면 React가 나머지를 처리
- Component
  - 위 개념에 대한 캡슐화 단위는 컴포넌트
  - 컴포넌트는 특정 UI와 함께 제공되는 state, logic을 모두 캡슐화
  - 컴포넌트가 UI 구성과 재사용성을 가능케 한 것처럼 React hooks는 비시각적 논리의 구성과 재사용성을 가능하게 함
- React hooks
  - React에서 제공되는 hooks는 데이터 가져오기에 전념하지 않음
  - 일반적인 방법은 useEffect 내에서 데이터를 가져와 state로 관리하는 것
  - race condition
    - 빠르게 연속적으로 요청을 보내면 요청이 순서대로 처리되지 않아 사용자가 원하는 결과가 나오지 않는 경우가 있음
    - 이를 해결하기 위해서는 아래 과정 수행
      - useEffect 클로저에 ignore이라는 flag 정의, 기본값은 false
      - cleanup 함수에 flag를 true 처리
      - useEffect 함수 내부에 정의된 fetch 함수에서 ignore flag를 보고 최신의 effect가 아님을 판단하고 필터링 처리
  - data duplication
    - 기본적으로 fetch된 데이터는 fecth한 컴포넌트에만 로컬로 존재
    - 동일한 데이터가 필요한 모든 컴포넌트에 대해 다시 fetch가 필요
    - 이를 데이터를 전역으로 만들어 해결하려고 하면 여러 url에 대해 data, loading, error state를 저장할 수 있어야 함
      - 동일한 url에 대한 요청을 캐싱 처리해 반환하려고 하기 때문
    - React Context는 상태의 일부를 구독할 수 있는 기능이 없어 애플리케이션 전체에 동적 데이터를 분산하는 데 특별히 적합한 도구가 아님
    - 변경 사항이 없더라도 해당 hook을 사용하는 모든 컴포넌트가 다시 렌더링됨
- 문제점
  - react를 통해 데이터 가져오는 로직을 관리할 경우
    - useEffect는 혼란스럽다
    - 시간이 지날수록 Context가 혼란스러워짐
    - useState, useEffect, 그리고 Context를 함께 사용할 경우 매우 고통스러워짐
    - 비동기 상태를 동기 상태처럼 취급하고 있음
- 클라이언트 상태와 서버 상태
  - 클라이언트 상태
    - 클라이언트 소유, 항상 최신
    - 클라이언트만이 바꿀 수 있음
    - 브라우저를 닫으면 사라짐
    - 동기식
  - 서버 상태
    - 서버 소유, 클라이언트에서 사용하는 것은 단순한 스냅샷
    - 여러 사용자가 소유
    - 원격으로 유지됨
    - 비동기식
  - 그래서 이 둘을 동등하게 취급하는 것은 문제가 있음
- react-query는 비동기 상태 관리 라이브러리
  - 데이터를 가져오기 위한 라이브러리가 아님
  - react-query는 데이터를 가져와주지 않음
    - fetch, axios 등을 통해 promise를 반환하면 이를 전역에서 사용할 수 있게끔 처리

### Query Fundamentals

- QueryClient의 핵심은 QueryCache를 보관하고 관리한다는 것
- cache가 있어야만 제대로 동작 가능
- 주의해야 할 점
  - 루트 컴포넌트 밖에 QueryClient를 만들어야 함
  - 그래야만 리렌더링이 일어나더라도 캐시가 안정적으로 유지됨
- QueryClientProvider
  - query client을 생성하고 client prop에 전달
  - 이 컴포넌트로 루트 컴포넌트를 감싸주면 컴포넌트 트리 어느 곳에서나 쿼리 캐시 사용 가능하게끔 함
  - 전달되는 것은 절대로 변하지 않는 정적 객체인 query client
  - 이에 따라 불필요한 리렌더링이 트리거되는 것에 걱정할 필요 없음
- useQuery
  - cache와 상호작용하는 법
  - 내부적으로는 캐시에 있는 데이터가 변경될 때마다 useQuery가 QueryCache를 subscribe해 리렌더링을 함
    - 어떤 데이터를 사용해야 하는지?
    - 어디서 데이터를 가져와야 하는지?
  - queryKey
    - queryKey로 캐시된 데이터가 있으면 즉시 반환
    - 무조건 전역적으로 unique해야함
  - queryFunc
    - 없을 경우 func을 통해 가져온 데이터를 반환, 그 값을 쿼리에 저장
    - Promise를 반환해야만 함

### Deduplication

- queryKey에 캐시된 데이터가 있을 경우 queryFn을 중복호출하지 않고 데이터를 그대로 반환하는 것
- 관찰자 패턴
  - React 외부에 캐시가 있기 때문에 캐시의 값을 다시 React 컴포넌트로 동기화할 방법
  - 컴포넌트 마운트시 useQuery 호출에 대해 Observer 생성
  - Observer는 특정 query key를 바라보고 있음 
  - 해당 query key에 대한 변경이 생기면 observer가 감지하고 컴포넌트를 리렌더링
  - 각 컴포넌트가 캐시 데이터를 정확하게 표시하므로 예측 가능성을 높일 수 있고, queryFn을 필요할 때만 호출해 성능을 높일 수 있음

### The Query LifeCycle

- react query
  -  status
    - pending
    - success
    - error
  - 이 상태들은 queryFn에서 반환된 Promise 상태를 그대로 따르고 있음
  - boolean flag
    - isPending
    - isSuccess
    - isError