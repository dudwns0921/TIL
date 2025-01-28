# Query.gg

## Handling User Interactions

### Managing Mutations

- useQuery를 사용해 서버에 요청하는 게 실현되지 않는 이유
  - 쿼리는 컴포넌트가 마운트되면 즉시 실행됨
  - 하지만 실제로는 사용자의 특정 이벤트를 기다렸다가 실행이 되어야 함
  - enabled 옵션을 통해 이를 해결할 수도 있겠지만, 쿼리는 자동으로 여러 번 실행됨
  - 쿼리를 실행하는 건 멱등성이 보장되어야 함
  - React Query는 의도치 않은 결과 없이 원하는 만큼 자주 쿼리를 실행시킬 수 있어야 함
  - 하지만 Update는 멱등성이 보장되지도 않고 서버에 영향이 없지도 않음
  - 이를 위해 useMutations을 사용

- useMutation

  - 호출하면 mutate라는 메서드를 포함한 객체를 제공

  - mutate을 호출하면 React Query는 전달 받은 인수를 가져와 mutationFn을 실행

  - useMutation의 요점은 mutation의 라이프 사이클을 관리하는 것

  - status를 사용해 라이프 사이클을 관리

  - ```js
    function useUpdateUser() {
      const queryClient = useQueryClient()
    
      return useMutation({
        mutationFn: updateUser,
        onSuccess: (newUser) => {
          queryClient.setQueryData(['user', newUser.id], newUser)
        }
      })
    }
    ```

  - 성공했을 때 캐시를 업데이트

  - React Query는 데이터가 어디서 왔는지 구별하지 않음

  - staleTime 동안은 fresh한 데이터라고 인식

  - ```js
    function useUpdateUser() {
      const queryClient = useQueryClient()
    
      return useMutation({
        mutationFn: updateUser,
        onSuccess: (data, { id, newName }) => {
          queryClient.setQueryData(
            ['user', id], 
            (previousUser) => previousUser
              ? ({ ...previousUser, name: newName }) 
              : previousUser
          )
        }
      })
    }
    ```

  - 여기서 주의할 점은 setQueryData로 캐시를 업데이트할 때, 새로운 객체를 반환해주어야 한다는 점

  - 만약 previousUser을 그대로 반환한다면 React Query는 변경된 걸 인식하지 못함

  - React Query는 기존 데이터를 수정하는 게 아니라 새로운 데이터로 교체해주어야 한다는 의미

  - 쿼리 무효화

    - 캐시된 여러 항목을 업데이트해야 할 때, 각 항목을 일일이 수동으로 업데이트하기보다는 모든 항목을 무효화(invalidate)하는 것이 더 효율적
    - 쿼리를 무효화하면 모든 활성화된 쿼리를 refetch함
    - 남아있는 쿼리들을 모두 stale 상태로 변경
    - `queryClient.invalidateQueries`을 사용
    - Fuzzy Query Key matching
      - **부분 일치**:
        - 쿼리 키의 일부만 매칭시켜도 관련 쿼리를 찾을 수 있음
        - 예: `['todos', { status: 'done' }]`와 `['todos', { status: 'pending' }]`는 `todos`로 부분 일치 가능.
      - **배열 기반 키**:
        - 쿼리 키가 배열일 경우, 배열의 특정 부분만 매칭할 수 있음
        - 예: `['todos', 1]`과 `['todos', 2]`는 `todos`로 부분 일치 가능.
      - **와일드카드 사용**:
        - 정확한 키를 모르더라도 패턴을 사용해 쿼리를 무효화하거나 업데이트 가능
      - 이를 위해서 queryKey는 계층적으로 작성해야 함

### Optimistic Updates

- 방법
  - mutation 이후 최종 UI가 어떤 모습인지 안다면, 사용자에게 결과를 바로 보여줌
  - 그리고 서버에서 에러가 있다면 다시 롤백을 진행
- 적용 과정 (체크박스 예시)
  - 체크박스의 state는 캐시에 저장된 것과 반대
  - 쿼리가 정상적으로 실행됐다면 UI는 그대로 유지
  - 만약 쿼리가 실패한다면 원래 state로 복귀
- 여러 mutation이 연속적으로 발생하면 경쟁 조건이 발생할 수 있음
- 그래서 초기 체크박스의 state가 서버 상태와 일치하지 않는 경우가 발생
- 이를 위해 체크박스의 state를 변경하는 것이 아니라 캐시의 state를 변경
- 이는 onMutate라는 fn을 통해 구현 가능
- 만약 에러가 발생해 쿼리가 실패한다면, 변경된 캐시가 아닌 초기 상태의 캐시의 스냅샷이 필요
- onError에서는 세번째 인자로 rollback 메서드를 전달하고 있어, 이를 실행시키면 초기 상태의 스냅샷으로 돌아가게 됨
- 연속적인 mutation을 제한하기 위해 onMutate 에서 cancelQueries를 호출
- onSettled에서 invalidateQuries를 호출해 서버와의 sync를 맞춤

