# HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>이게 이 문서의 제목이야</title>
</head>
<body>
    
</body>
</html>
```



## Tag

HTML의 목적은 웹사이트의 콘텐츠가 어떻게 구성되어있는지 브라우저에게 알려주는 것이다.

이 목적을 위해 사용하는 것이 바로 태그(tag)이다.

```html
<food spicy_level="Hell">kimchi</food>
<!-- 실제로는 존재하지 않는 태그와 속성 -->
```

태그는 위와 같이 사용한다.

태그 안의 있는 내용이 웹사이트의 콘텐츠가 되고, 태그는 그 콘텐츠가 웹사이트에서 어떤 구조에 해당하는지를 말해준다.



### Attribute

예시로 든 food 태그 안을 보면 `spicy_level="Hell"`부분을 확인할 수 있다.

이 부분은 Attribute(속성)이라고 하며, 태그의 부가적인 정보를 추가하는데 사용한다.



위의 예시는 엄청 매운 맛의 김치라는 음식을 나타낸 태그라고 할 수 있다.



## DOCTYPE 선언

DOCTYPE 선언은 HTML 문서에서` <html>` 태그를 정의하기 전에 가장 먼저 선언되어야 한다.

이러한 DOCTYPE 선언은 태그는 아니지만, 선언된 페이지의 html 버전이 무엇인지를 웹 브라우저에 알려주는 역할을 한다.

각 버전별로 선언하는 방법이 다르며 예시에서 선언된 건 html5 버전이다.



## html

`<html>`태그는 HTML 문서의 루트 요소(root element)를 정의할 때 사용한다.

`<html>` 요소는 DOCTYPE 선언을 제외한 모든 다른 html 요소를 포함하기 위한 컨테이너이다.

브라우저에게 해당 문서가 html 문서임을 알려주는 역할을 한다.



lang 속성은 이 웹사이트의 주언어가 무엇인지 브라우저에게 알려주는 역할을 한다.

위 예시에서 주언어는 한국어로 되어있다.



## Head

HTML 문서는 크게 head와 body라는 두 부분으로 나누어진다.

`<head>`태그는 해당 문서에 대한 정보인 메타데이터의 집합을 정의할 때 사용한다.

다시 말하면 브라우저에게 이 문서에 대한 정보를 제공해주는 부분이라고 볼 수 있다.

`<head>`태그에 들어가 있는 정보들은 웹사이트에서는 볼 수 없다.



위 예시의 `<title>`태그는 HTML 문서의 제목을 알려주는 역할을 한다.

`<meta>`요소는 `<title>`과 같은 다른 메타데이터 관련 요소들이 나타낼 수 없는 다양한 종류의 메타데이터를 나타낼 때 사용된다.

`<meta charset=UTF-8>`에서 charset이라는 속성은 브라우저한테 텍스트를 어떻게 표현할 것인지 요청한다.

영어가 아닌 한글이나 다른 특수문자가 있는 언어를 입력할 때, 브라우저가 이해하지 못하는 경우가 있어 글자가 깨질 수도 있다.

이러한 상황을 미연에 방지하기 위해 브라우저에게 텍스트를 이렇게 표현해달라고 요청하는 것이다. 



## Body

`<body>`태그는 해당 HTML 문서의 텍스트, 하이퍼링크, 이미지, 리스트 등과 같은 모든 콘텐츠를 포함하는 영역을 정의할 때 사용한다.

쉽게 말하면 웹사이트에 나타나는 콘텐츠들을 작성하는 부분이다.

HTML 문서에는 단 하나의 body 요소만이 존재할 수 있다.



# 참고자료

http://tcpschool.com/

노마드코더 카카오톡 클론코딩 수업 내용
