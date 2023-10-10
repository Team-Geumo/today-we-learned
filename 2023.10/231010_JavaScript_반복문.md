### 반복문 (iteration statements)

- 프로그램 내에서 똑같은 명령을 일정 횟수만큼 반복하여 수행하도록 제어하는 실행문

- while 문
  
  - 특정 조건을 만족할 때까지 계속해서 주어진 실행문 반복 실행
  
  - 문법
    
    ```javascript
    while (표현식) {
        표현식의 결과가 참인 동안 반복적으로 실행하고자 하는 실행문;
    }
    ```
  
  - 예제
    
    ```javascript
    var i = 3;
    while (i < 7) {
        console.log(i);
        i++;
    }
    
    // 3
    // 4
    // 5
    // 6
    ```

- do / while 문
  
  - 표현식의 결과와 상관없이 무조건 한 번은 루프 실행
  
  - 문법
    
    ```javascript
    do {
        표현식의 결과가 참인 동안 반복적으로 실행하고자 하는 실행문;
    } while (표현식);
    ```
  
  - 예제
    
    ```javascript
    var i = 8;
    do {
        console.log(i);
        i++;
    } while (i < 7);
    
    // 8
    ```
    
    ```javascript
    var i = 3;
    do {
        console.log(i);
        i++;
    } while (i < 7);
    
    // 3
    // 4
    // 5
    // 6
    ```

- for 문
  
  - 자체적으로 초기식, 표현식, 증감식을 모두 포함하고 있는 반복문
  
  - 문법
    
    ```javascript
    for (초기식; 표현식; 증감식) {
        표현식의 결과가 참인 동안 반복적으로 실행하고자 하는 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    for (var i = 3; i < 7; i++) {
        console.log(i);
    }
    
    // 3
    // 4
    // 5
    // 6
    ```

- for / in 문
  
  - 해당 객체의 모든 열거할 수 있는 프로퍼티를 순회할 수 있도록 해주는 반복문
  
  - 문법
    
    ```javascript
    for (변수 in 객체) {
        객체의 모든 열거할 수 있는 프로퍼티의 개수만큼 반복적으로 실행하고자 하는 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    const fruits = { a: 'apple', b: 'banana' }
    
    for (const key in fruits) {
      console.log(key);
      console.log(fruits[key]);
    }
    
    // a
    // apple
    // b
    // banana
    ```
    
    ```javascript
    const arr = [3, 4, 5];
    for (const i in arr) {
        console.log(i);
    }
    console.log('---');
    for (const i in arr) {
        console.log(arr[i]);
    }
    
    // 0
    // 1
    // 2
    // ---
    // 3
    // 4
    // 5
    ```

- for / of 문
  
  - 반복할 수 있는 객체를 순회할 수 있도록 해주는 반복문
    
    - 반복할 수 있는 객체 (iterable objects)
      
      - Array, Map, Set, String 등
  
  - 문법
    
    ```javascript
    for (변수 of 객체) {
        객체의 모든 열거할 수 있는 프로퍼티의 개수만큼 반복적으로 실행하고자 하는 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    const arr = [3, 4, 5];
    for (const i of arr) {
        console.log(i);
    }
    
    // 3
    // 4
    // 5
    ```
    
    ```javascript
    const arr = new Set([1, 3, 2, 2, 1, 3, 3, 4]);
    for (const i of arr) {
        console.log(i);
    }
    
    // 1
    // 3
    // 2
    // 4
    ```

- forEach 문
  
  - 배개변수와 함께 콜백 함수를 전달하는 반복문
  
  - 문법
    
    ```javascript
    객체.forEach(callback(element[, index[, array]])) 
    ```
  
  - 예시
    
    ```javascript
    const numbers = [1, 2, 3, 4, 5];
    numbers.forEach(function(number) {
        console.log(number);
    });
    
    // 1
    // 2
    // 3
    // 4
    // 5
    
    numbers.forEach(number => console.log(number));
    
    // 1
    // 2
    // 3
    // 4
    // 5
    
    numbers.forEach((number, index) => {
        console.log(index, number);
    });
    
    // 0 1
    // 1 2
    // 2 3
    // 3 4
    // 4 5
    
    numbers.forEach((number, index, array) => {
        console.log(array);
    });
    
    // [1, 2, 3, 4, 5]
    // [1, 2, 3, 4, 5]
    // [1, 2, 3, 4, 5]
    // [1, 2, 3, 4, 5]
    // [1, 2, 3, 4, 5]
    ```