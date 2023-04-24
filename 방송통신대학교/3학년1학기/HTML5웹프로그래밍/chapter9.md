# HTML5웹프로그래밍

## 9강. CSS: 전환, 애니메이션, 다단

### 전환

- 어떤 이벤트에 대해서 지정한 시간 내에 속성의 특정 상태가 다른 상태로 부드럽게 변화하는 것
- 스타일의 점진적인 변화 -> 애니메이션 효과 부여

- 전환 지정 방법
  - 어떤 이벤트에 대해서 스타일 변화를 부여할 지를 지정
  - 전환 효과를 부여하려는 속성의 처음 상태와 최종 상태를 지정
- 전환 관련 속성의 설정
  - transition-property
    - 전환이 적용될 속성의 이름 나열
    - 여러 개인 경우에는 콤마로 구분
  - transition-duration
    - 전환이 진행되는 시간 지정
  - transition-delay
    - 전환 효과가 시작되기 전 대기 시간 지정
      - 전환이 바로 시작하지 않고 지정한 시간이 지난 후에 시작
  - transition-timing-function
    - 전환이 진행되는 속도의 형식 지정
      - 값
        - 아래 값들은 cubic-bezier 함수에 특정 값을 사용한 것을 일반적인 텍스트로 정의한 
        - ease
          - 느리게 시작해서 점점 빠르게 진행하다가 후반부에 다시 느리게 진행
        - linear
          - 처음부터 끝까지 일정한 속도로 진행
        - ease-in
          - 느리게 시작해서 점점 빠르게 진행
        - ease-out
          - 빠르게 진행하다가 느리게 종료
  - transition
    - 위 네 가지 속성을 한 번에 지정하는 속성
  - CSS의 모든 속성과 속성값에 전환 효과를 부여할 수 있는 것은 아님.

### 애니메이션

#### 키프레임

- 애니메이션을 구성하는 움직임의 키가 되는 프레임
  - 각 프레임을 연결하여 동작을 구성

#### 애니메이션 속성

transition과 거의 유사함.

- animation-name 속성
  - 키 프레임의 이름 지정
- animation-duration 속성
  - 애니메이션의 한 사이클이 실행되는 시간 지정
- animation-delay
- animation-timing-function
- animation-iteration-count
- animation-direction
  - 애니메이션의 진행 방향 지정
  - 값
    - noraml
    - reverse
    - alternate
    - alternate-reverse
- animation-play-state
  - 애니메이션의 실행 상태 또는 일시정지 상태 지정
    - 값
      - running
      - paused
- animation-fill-mode
  - 실행 이전 또는 실행 이후의 스타일의 유지 여부 지정
    - none
    - forwards
    - backwards
    - both

### 다단

#### 다단 지정

- columns: column-width 값 / column-count 값
- 두 값이 동시에 auto가 되면 안됨
- 단의 폭 지정 -> 단의 개수는 요소의 폭에 따라 자동으로 조정
  - 단의 최소 폭을 의미
- 단의 개수 지정 -> 단의 폭은 요소의 폭에 따라 자동으로 조정
  - 단의 최대 개수를 의미
- column-gap
  - 단과 단 사이의 간격 지정
- column-rule
  - 단과 단사이의 구분선 관련 속성 일괄 지정
  - border과 동일한 속성을 가지고 있으니 참조
- column-span
  - 해당 요소를 얼마나 많은 단을 차지해서 표시할 지 지정
    - 해당 요소에 설정된 다단을 무시하고 하나의 단으로 표시할 지 여부
    - 값
      - none
      - all
- column-fill
  - 각 단을 채우는 콘텐츠의 양을 조절하여 각 단의 높이를 차이를 최소할지를 지정
  - balance로 지정하면 각 단마다 일정하게 높이가 지정됨.



