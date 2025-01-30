# D3js

https://paullabworkspace.notion.site/D3-js-44bff65b641b46eba9b7685860a771cc

## D3의 개념과 도형 그리기

- Data Driven Documents의 약자

- SVG를 통해 깨짐없는 시각화 가능

- 데이터를 시각화하려는 목적

- 러닝커브가 있지만 커스터마이징이 쉬움

- 동작 과정

  - 데이터 로딩
  - 코드 연동
  - 그래프의 색상, 축 등 설정
  - 클릭 등의 효과 지정

- svg

  - circle

    - cx : 중심 x 좌표
    - cy : 중심 y 좌표
    - r : 반지름

  - rect

    - stroke-width

      - width, height와 상관없이 실제 크기가 더 커질 수 있음

      - `r=50`이면, 원의 지름이 100px인데, `stroke-width=100`이면 `100/2 = 50px`씩 양쪽으로 퍼짐.

        따라서 실제 크기가 200px (100px + 50px + 50px)처럼 보일 수도 있음

  - path

    - d : 경로를 그리는 명령어들의 조합
    - M : 펜을 움직여서 시작 위치를 설정하는 명령어

  - g

    - 그룹화를 위해 사용

  - text

    - legend, label, caption 등으로 사용
    - 일반 html 태그를 사용하지 않음
    - 작동은 하나 x축, y축 이동이 되지 않음

## SVG

- 확장 가능한 벡터 그래픽

- XML 기반의 2차원 그래픽

- HTML 태그의 집합으로 이루어져 있음

- css, js로 컨트롤이 가능

- 장점

  - 아무리 확대해도 깨지지 않음

- 단점

  - 복잡한 이미지일수록 파일 사이즈가 커짐
  - 아이콘 위주로 사용

- hover 효과 추가

  - ```css
    path:hover {
    	fill: red;
    }
    ```

- svg가 나오지 않을 때는 width, height 속성이 설정되어있는지 확인
