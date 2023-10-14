### 함수

- 함수 (function)
  
  - 하나의 특별한 목적의 작업을 수행하도록 설계된 독립적인 블록

- 자바스크립트에서의 함수
  
  - function 키워드로 시작
  
  - 구성요소
    
    - 함수의 이름
    
    - 매개변수 (parameter)
    
    - 실행문
  
  - 문법
    
    ```javascript
    function 함수이름(매개변수1, 매개변수2,...) {
        함수가 호출되었을 때 실행하고자 하는 실행문;
    }
    ```
  
  - 예시
    
    ```javascript
    function mulNum(x, y) {
        console.log(x * x * y);
    }
    mulNum(3, 7);            // 63
    ```

- return 문
  
  - 함수의 실행을 중단하고 return 키워드 다음에 명시된 표현식의 값을 반환
  
  - 배열이나 객체를 포함한 모든 타입의 값을 반환할 수 있음
  
  - 문법
    
    ```javascript
    function 함수이름(매개변수1, 매개변수2,...) {
        함수가 호출되었을 때 실행하고자 하는 실행문;
        return 반환할 표현식의 값;
    }
    ```
  
  - 예시
    
    ```javascript
    function mulNum(x, y) {
        return (x * y * y);
    }
    const result = mulNum(3, 7);
    console.log(result);            // 147
    ```

- 값으로서의 함수
  
  - 예시
    
    ```javascript
    function sqr(x) {
        return x * x;
    }
    const sqrNum = sqr;        // 변수 sqrNum에 함수 sqr 대입
    console.log(sqr(4));       // 16
    console.log(sqrNum(4));    // 16    // 변수 sqrNum를 함수처럼 호출
    ```