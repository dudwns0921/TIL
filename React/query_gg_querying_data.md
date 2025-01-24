# Query.gg

## Querying Data

### Fetching Data

- react query는 데이터를 가져오는 요청에 아무런 영향을 끼치지 않음

- 그렇기 때문에 데이터를 가져오는 요청은 react query가 없을 때와 동일하게 처리하면 됨

- fetch는 status 응답 코드가 4xx 5xx에 있으면 프로미스 reject를 하지 않음

- ```js
  const fetchRepos = async () => {
    try {
      const response = await fetch('https://api.github.com/orgs/TanStack/repos')
  
      if (response.ok) {
        const data = await response.json()
        return data
      } else {
        throw new Error(`Request failed with status: ${response.status}`)
      }
    } catch (error) {
      // handle network errors
    }
  }
  ```

- ```js
  function useRepos() {
    return useQuery({
      queryKey: ['repos'],
      queryFn: async () => {
        const response = await fetch('https://api.github.com/orgs/TanStack/repos')
        
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`)
        }
  
        return response.json()
      },
    })
  }
  ```

  - queryFn에서 사용할 때 try/catch 구문 제거 가능
  - queryFn에서는 프로미스 객체를 리턴하도록 되어있기 때문에 json()을 그대로 반환 가능

### Managing Query Dependencies

- ```js
  function useRepos(sort) {
    return useQuery({
      queryKey: ['repos'],
      queryFn: async () => {
        const response = await fetch(
          `https://api.github.com/orgs/TanStack/repos?sort=${sort}`
        )
        
        if (!response.ok) {
          throw new Error(`Request failed with status: ${response.status}`)
        }
  
        return response.json()
      },
    })
  }
  ```

- sort를 전달해 동적으로 api 요청을 날리더라도 queryKey의 값이 동일하기 때문에 캐시된 값을 반환

- queryKey 배열에 sort 값을 전달해 문제를 해결

- react query가 의존성에 따라 데이터를 저장하기 때문에 서로 다른 인자를 갖는 요청들은 데이터가 겹칠 수가 없음

### Data Synchronization

- 서버는 살아있는 것
- 서버와 클라이언트 상태를 동기화시키기 위해 캐시 무효화, 즉 캐시를 서버와 동기화해야 함
- 대부분 캐시 기본 구성은 일정 기간 후에 캐시를 무효화
- response의 header의 cache-control을 통해 얼마만의 시간 동안 캐시가 유지되는지 알 수 있음
- React Query는 실제로 요청하는 주체가 아니기 때문에 cache-control에 대해 알지 못함
- 다행히 React Query는 stale time이라는 비슷한 개념을 가지고 있음
- stale은 fresh의 반대
- stale의 기본값은 0으로 모든 쿼리가 즉시 오래된 것으로 간주됨
- stale의 값은 상황에 따라 달라져야 하며 이 판단은 개발자가 해야 함
- stale이 true일 때 캐시된 데이터를 전달하고 React Query는 백그라운드에서 다시 서버와 동기화하고 캐시를 업데이트
- 이 캐싱 전략은 Stale While Revalidate라는 전략
- React Query가 UI를 업데이트하는 동시에 데이터를 최신 상태로 유지하여 UX를 최적화할 수 있기 때문
- 동기화 진행하는 트리거
  - queryKey 변경시
  - 새로운 관찰자 생성시
  - 사용자가 애플리케이션이 실행중인 탭으로 돌아왔을 때
  - 장치가 온라인 상태가 됐을 때
- 만약 데이터가 절대로 변경되지 않을거라고 생각한다면 staleTime을 무한대로 설정할 수 있음
- 정리
  - React Query는 최신이 아니더라도 항상 캐시된 데이터를 제공
  - 기본적으로 모든 쿼리는 staleTime이 0으로 기본 설정되어 즉시 오래된 것으로 간주됨
  - 쿼리가 오래되면 React Query는 트리거가 발생할 때 데이터를 다시 가져오고 캐시를 업데이트
  - 모든 트리거를 비활성활 수 있지만 리소스를 얼마나 오랫동안 새 것으로 간주해야 하는지 생각하고 이를 staleTime으로 구성하는 것이 좋음

### Fetching on demand

- 구성 요소가 마운트되는 시점에 즉시 데이터를 가져오는 것이 일반적

- enabled 속성을 통해 쿼리 함수를 실행할지 말지 여부를 결정할 수 있음

- 쿼리 함수를 실행시키지 않았을 때 status는 pending

- pending은 단순히 데이터가 없고 error도 없다는 것을 의미

- 다만 우리는 실제 쿼리 함수가 실행중인지 아닌지를 확인해야 함

- 이는 fetchStatus를 통해 알 수 있음

- pending과 fetchStatus의 조합은 너무 일반적이라서 react-query에서는 isLoading이라는 flag를 제공

- 하지만 isLoading은 pending인 상태에서 fetch를 하지 않았을 경우 false이기 때문에 data 자체에 접근하지 못하는 오류가 발생할 수 있음

- 그래서 데이터가 캐시에 있는 상황, status가 success일때만 데이터에 접근해야만 함

- 리액트에서는 useQuery를 반환하는 컴포넌트를 조건부 처리해서 enabled과 비슷한 효과를 낼 수 있음

- 아래 코드는 isLoading으로 대체 가능

- ```js
  if (status === 'pending') {
    if (fetchStatus === 'fetching') {
      return <div>...</div>
    }
  }
  ```

### Garbage Collection

- 캐시에 데이터가 있다는 건 반응성 있는 앱이라는 걸 의미하지만, 캐시의 데이터가 오래되고 관련이 없다면 이는 단점이 더 많음
- 이를 위해 React-Query는 Garbage Collection을 수행
- 기본값은 5분이지만, 5분이 지난다고 무조건 Garbage Collection이 수행되는 것은 아님
- 활발하게 사용될 경우 Garbage Collection의 대상이 아님
  - Observer가 남아있지 않은 경우
  - DOM에서 사라질 경우 Observer은 사라짐
- 검색 기능의 예시
  - 모든 검색은 새로운 캐시 항목을 생성
  - 5분안에 같은 용어를 검색하면 캐시에서 데이터가 제공됨, 데이터가 stale일 경우 refetch를 통해 가져오기도 함
  - 하지만 5분이 지난 후 초기 Observer가 사라진 다음에 검색을 하면 캐시 항목은 삭제됨
- gcTime을 사용자가 원하는 대로 설정 가능
