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