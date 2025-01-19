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

