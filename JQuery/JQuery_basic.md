# jQuery

## Basic

### 정의

- jQuery는 빠르고 작으며 기능이 풍부한 JavaScript 라이브러리
- 다양한 브라우저에서 작동하는 사용하기 쉬운 API로 HTML 문서 탐색 및 조작, 이벤트 처리, 애니메이션, Ajax와 같은 작업을 훨씬 더 간단하게 만들어줌

### 사용 방법

CDN을 통해 jQuery 라이브러리를 사용하고, 예시를 만들어보았다. 여기서 CDN은 **Content Delivery Network**의 약자로, 웹 콘텐츠를 빠르게 제공하기 위해 전 세계 여러 서버에 데이터를 분산 저장하고, 사용자가 요청할 때 가장 가까운 서버에서 데이터를 제공하는 시스템이다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <a>Hello World!</a>
    <script
      src="https://code.jquery.com/jquery-3.7.1.min.js"
      integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
      crossorigin="anonymous"
    ></script>
    <script>
      $(document).ready(function () {
        $("a").click(function (event) {
          alert("Thanks for visiting!");
        });
      });
    </script>
  </body>
</html>

```

### $

- $는 jQuery 객체를 선택하고 조작하는 데 사용되는 축약형

##### 이벤트 리스너 구현

- $을 통해 DOM의 요소를 선택하고 event명으로 된 함수에 이벤트 리스너를 넘기는 방식으로 구현

##### 클래스 처리

- addClass

  - ```js
    $('#myElement').addClass('active');
    ```

- removeClass

  - ```js
    $('#myElement').removeClass('active');
    ```

##### 비동기 처리

- ajax

  - ```js
    $.ajax({
      url: 'https://example.com/api',  
      type: 'GET',                     
      dataType: 'json',                
      success: function(response) {    
        console.log('응답 데이터:', response);
      },
      error: function(xhr, status, error) {
        console.error('에러 발생:', error);
      }
    });
    ```

- get

  - ```js
    $.get('https://example.com/api', { key1: 'value1', key2: 'value2' }, function(response) {
      console.log('성공:', response);
    }).fail(function(xhr, status, error) {
      console.error('에러:', error);
    });
    ```

- post

  - ```js
    $.post('https://example.com/api', {
      key1: 'value1',
      key2: 'value2'
    }, function(response) {
      console.log('성공:', response);
    }).fail(function(xhr, status, error) {
      console.error('에러:', error);
    });
    ```

# :books:참고자료

- https://jquery.com/
- https://learn.jquery.com/about-jquery/how-jquery-works/
