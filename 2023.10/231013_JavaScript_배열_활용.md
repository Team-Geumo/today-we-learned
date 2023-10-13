- 희소 배열
  
  - 배열에 속한 요소의 위치가 연속적이지 않은 배열
  
  - 배열의 length 프로퍼티 값보다 배열 요소의 개수가 언제나 적음
  
  - 예시
    
    ```javascript
    const arr = new Array();
    arr[3] = 'l';
    console.log(arr);
    // [empty, empty, empty, 'l']
    console.log(arr.length);    // 4
    ```

- 다차원 배열
  
  - 1차원 배열
    
    ```javascript
    const arr1 = new Array(3);
    console.log(arr1);
    // [empty, empty, empty]
    ```
  
  - 2차원 배열
    
    ```javascript
    let arr2 = new Array(3);
    for (let row = 0; row < 3; row++) {
        arr2[row] = new Array(2);
        for (let column = 0; column < 2; column++) {
            arr2[row][column] = '[' + row + ',' + column + ']';
        }
    }
    console.log(arr2);
    // ['[0,0]', '[0,1]']
    // ['[1,0]', '[1,1]']
    // ['[2,0]', '[2,1]']
    ```

- 배열 여부 확인
  
  - 자바스크립트 배열은 객체(object) 타입이 되며, typeof 연산자를 사용하면 'object'를 반환
  
  - 배열 여부 확인 방법
    
    - Array.isArray() 메소드
      
      - ECMAScript 5부터 사용 가능
        
        ```javascript
        console.log(Array.isArray(arr2));    // true
        console.log(Array.isArray(2));       // false
        ```
    
    - instanceof 연산자
      
      ```javascript
      console.log(arr2 instanceof Array);    // true
      console.log(2 instanceof Array);       // false
      ```