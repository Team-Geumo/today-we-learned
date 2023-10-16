### 매개변수 (parameter)와 인수 (argument)

- 매개변수
  
  - 함수의 정의에서 전달받은 인수를 함수 내부로 전달하기 위해 사용하는 변수

- 인수
  
  - 함수가 호출될 때 함수로 값을 전달해주는 값

- 예시
  
  - 3개의 매개변수를 가지는 함수
    
    ```javascript
    function addNum(x, y, z) {
        return x + y + z;
    }
    
    console.log(addNum(1, 2, 3)); //  6
    // 전달되지 않은 나머지 값이 자동으로 undefined 값으로 설정되어
    // 산술 연산을 수행할 수 없음
    console.log(addNum(1, 2));    //  NaN
    console.log(addNum(1));       //  NaN
    console.log(addNum());        //  NaN
    ```
  
  - 인수가 3개 미만인 경우에도 계산하는 방법
    
    ```javascript
    function addNum(x, y, z) {
        if(x === undefined)
            x = 0;
        if(y === undefined)
            y = 0;
        if(z === undefined)
            z = 0;
        return x + y + z;
    }
    
    console.log(addNum(1, 2, 3)); //  6
    console.log(addNum(1, 2));    //  3
    console.log(addNum(1));       //  1
    console.log(addNum());        //  0
    ```
  
  - 전달받는 인수의 개수에 상관없이 언제나 정상적인 계산을 수행하는 방법
    
    ```javascript
    function addNum() {
        var sum = 0;
        for(var i = 0; i < arguments.length; i++) {
            sum += arguments[i];
        }
        return sum;
    }
    
    console.log(addNum(1, 2, 3));                         // 6
    console.log(addNum(1, 2));                            // 3
    console.log(addNum(1));                               // 1
    console.log(addNum());                                // 0
    console.log(addNum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));   // 55
    ```
    
    - arguments 객체
      
      - 함수가 호출될 때 전달된 인수를 배열의 형태로 저장
      
      - 숫자로 된 인덱스와 length 프로퍼티를 가지고 있지만 모든 것을 배열처럼 다룰 수는 없음

- 디폴트 매개변수 (default parameter)
  
  - 함수를 호출할 때 명시된 인수를 전달하지 않았을 경우에 사용하게 될 기본값
  
  - ECMAScript 6부터 새롭게 정의됨
  
  - 예시
    
    ```javascript
    function addNum(x, y, z = 2) {
        return x + y + z;
    }
    
    console.log(addNum(2, 5, 8));        // 15
    console.log(addNum(2, 5));           // 9
    console.log(addNum(2));              // NaN
    console.log(addNum(2, 5, 8, 6));     // 15
    ```

- 나머지 매개변수 (rest parameter)
  
  - 생략 접두사(...)를 사용하여 특정 위치의 인수부터 마지막 인수까지를 한 번에 지정
  
  - ECMAScript 6부터 새롭게 정의됨
  
  - 예시
    
    ```javascript
    function addNum(num1, ...restArgs) {
        for(var i = 0; i < restArgs.length; i++) {
            num1 += restArgs[i];
        }
        return num1;
    }
    
    console.log(addNum(1, 2, 3));                         // 6
    console.log(addNum(1, 2));                            // 3
    console.log(addNum(1));                               // 1
    console.log(addNum());                                // undefined
    console.log(addNum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));   // 55
    ```