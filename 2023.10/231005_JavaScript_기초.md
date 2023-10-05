### JavaScript

- JavaScript
  
  - 객체(object) 기반의 스크립트 언어
  
  - `HTML`로는 **웹의 내용**을 작성하고, `CSS`로는 **웹을 디자인**하며, `자바스크립트`로는 **웹의 동작**을 구현
  
  - 주로 웹 브라우저에서 사용되나, Node.js와 같은 프레임워크를 사용하면 서버 측 프로그래밍에서도 사용할 수 있음

- 특징
  
  - 프로토타입(prototype) 기반의 객체 지향 언어
  
  - 동적이며, 타입을 명시할 필요가 없는 인터프리터 언어
    
    - 인터프리터 언어
      
      - 컴파일 작업을 거치지 않고, 소스 코드를 바로 실행할 수 있는 언어
  
  - 객체 지향형 프로그래밍과 함수형 프로그래밍을 모두 표현할 수 있음

- 작업
  
  - HTML 내용 변경
    
    - 버튼 클릭 시 div 태그 내용 변경
  
  - HTML 속성 변경
    
    - 버튼 클릭 시 img 태그 속성 변경
  
  - HTML 스타일 변경
    
    - 버튼 클릭 시 p 태그 스타일 변경

- 문법
  
  - 실행문은 세미콜론(;)으로 구분
  
  - 대소문자 구분
  
  - 식별자(identifier)
    
    - 변수나 함수의 이름을 작성할 때 사용하는 이름
    
    - 자바스크립트에서는 영문자(대소문자), 숫자, 언더스코어(_) 또는 달러($)만 사용 가능
      
      - 숫자로 시작할 수는 없음
    
    - 관행적으로 `Camel Case 방식`을 많이 사용
      
      - camelCase, computerDesk
  
  - 예약어(reserved word)
    
    - 미리 예약된 단어
    
    - var, function 등
  
  - 주석(comment)
    
    - 한 줄 주석
      
      ```javascript
      // 주석
      ```
    
    - 여러 줄 주석
      
      ```javascript
      /* 주석 */
      ```
    
    - 여러 줄 주석 내부에 또 다른 한 줄 주석을 삽입할 수 있음

- 출력
  
  - window.alert() 메소드
  
  - HTML DOM 요소를 이용한 innerHTML 프로퍼티
    
    - getElementById, innerHTML 등
  
  - document.write() 메소드
    
    - 웹 페이지가 로딩될 때 실행되면, 웹 페이지에 가장 먼저 데이터를 출력
    
    - 대부분 테스트나 디버깅을 위해 사용
      
      ```javascript
      document.write(48 * 5);
      ```
  
  - console.log() 메소드
    
    - 웹 브라우저의 콘솔을 통해 데이터를 출력

- 적용
  
  - 내부 자바스크립트 코드로 적용
    
    - `<script>태그`를 사용하여 HTML 문서 안에 삽입
    
    - HTML 문서의 <head>태그나 <body>태그, 또는 양쪽 모두에 위치할 수 있음
      
      - 자바스크립트 코드를 <head>태그에 삽입하나 <body>태그에 삽입하나 동작상의 차이는 없음
  
  - 외부 자바스크립트 파일로 적용
    
    - 외부 파일로 생성하여 삽입
    
    - .js 확장자를 사용하여 저장 후 해당 자바스크립트 파일을 적용하고 싶은 모든 웹 페이지에 `<script>`태그를 사용해 외부 자바스크립트 파일을 포함
      
      ```javascript
      // date.js
      function printDate() {
          document.getElementById("date").innerHTML = Date();
      }
      ```
      
      ```html
      <head>
          <meta charset="UTF-8">
          <title>JavaScript Date Test</title>
          <script src="/example/date.js"></script>
      </head>
      ```
    
    - HTML 코드로부터 자바스크립트 코드를 분리할 수 있음
      
      - HTML 코드와 자바스크립트 코드를 각각 읽기도 편해지고, 유지 보수도 쉬워짐
      
      - 웹 브라우저가 미리 읽어 올 수 있어 웹 페이지의 로딩 속도 또한 빨라짐
