### 배열 (array)

- 배열
  
  - 이름과 인덱스로 참조되는 정렬된 값의 집합
  
  - 특징
    
    - 배열 요소의 타입이 고정되어 있지 않으므로, 같은 배열에 있는 배열 요소끼리의 타입이 서로 다를 수 있음
      
      ```javascript
      const arr = [1, true, "JavaScript"];
      ```
    
    - 배열 요소의 인덱스가 연속적이지 않아도 되며, 따라서 특정 배열 요소가 비어 있을 수도 있음
      
      ```javascript
      const arr = [1, , "JavaScript"];
      console.log(arr);                // [1, empty, 'JavaScript']
      ```
    
    - 자바스크립트에서는 객체로 다뤄짐

- 배열 생성
  
  - 문법
    
    ```javascript
    // 배열 리터럴
    const arr1 = [배열요소1, 배열요소2,...];
    // Array 객체
    const arr2 = Array(배열요소1, 배열요소2,...);
    new 연산자를 이용한 Array 객체
    const arr3 = new Array(배열요소1, 배열요소2,...);
    ```
  
  - 예시
    
    ```javascript
    const arr1 = ["pen", "pencil", "eraser"];
    console.log(arr1);        // ['pen', 'pencil', 'eraser']
    const arr2 = Array("pen", "pencil", "eraser");
    console.log(arr2);        // ['pen', 'pencil', 'eraser']
    const arr3 = new Array("pen", "pencil", "eraser");
    console.log(arr3);        // ['pen', 'pencil', 'eraser']
    ```

- 배열 참조
  
  - 문법
    
    ```javascript
    배열이름[인덱스]
    ```
  
  - 예시
    
    ```javascript
    console.log(arr1[0]);        // pen
    console.log(arr2[2]);        // eraser
    console.log(arr3[1]);        // pencil
    ```

- 배열 요소 추가
  
  - 문법
    
    ```javascript
    arr1.push(추가할 요소);
    arr2[arr2.length] = 추가할 요소;
    arr3[특정인덱스] = 추가할 요소;
    ```
  
  - 예시
    
    ```javascript
    arr1.push('highlighter');
    console.log(arr1);
    // ['pen', 'pencil', 'eraser', 'highlighter']
    arr2[arr2.length] = 'highlighter';
    console.log(arr2);
    // ['pen', 'pencil', 'eraser', 'highlighter']
    arr3[4] = 'highlighter';
    console.log(arr3);
    // ['pen', 'pencil', 'eraser', empty, 'highlighter']
    ```

- 배열 요소 삭제
  
  - 문법
    
    ```javascript
    delete 배열이름[인덱스];
    ```
  
  - 예시
    
    ```javascript
    delete arr3[4];
    console.log(arr3);
    // ['pen', 'pencil', 'eraser', empty, empty]
    console.log(arr3.length);        // 5
    ```

- 배열 순회
  
  - 반복문 이용
  
  - 예시
    
    ```javascript
    let answer = '';
    for (const i of arr1) {
        answer += i + ' ';
    }
    console.log(answer);
    // pen pencil eraser highlighter 
    ```