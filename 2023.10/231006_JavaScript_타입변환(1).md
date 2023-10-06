### 타입 변환

- 묵시적 타입 변환 (implicit type conversion)
  
  ```javascript
  10 + "문자열"; // 10문자
  "4" * "3";    // 12
  8 - "문자열";  // NaN
  ```
  
  - NaN (Not a Number)
    
    - 정의되지 않은 값이나 표현할 수 없는 값

- 명시적 타입 변환 (explicit type conversion)
  
  - Number(), String(), Boolean(), Object() 등

- 숫자를 문자열로 변환
  
  - toExponential()
    
    ```javascript
    3.33.toExponential(0);    // 3e+0
    3.33.toExponential(1);    // 3.3e+0
    3.33.toExponential(2);    // 3.33e+0
    3.33.toExponential(6);    // 3.330000e+0
    ```
    
    - 정수 부분은 1자리, 소수 부분은 입력받은 수만큼 e 표기법을 사용하여 숫자를 문자열로 변환
  
  - toFixed()
    
    ```javascript
    3.33.toFixed(0);            // 3
    3.73.toFixed(0);            // 4
    3.73.toFixed(3);            // 3.730
    typeof(3.73.toFixed(3));    // string
    ```
    
    - 소수 부분을 입력받은 수만큼 사용하여 숫자를 문자열로 변환
  
  - toPrecision()
    
    ```javascript
    3.33.toPrecision();            // 3.33
    typeof(3.33.toPrecision());    // string
    3.33.toPrecision(1);           // 3
    3.73.toPrecision(1);           // 4
    3.73.toPrecision(2);           // 3.7
    3.73.toPrecision(3);           // 3.73
    ```
    
    - 입력받은 수만큼 유효 자릿수를 사용하여 숫자를 문자열로 변환

- 문자열을 숫자로 변환
  
  - parseInt(string, radix)
    
    ```javascript
    parseInt("50");        // 50
    parseInt("50", 2);     // NaN
    parseInt("50", 4);     // NaN
    parseInt("50", 6);     // 30
    parseInt("50", 16);    // 80
    ```
    
    - 문자열을 파싱하여 특정 진법의 정수를 반환
  
  - parseFloat()
    
    ```javascript
    parseFloat("1");        // 1
    parseFloat("1.23");     // 1.23
    parseFloat("1 2 3");    // 1
    parseFloat("  1");      // 1
    parseFloat("  1a");     // 1
    parseFloat("  a1");     // NaN
    ```
    
    - 문자열을 파싱하여 부동 소수점 수를 반환