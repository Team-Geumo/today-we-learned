### 조건문 (conditional statements)

- 프로그램 내에서 주어진 표현식의 결과에 따라 별도의 명령을 수행하도록 제어하는 실행문

- if 문
  
  - 문법
    
    ```javascript
    if (표현식) {
        표현식의 결과가 참일 때 실행할 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    const x = 2, y = 3;
    if (x == y) {
        console.log('같은 값');
    }
    ```

- if / else 문
  
  - 문법
    
    ```javascript
    if (표현식) {
        표현식의 결과가 참일 때 실행할 실행문;
    } else {
        표현식의 결과가 거짓일 때 실행할 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    const x = 2, y = 3;
    if (x == y) {
        console.log('같은 값');
    } else {
        console.log('다른 값');
    }
    ```

- if / else if / else 문
  
  - 문법
    
    ```javascript
    if (표현식1) {
        표현식1의 결과가 참일 때 실행할 실행문;
    } else if (표현식2) {
        표현식2의 결과가 참일 때 실행할 실행문;
    } else {
        표현식1의 결과도 거짓이고, 표현식2의 결과도 거짓일 때 실행할 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    const x = 2, y = 3;
    if (x == y) {
        console.log('x와 y는 같은 값');
    } else if (x > y) {
        console.log('x는 y보다 큰 값');
    } else {
        console.log('x는 y보다 작은 값');
    }
    ```
  
  - 삼항 연산자
    
    `표현식 ? 반환값1 : 반환값2`

- switch 문
  
  - 문법
    
    ```javascript
    switch (조건 값) {
        case 값1:
            조건 값이 값1일 때 실행할 실행문;
            break;
        case 값2:
            조건 값이 값2일 때 실행할 실행문;
            break;
        ...
        default:
            조건 값이 어떠한 case 절에도 해당하지 않을 때 실행할 실행문;
            break;
    }
    ```
    
    - default 절
      
      - 조건 값이 위에 나열된 case 절에 하나도 해당하지 않을 때 실행
      
      - 위치가 반드시 switch 문의 맨 마지막일 필요는 없음
      
      - 무조건 존재해야 하는 것은 아니고, 필요할 때만 선언하여 사용
    
    - case 절 및 default 절은 반드시 `break` 키워드를 포함하고 있어야 함
      
      - `break` 키워드
        
        - 조건 값에 해당하는 case 절이나 default 절이 실행된 뒤 전체 switch 문을 빠져나가게 해주는 키워드
  
  - 예시
    
    ```javascript
    const x = 10;
    switch (typeof x) {
        case "number":
            console.log("숫자");
            break;
        case "string":
            console.log("문자열");
            break;
        case "object":
            console.log("객체");
            break;
        default:
            console.log("모르겠네요...");
            break;
    }
    
    // 숫자
    ```
  
  - break문을 사용하지 않은 경우
    
    ```javascript
    const x = 10;
    switch (typeof x) {
        case "string":
            console.log("문자열");
        case "number":
            console.log("숫자");
        case "object":
            console.log("객체");
        default:
            console.log("모르겠네요...");
    }
    
    // 숫자
    // 객체
    // 모르겠네요...
    ```
    
    - 10의 type은 number이므로 number의 case가 실행됨
    
    - break 키워드가 없으므로 이후 나오는 실행문이 전부 실행됨