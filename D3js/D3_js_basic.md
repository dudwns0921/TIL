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

## 막대 그래프 그리기

- filter, map, forEach 메서드는 D3에서 많이 사용되는 메서드

- ```html
      <svg width="500" height="500"></svg>
      <script>
        const sampleData = [100, 10, 30, 50, 10, 70, 200, 90];
        const svg = d3.select("svg");
        const maxHeight = 300
  
        sampleData.forEach((data, index) => {
          svg
            .append("rect")
            .attr("height", data)
            .attr("width", 30)
            .attr("x", 30 * index) //막대 생성좌표 x 막대의 좌측
            .attr("y", maxHeight - data); //막대 생성 좌표 y 막대의 윗부분
        });
      </script>
  ```

- svg를 select 메서드로 가져와 데이터를 순회하며 도형을 생성

- x,y 좌표에서부터 height만큼 도형이 생성되기 때문에 최대 y값에서 데이터를 빼는 형태로 설정을 해야함

- ```js
        sampleData.forEach((data, index) => {
  		...
  
          svg
            .append("text")
            .attr("x", 30 * index + 15) //텍스트 생성 좌표 x 막대의 중앙
            .attr("y", maxHeight - data - 5) //텍스트 생성 좌표 y 막대의 윗부분에서 5만큼 위로
            .attr("text-anchor", "middle") //텍스트 정렬
            .text(data); //텍스트 내용
        });
  ```

- "텍스트 앵커(text-anchor) 속성은 미리 포맷된 텍스트나 자동 줄 바꿈된 텍스트를 정렬하는 데 사용

- 여기서 줄 바꿈 영역은 inline-size 속성에 의해 결정되며, 주어진 지점을 기준으로 텍스트를 시작, 중간 또는 끝 정렬

- ![image-20250202192125832](.\md-images\image-20250202192125832.png)

- ```js
        sampleData.forEach((data, index) => {
          svg
          ...
  
            .transition()
            .duration(3000)
            .ease(d3.easeLinear)
            .style("fill", "red")
            .attr("y", maxHeight - sampleData2[index])
            .attr("height", sampleData2[index]);
        });
  ```

- 기존 attr로 적용했던 fill을 transition에서는 style로 적용

- y좌표뿐만 아니라 height까지 데이터에 맞게 변경해주어야 정상적으로 동작
