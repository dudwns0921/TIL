# Java 프로그래밍

## java.lang 패키지

### Object 클래스

#### java.lang 패키지

- 자바 프로그래밍에 필요한 기본 클래스를 제공
  - java.lang 패키지에 존재하는 클래스를 사용할 때는 import문이 필요없음

#### Object 클래스와 주요 메소드

- 자동으로 모든 클래스의 조상이 되는 클래스
  - 클래스 계층 구조에서 루트가 되는 클래스
  - 모든 클래스는 자동으로 Object 클래스를 상속받음
- 주요 메소드
  - toString()
    - 객체의 문자열 표현을 반환
    - 어떠한 유형이든 Object 클래스를 상속받고 있기 때문에 toString 호출 가능
    - 자식클래스에서 재정의되어 있음
  - equals
    - 두 객체 변수를 비교해서 두 변수의 참조값이 같을 때 true를 반환
    - Object 클래스에서 equals()의 의미
      - obj1.equals(obj2)의 결과는 (obj1==obj2)와 같음
    - 자식 클래스에서 재정의할 수 있음
      - String, Integer 클래스 등에서 재정의되어 있음
      - Integer에서는 값이 같으면 true를 반환하도록 재정의되어있음
    - Object clone() 메서드
      - 객체를 복제하여 리턴함
      - Cloneable 인터페이스를 구현한 클래스의 객체만 clone() 메소드를 호출할 수 있음
      - 예외 처리 필요

### String 클래스

#### String 클래스와 생성자

- 문자열을 표현하고 처리하기 위한 클래스
- 기본 자료형처럼 다룰 수 있음
- String 객체는 내용이 변하지 않는 상수 객체
- 생성자에는 그냥 문자열, char 배열, char 배열과 시작점, 그리고 count 값을 넣을 수 있다.

#### 문자열의 비교 메소드

- int compareTo
  - 같으면 0을 리턴하고, 다르면 0이 아닌 정수값을 리턴함
- int compareToIgnoreCase
- boolean equals
  - 문자열이 같으면 true를 리턴하고, 다르면 false를 리턴함
- boolean equalsIgnoreCase(String anotherString)
  - 소문자 대문자 상관없음
- int indexOf
  - 처음 위치부터 문자열 str을 찾아 처음 등장하는 위치를 리턴함. 없으면 -1을 리턴함

#### 문자열의 추출 메소드

- char charAt
  - index 위치에 있는 문자를 리턴한다
- String substring(int beginIndex, endIndex)
  - beginIndex 위치부터 endIndex-1까지의 문자열을 리턴
  - endIndex가 없으면 끝까지

#### 문자열의 변환 메소드

- 원본 문자열은 변경되지 않고 새로운 객체가 만들어짐
- String replace
  - oldChar 문자를 newChar 문자로 변환하여 리턴함
- String trim
  - 문자열 앞과 뒤에 나오는 화이트 스페이스 문자를 제거하여 리턴함
- String toUpperCase
- String toLowerCase
- String concat(String str)
  - 두 문자열을 연결함

#### 다른 자료형을 문자열로 변환하는 메소드

- valueOf 메소드
  - String 클래스의 static 메서드
  - 주어진 자료형을 String으로 변환

#### 기타 메소드

- startsWith
- endsWith
- toCharArray

### StringBuffer 클래스

- 객체 생성 이후 문자열을 수정할 수 있는 기능을 제공
  - StringBuffer은 내용 변경이 가능한 mutable 클래스
- 내부적으로 문자열을 저장하기 위해 크기가 조절되는 버퍼를 사용함
- 생성자
  - StringBuffer()
    - 초기 버퍼의 크기는 16
  - StringBuffer(int length)
  - StringBuffer(String str)
    - 초기 버퍼의 크기는 str의 길이  + 16

#### 주요 메소드

- int capacity(), int length()
- char charAt(int index), int indexOf(String str)
- String substring(int start, int end)
- StringBuffer append(char c)
  - 인자를 String 표현으로 바꾸고 원 문자열 끝에 추가하여 반환함
  - 인자는 char[], Object, String, 기본 자료형도 가능함
  - String 클래스는 새로운 객체를 만드는 반면에 원본을 유지
- delete
- insert
- replace
- reverse

#### String 클래스를 사용할 때의 문제점

- 문자열을 빈번하게 변경하는 프로그램
  - String은 immutable 클래스
  - 기존 String 객체는 놔둔 채 새로운 String 객체가 계속 생성됨.

### 포장 클래스

#### 포장 클래스

- 기본형을 참조형으로 표현하기 위한 클래스
  - 기본형의 값을 가지고 객체로 포장함
- 사용 목적
  - 메소드의 인자로 객체가 필요할 떼
  - 클래스가 제공하는 상수를 사용할 때
  - 클래스가 제공하는 다양한 메소드를 사용할 때

- Number 클래스
  - Number는 Byte, Short, Integet, Long, Float, Double의 추상 부모 클래스
  - Number의 자식 클래스에서 구현된 주요 메소드
    - byte byteValue(), short shortValue()
      - 객체를 해당 기본형의 숫자로 변환
    - int compareTo
      - this와 인자를 비교하여 같으면 0을 리턴
    - boolean equals
      - 같은 유형이고, 값이 같으면 true를 리턴

#### String과 기본형 데이터 간의 변환

- 포장 클래스가 제공하는 static 메소드를 사용함
- String을 int 또는 long 형으로 변환할 때
  - parseInt, parseLong
- int형을 String 형으로 변환

#### Integer 클래스

- Integer, String, int 사이의 변환 기능을 제공
- 다른 클래스들도 유사한 기능을 제공함

#### 박싱

- 기본형 데이터를 포장 클래스의 객체로 변환하는 것
- 자동 박싱
  - 기본형에서 포장 클래스의 객체로 자동 변환하는 것
  - 인자에 전달되거나 변수에 대입될 때 적용됨

#### 언박싱

- 포장 클래스의 객체를 기본형 데이터로 변환하는 것
- 포장 클래스에서 기본형 Value() 메소드를 사용
- 자동 언박싱
  - 포장 클래스의 객체에서 기본형으로 자동 변환되는 것
  - 인자에 전달되거나 변수에 대입될 때 적용됨

### System 클래스

- Java 플랫폼 및 시스템과 관련된 기능 제공
  - 유용한 클래스 필드와 메소드를 가짐
  - 모든 멤버는 static, 사용 시 객체를 생성할 필요 없음
- 주요 기능
  - 표준 입출력
  - 배열 복사
  - JVM 또는 운영체제 속성과 시스템 환경 변수의 사용

#### System 클래스의 표준 입출력 필드

- System.in
  - 표준 입력 스트림으로 InputStream 유형
  - 키보드로부터 입력을 받을 때 사용
    - Systme.in.read()는 키보드로부터 1바이트 문자를 입력 받음
- System.out
  - 표준 출력 스트림으로 PrintStream 유형
  - 화면에 데이터를 출력할 때 사용
- System.err
  - 표준 에러 출력 스트림으로 PrintStream 유형
  - 오류 메시지를 화면에 출력할 때 사용

- 엔터 칠 경우, CR - 13 + LF - 10
