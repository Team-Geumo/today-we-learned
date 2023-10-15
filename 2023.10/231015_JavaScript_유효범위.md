### 변수의 유효범위 (variable scope)

- 지역 변수 (local variable)
  
  - 함수 내에 선언된 변수
  
  - 변수가 선언된 함수 내에서만 유효하며 함수가 종료되면 메모리에서 사라짐
  
  - **자바스크립트에서 지역 변수를 선언할 때에는 반드시 var 키워드를 사용하여 선언**해야 함
    
    - 그렇지 않으면 해당 변수는 지역 변수가 아닌 전역 변수로 선언
  
  - 예시
    
    ```javascript
    function test() {
        const var = 10;
        console.log(typeof num);        // number
    }
    test();
    console.log(typeof num);            // undefined
    ```
    
    - 자바스크립트에서는 선언되지 않은 변수를 사용하려고 하거나 접근하려고 하면 오류를 발생시키지만 typeof 연산자의 결괏값은 undefined

- 전역 변수 (global variable)
  
  - 함수의 외부에서 선언된 변수
  
  - 프로그램의 어느 영역에서나 접근할 수 있으며, 웹 페이지가 닫혀야만 메모리에서 사라짐
  
  - 예시
    
    ```javascript
    const num = 10;
    function test() {
        console.log(typeof num);        // number
    }
    test();
    console.log(typeof num);            // number
    ```
    
    ```javascript
    const num = 10;
    function test() {
        const num = 100;
        console.log(num);        // 100
    }
    test();
    console.log(num);            // 10
    ```
    
    ```javascript
    const num = 10;
    function test() {
        const num = 100;
        console.log(num);        // 100
        console.log(window.num); // undefined
    }
    test();
    console.log(num);            // 10
    ```
    
    ```javascript
    var num = 10;
    function test() {
        var num = 100;
        console.log(num);        // 100
        console.log(window.num); // 10
    }
    test();
    console.log(num);            // 10
    ```

### 함수의 유효범위 (variable scope)

- 함수의 유효 범위
  
  ```javascript
  const x = 100, y = 10;
  function sub() {
      return x - y;              // 전역 변수인 x, y에 접근
  }
  console.log(sub());            // 90
  
  function parentFunc() {
      const x = 10, y = 20;
      function add() {
          return x + y;          // 전역 변수가 아닌 지역 변수 x, y에 접근
      }
      return add();
  }
  console.log(parentFunc());     // 30
  ```

- 함수 호이스팅 (hoisting)
  
  - 유효 범위의 적용이 변수가 선언되기 전에도 똑같이 적용되는 것
  
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
    
    ```javascript
    var num = 10;
    function test() {
        console.log(num);        // undefined
        var num = 100;
        console.log(num);        // 100
    }
    test();
    console.log(num);            // 10
    ```