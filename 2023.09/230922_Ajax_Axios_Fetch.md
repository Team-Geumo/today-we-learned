### Ajax (Asynchronous JavaScript And XML)

- 개념
  
  - JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 데이터를 주고받는 기술
  
  - 전체 웹페이지를 다시 불러오는 동기 방식과는 다르게 점진적으로 해당 부분의 사용자 인터페이스를 갱신할 수 있음

- 활용
  
  - 순수 Ajax를 사용하는 경우
    
    ```javascript
    function reqListener (event) {
        console.log(event.currentTarget.response);
    }
    
    var oReq = new XMLHttpRequest();
    var serverAddress = "https://~";
    
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", serverAddress);
    oReq.send();
    ```
  
  - Jquery를 통해 Ajax를 사용하는 경우
    
    ```javascript
    var serverAddress = 'https://~';
    
    // jQuery의 .get 메소드 사용
    $.ajax({
        url: ,
        type: 'GET',
        success: function onData (data) {
            console.log(data);
        },
        error: function onError (error) {
            console.error(error);
        }
    });
    ```

### Axios

- 개념
  
  - node.js와 브라우저를 위한 HTTP 통신 라이브러리
  
  - 비동기로 HTTP 통신을 가능하게 해주며 return을 promise 객체로 해주기 때문에 response 데이터를 다루기도 쉬움

- 활용
  
  ```javascript
  axios({
    method: 'post',
    url: '/forum/5',
    data: {
      title: 'music',
      content: 'is my life!'
    }
  });
  ```

- 장점
  
  - promise 기반으로 다루기가 쉬움
  
  - 브라우저 호환성이 뛰어남

- 단점
  
  - 모듈을 설치해야 함

### Fetch

- 개념
  
  - ES6부터 javascript의 내장 라이브러리

- 활용
  
  ```javascript
  const url ='https://~`
  const option ={
     method:'POST',
     header:{
       'Accept':'application/json',
       'Content-Type':'application/json';charset=UTP-8'
    },
    body:JSON.stringify({
    	title: 'music',
      content: 'is my life!'
    })
  
    fetch(url,options)
    	.then(response => console.log(response))
  ```

- 장점
  
  - 별도의 import 과정이 필요하지 않음
  
  - promise 기반으로 다루기가 쉬움
  
  - 사용하는 프레임워크가 안정적이지 않은 때 유용

- 단점
  
  - 브라우저 호환성이 상대적으로 떨어짐