# Oracle Cloud Free tier 서버 튜토리얼

> 아래는 가장 기본적인 인스턴스 설정임을 참고

## 인스턴스 만들기

### 1. 계정 생성 및 로그인

- Oracle Cloud 무료 계정 생성
- 로그인 후 클라우드 콘솔 접속

### 2. 인스턴스 생성 시작

- 클라우드 콘솔에서 Compute > Instances 메뉴로 이동
- Create Instance 클릭하여 새 인스턴스 생성 시작

### 3. 이미지 선택 (Image)

- OS 이미지는 범용성 높은 Ubuntu 버전 추천 (예: Ubuntu 22.04)

### 4. 보안 설정 (Security)

| 보안 옵션              | 설명                                                         | 권장 여부                   |
| ---------------------- | ------------------------------------------------------------ | --------------------------- |
| Shielded Instances     | VM 부팅 시 무결성 검증, 루트킷/부팅키트 방어 등 기본 보안 강화 기능 | 가능하면 활성화 권장        |
| Confidential Computing | 메모리 내 데이터 암호화 처리 (고급 하드웨어 보안)            | 매우 높은 보안 요구 시 고려 |

- 보안 강화가 필요하면 Shielded Instances 켜기
- Confidential Computing은 비용과 제약 고려하여 필요 시 선택

### 5. 네트워크 설정

- VCN (Virtual Cloud Network) 신규 생성
  - VCN이란 가상 클라우드 네트워크로 클라우드 내에서 가상의 사설 네트워크를 만드는 것
- 서브넷 신규 생성 (공용 서브넷 권장: 인터넷 접속 가능)
  - 서브넷이란 VCN 안에서 IP 주소 범위를 더 작게 나눈 네트워크 영역
- VNIC (Virtual Network Interface Card) 설정
  - VNIC란 인스턴스에 할당되는 가상의 네트워크 인터페이스 카드
  - 물리적 서버의 네트워크 카드와 비슷한 역할을 하며, 인스턴스가 네트워크와 통신할 수 있도록 연결해줌
  - 설정 항목
    - ![image-20250716093501779](./md-images/image-20250716093501779-1752626103753-1.png)
    - Private IPv4 주소 자동 또는 수동 할당
    - 공인 IP 주소 할당 여부 결정 (외부 접속 필요 시 할당 필수)

### 6. SSH 키 추가

- Generate a key pair for me 선택
  - 개인키는 안전하게 보관 후 이후 ssh 접속 시 사용

### 7. 부팅 볼륨 (Boot Volume) 설정

| 설정 항목                              | 설명                                   | 권장 설정                       |
| -------------------------------------- | -------------------------------------- | ------------------------------- |
| 크기 (Size)                            | 기본 46.6GB (Ubuntu OS 용량)           | 기본 유지, 필요시 증설 가능     |
| 인-트랜짓 암호화 (Use in-transit)      | 인스턴스와 볼륨 간 데이터 전송 암호화  | 활성화 권장                     |
| 사용자 관리 키 (Customer-managed keys) | 기본 Oracle 관리 키, 직접 키 관리 가능 | 특별 보안 요구 없으면 기본 사용 |

### 8. 블록 볼륨 (Block Volume) 설정

- 기본 설정 유지 (추가 블록 볼륨 연결 필요 없으면 건드리지 않음)

## 네트워크 설정

### 외부 접속을 위해 반드시 필요한 4가지 설정

> 아래 내용은 공인 IP가 할당된 서브넷을 사용하는 경우에 해당

#### 1. 서브넷 보안 규칙(Security Lists) 추가

- 인스턴스가 속한 서브넷의 방화벽 역할
- 필요한 포트(TCP 22, 8000 등)와 프로토콜(TCP, ICMP 등)을 허용하는 인그레스/이그레스 규칙 설정 필수
- ![image-20250716094331599](./md-images/image-20250716094331599-1752626614736-3.png)

#### 2. 네트워크 보안 그룹(NSG) 보안 규칙 추가

- 인스턴스의 네트워크 인터페이스(VNIC)에 적용되는 세분화된 방화벽
- 서브넷 보안 규칙과 별개로 작동하며, 양쪽 모두 허용되어야 트래픽이 통과 가능
- 마찬가지로 필요한 포트와 프로토콜을 허용하는 인그레스/이그레스 규칙 설정 필요
- ![image-20250716094458371](./md-images/image-20250716094458371.png)

#### 3. 라우트 룰(Route Rules) 추가

- 인스턴스가 인터넷으로 나가는 경로(Route)를 설정
- 목적지 `0.0.0.0/0` → 인터넷 게이트웨이(Internet Gateway) 설정 필수
- 이 설정이 없으면 인스턴스가 외부와 통신할 수 없음
- ![image-20250716094631924](./md-images/image-20250716094631924.png)

#### 4. 고정 IP 할당

- 이 부분은 외부 통신과는 관련이 없으나 IP가 유동적으로 바뀌기 때문에 기존 IP로 접속 시 접속이 안되는 경험을 할 수도 있기 때문에 설정하는 것.

https://velog.io/@kimsoohyun/Oracle-cloud-4
