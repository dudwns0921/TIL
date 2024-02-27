# 모바일 앱 프로그래밍

## 5강. 레이아웃1

### 1. ViewGroup 속성

#### ViewGroup

- 다양한 View에 대한 그룹 관리를 수행
- 스마트폰 화면에 어떻게 보여지는지 결정
- 계층적 관리 구조를 제공하여 화면 관리를 효율성을 높여줌
- 그릇에 해당하는 위젯과 View를 모아서 관리할 수 있는 쟁반 역할
- 각 View마다 ViewGroup 내부에서 표현되는 구체적인 형태를 지정 가능

#### layout_width와 layout_height

- View가 레이아웃에 배치될 때 크기를 결정하는 기준
- match_parent
  - View가 위치한 레이아웃의 크기에 맞춰 최대한의 크기로 출

#### layout_margin 속성

- View와 형제 View 사이의 간격을 지정하는 속성
- 4면의 여백을 동일하게 지정

### 2.LinearLayout

#### LinearLayout 개요

##### LinearLayout

- 내부 구성요소를 선형적으로 배치하는 ViewGroup

#### 1. orientation 속성

- LinearLayout 내부에 포함된 View들을 배치하는 방향 지정
- flex-direction과 비슷함

#### 2. baselineAligned 속성

- TextView 아래쪽을 기준으로 TextView들을 정렬해주는 속성
- View들이 수평으로 있을 때 적용되는 속성

### 3. LinearLayout2

#### 1. gravity 속성

- View 안쪽에 배치되는 TextView, ImageView와 같은 내용물의 정렬 방식을 결정하는 속성

#### 2. layout_weight 속성

- 상위 레이아웃의 영역에서 내부 레이아웃이나 위젯의 영역 할당 비율을 지정하는 속성