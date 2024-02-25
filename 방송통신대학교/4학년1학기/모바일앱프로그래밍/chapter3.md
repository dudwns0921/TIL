# 모바일 앱 프로그래밍

## 3강. 문자 및 이미지 출력을 위한 위젯

### 1. TextView

#### 3. textSize 속성

- 텍스트 단위는 dp, sp 등 사용
- dp
  - 고정 크기
  - 해상도에 따라 달라짐
- sp
  - 해상도와 무관하게 지정해놓은 크기
  - sp가 가변적인 크기이기 때문에 sp를 사용하는 것이 좋음

### 2. ImageView

#### 1. src 속성

##### src 속성을 통한 이미지 출력

- 리소스 폴더에 이미지 복사
- @drawalbe/ID 형식으로 이미지의 ID를 지정
- 해당 ID를 사용해서 ImageView의 표면에 그림을 출력

#### 2.이미지 포맷

- png
  - 투명도 설정 가능한 알파 채널이 존재
  - 실용성이 높음

#### 4. adjustViewBounds

- true
  - 원본의 종횡비가 유지되면서 maxWidth, maxHeight에 제한을 받음
- false
  - 이미지의 가로와 세로가 화면 전체를 채우게 됨

#### 5. cropToPadding

- true
  - ImageView를 감싸는 레이아웃에 적용된 padding의 크기가
  - ImageView 영역까지 포함된 경우
  - 겹치는 부분을 잘라냄
- false
  - padding이 비활성화되고 이미지 원본이 모두 보임

#### 6. scaleType

- 다양한 해상도를 가진 원본 이미지를 항상 스마트폰 화면에 원하는 형태로 배치하기 위한 속성

#### 7. ImageView 프로젝트

##### 이미지 리소스 ID

- 이미지 파일을 res 폴더에 복사만 해 놓으면 AAPT가 컴파일 전에 res 폴더에서 새로 추가된 이미지 파일을 찾아내어 파일명 ID를 자동으로 R.java에 정의 및 등록
- 프로그래머가 임의로 변경 불가