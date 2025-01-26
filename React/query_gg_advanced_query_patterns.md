# Query.gg

## Advanced Query Patterns

### Polling Data

- 기본 원칙

  - React Query는 최신의 데이터가 아니더라도 항상 캐시된 데이터를 즉각적으로 반환
  - 기본적으로 모든 쿼리는 staleTime이 0이므로 즉시 오래된 것으로 간주됨
  - 쿼리가 오래되면 React Query는 트리거가 발생할 때 데이터를 다시 가져와 캐시를 업데이트
  - 트리거
    - queryKey가 바뀌는 경우
    - 새로운 Observer가 마운트되는 경우
    - window가 focus 이벤트를 받는 경우
    - 장치가 온라인이 되는 경우

- 하지만 이러한 원칙은 특정 시점의 데이터 페칭을 고려하지 않음

- 이를 위해서는 React Query가 주기적으로 queryFn을 호출하도록 알려주어야 함

- 이 개념을 폴링이라고 하며, refetchInterval 속성을 통해 구현 가능

- 데이터가 자주 변경되고 캐시를 항상 최신 상태로 유지하려는 시나리오에 가장 적합

- refetchInterval 은 명시적으로 refetch했을 때도 리셋이 됨

- 서버 데이터를 활용해 폴링을 멈출 수 있음

- dataUpdatedAt 속성을 통해 최신 데이터 fetch한 timestamp를 얻을 수 있음


### Dependent Queries

- 요청들이 의존적인 경우
  - 예를 들어 영화 정보를 표시할 때 api 하나에서는 영화 정보만을, 다른 하나에서는 감독만을 반환할 경우
  - queryFn에 두 정보를 모두 가져오도록 연속적인 요청을 보낼 경우
    - 동작하지만 단점이 존재
    - 데이터의 일부만 가져올 수 없음
    - 두 요청중 하나만 실패하더라도 전체 쿼리는 오류 상태가 됨
    - 두 요청 모두 중복 제거가 없음
      - 가장 큰 단점
      - 같은 queryKey를 사용하기 때문
    - 위 경우에서는 영화와 감독을 별도의 query로 설정하는 것이 좋음
    - 둘은 완전히 다른 entity이기 때문
    - 이 때 종속 쿼리를 만들기 위해서는 enabled를 사용

### Parallel Queries

- 복잡한 애플리케이션에서는 여러 쿼리가 병렬로 수행될 가능성이 높으며 웹 개발에서는 더 많은 작업을 병렬로 수행할수록 좋음

- useQuries hook을 사용하면 Promise.all을 사용하는 것과 같이 쿼리를 연속적으로 수행 가능

  - useQuries는 자원 캐시를 개별적으로 할 수 있는 유연성을 제공하면서도 하나의 hook에서 호출 가능

- 작성한 순서대로 결과값을 반환

- 하나라도 쿼리가 pending일 경우

- ```js
  const areAnyPending = queries.some(
    query => query.status === 'pending'
  )
  ```

- useQuries 반환값을 결합하는 방법
  - map이나 reduce와 같은 js 배열 메서드 사용
  - useQuries의 combine 옵션 사용
- useQuries를 사용하지 않고 각 쿼리에 대해 별도의 컴포넌트를 렌더링할 경우, 모든 쿼리가 격리되어 있기 때문에 모든 쿼리를 기반으로 값을 도출하는 것이 어려움

### Avoiding Loading States

- React Query에는 인디케이터 관리를 도와주는 내장 API가 존재

- 프리패칭을 통해 사용자가 데이터를 요청하기 전에 미리 가져와 캐시할 수 있음

- 모든 데이터를 프리패칭하게 되면 오버페칭을 발생

- 사용자 마우스 커서가 앵커 태그에 진입하면 프리패칭 시작

- 프리패칭은 어떠한 데이터도 반환하지 않음

- staleTime이 없다면 마우스 커서가 진입할 때마다 query를 새롭게 요청

- ```jsx
  <a
    onClick={() => setPath(post.path)}
    href="#"
    onMouseEnter={() => {
      queryClient.prefetchQuery({
        queryKey: ['posts', post.path],
        queryFn: () => fetchPost(post.path),
        staleTime: 5000
      })
    }}
  >
    {post.title}
  </a>
  ```

- 프리패칭을 사용하더라도 응답이 느리다면은 여전히 로딩 인디케이터가 표시될 가능성이 높음

- 이때는 초기 데이터를 설정해 일부 데이터라도 사용자에게 보여줄 수 있음

- 이 때 queryClient을 사용해 캐시에 접근할 수 있음

- ```js
  function usePost(path) {
    const queryClient = useQueryClient()
    return useQuery({
        ...getPostQueryOptions(path),    
        placeholderData: () => {      
            return queryClient.getQueryData(['posts'])        
                ?.find((post) => post.path === path)    
        }  
    })}
  ```

- isPlaceholderData flag를 통해 사용자가 어떤 데이터를 보고 있는지 알 수 있음
- initialData라는 속성도 있는데, placeHolderData와는 달리 initialData는 캐시에 종속적
- 따라서 initialData는 placeHolderData와 달리 완전한 데이터 형태를 갖추고 있어야 함

### Pagination

- 대규모 데이터 세트를 효율적으로 처리하기 위해 페이지네이션을 구현
- API는 페이지네이션을 위해 `page`와 `per_page`라는 매개변수를 제공
  - `page`는 요청할 페이지 번호를, `per_page`는 한 페이지당 반환할 레코드 수를 지정
  - API는 이 매개변수를 기반으로 전체 데이터 중 해당하는 부분만 반환
  - 응답에는 데이터와 함께 총 레코드 수, 현재 페이지 번호, 총 페이지 수 등의 메타데이터가 포함
  - 다음 페이지의 데이터를 가져오려면 `page` 값을 증가시키고, `per_page`는 동일하게 유지하여 요청을 반복
  - 이 방식을 통해 전체 데이터 세트를 한 페이지씩 탐색할 수 있음
- 장점
  - 데이터 양을 줄여 성능 개선
  - 애플리케이션에서 데이터를 효율적으로 검색하고 표시할 수 있도록 함

- placeHolderData flag를 사용해서 캐시된 데이터가 있기 전까지 이전 데이터를 보여주도록 함

- ```jsx
  <ul style={{ opacity: isPlaceholderData ? 0.5 : 1 }}>
  ```

- ```js
  function useRepos(sort, page) {
    return useQuery({
      queryKey: ['repos', { sort, page }],
      queryFn: () => fetchRepos(sort, page),
      staleTime: 10 * 1000,
      placeholderData: (previousData) => previousData
    })
  }
  ```

### Infinite Queries

- 새로운 데이터를 받을 때마다 추가가 가능한 단일 캐시 항목이 필요

- useInfiniteQuery hook을 사용

- page를 react 대신 useInfiniteQuery가 관리

- ```js
  function usePosts() {
    return useInfiniteQuery({
      queryKey: ['posts'],
      queryFn: ({ pageParam }) => fetchPosts(pageParam),
      initialPageParam: 1,
      getNextPageParam: (lastPage, allPages, lastPageParam) => {
        if (lastPage.length === 0) {
          return undefined
        }
  
        return lastPageParam + 1
      }
    })
  }
  ```

- queryFn의 인자로  쿼리 자체에 대한 정보가 담긴 객체를 전달

- getNextPageParam

  - `lastPage`마지막 페이지에서 가져온 데이터
  - `allPages`지금까지 가져온 모든 페이지의 배열
  - `lastPageParam``pageParam`마지막 페이지를 가져오는 데 사용된 것

- useQuery가 캐시된 데이터 전체를 반환하는데 반해, useInfiniteQuery는 아래와 같은 형태의 데이터를 반환

- ```js
  {
   "data": {
     "pages": [
       [ {}, {}, {} ],
       [ {}, {}, {} ],
       [ {}, {}, {} ]
     ],
     "pageParams": [1, 2, 3]
   }
  }
  ```

- Array.flat을 사용해 2차원 배열에서 일반 배열을 얻을 수 있음

- fetchNextPage메서드를 실행시키면 그 다음 데이터를 가져옴

- isFetchingNextPage flag 사용 가능

- ```js
    getPreviousPageParam: (firstPage, allPages, firstPageParam) => {
      if (firstPageParam <= 1) {
        return undefined
      }
  
      return firstPageParam - 1
    }
  ```

- ```js
    const [ref, entry] = useIntersectionObserver();
  
    React.useEffect(() => {
      if (entry?.isIntersecting && hasNextPage && !isFetchingNextPage) {
        fetchNextPage()
      }
    }, [entry?.isIntersecting, hasNextPage, isFetchingNextPage])
  ```

- ```jsx
    return (
      <div>
        {data.pages.flat().map((post, index, pages) => (
          <p key={post.id}>
            <b>{post.title}</b>
            <br />
            {post.description}
            {index === pages.length - 3
                ? <div ref={ref} />
                : null}
          </p>
        ))}
      </div>
    )
  ```

- ref를 통해 바닥에 있는 요소를 가져와 관찰하면서 바닥에 닿았을 경우 fetchNextPage 메서드를 실행

- refetch

  - 일부만 refetch한다면 일관성을 보장할 수 없음
  - 항상 전체 페이지를 refetch해야만 함
  - 캐시에 페이지가 너무 많으면 문제 발생
  - 이를 위해 캐시에 보관하는 페이지 수를 제한하는 옵션을 사용 가능
    - maxPages
