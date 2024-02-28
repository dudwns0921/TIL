# 모바일 앱 프로그래밍

## 6강. 레이아웃2

AbsoluteLayout은 잘 사용되지는 않음. 나머지는 효율성 때문에 개발자들이 많이 사용

### 1. RelativeLayout

#### RelativeLayout 개요

- ViewGroup에서 View들 사이의 상대적인 관계를 이용하여 View의 위치를 지정하고 배치
- 특정 View와 다른 View 사이의 관계를 지정하려면 해당 View를 지칭하기 위한 식별자 필요
- R.java에 등록되어 있어야 함

#### 3. RelativeLayout의 제약사항

- 기준이 되는 다른 View가 먼저 정의되어 있어야 종속되는 View 위치가 정해짐
  - 특정 View에 종속되는 View가 있음
- 사용자의 화면에 보이는 View의 순서와 레이아웃 XML 상의 View의 정의 순서가 다를 수 있음
- 유지보수 어려움
  - 기준이 되는 View를 삭제되거나 위치를 이동하게 되면, 종속되는 View는 원하는 위치를 결정하지 못하게 됨

### 2. AbsoluteLayout

#### AbsoluteLayout

- 관계나 순서에 상관없이 지정한 절대 좌표에 자식 View를 배치

### 3. FrameLayout

#### FrameLayout

- 모든 자식 View가 FrameLayout의 좌측 상단에 나타나는 레이아웃
- XML 코드에 정의한 순으로 아래부터 자식 View가 놓여지게 