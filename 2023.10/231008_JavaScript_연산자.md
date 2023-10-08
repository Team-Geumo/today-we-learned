### 연산자

- 산술 연산자 (arithmetic operator)
  
  - `+`, `-`, `*`, `/`, `%`
    
    ```javascript
    const x = 3, y = 2;
    x + y;                // 5
    x - y;                // 1
    x * y;                // 6
    x / y;                // 1.5
    x % y;                // 1
    ```

- 대입 연산자 (assignment operator)
  
  - `=`, `+=`, `-=`, `*=`, `/=`, `%=`
    
    ```javascript
    var x = 3;
    x += 2;                // 5
    x -= 3;                // 2
    x *= 8;                // 16
    x /= 4;                // 4
    x %= 3;                // 1
    ```

- 증감 연산자 (increment and decrement operator)
  
  - `++x`, `x++`, `--x`, `x--`
    
    ```javascript
    var x = 8;
    ++x - 4;          // x의 값을 우선 1 증가시킨 후에 4를 뺌
                      // 5
    x;                // 9
    x-- + 3 + --x;    // 9 + 3 + 7
                      // 19
    x;                // 7
    ```

- 비교 연산자 (comparison operator)
  
  - `==`
    
    - 왼쪽 피연산자와 오른쪽 피연산자의 값이 같으면 참을 반환
  
  - `===`
    
    - 왼쪽 피연산자와 오른쪽 피연산자의 값이 같고, 같은 타입이면 참을 반환
  
  - `!=`
    
    - 왼쪽 피연산자와 오른쪽 피연산자의 값이 같지 않으면 참을 반환
  
  - `!==`
    
    - 왼쪽 피연산자와 오른쪽 피연산자의 값이 같지 않거나, 타입이 다르면 참을 반환
  
  - `>`, `>=`, `<`, `<=`

- 논리 연산자 (logical operator)
  
  - `&&`, `||`, `!`

- 비트 연산자 (bitwise operator)
  
  - 비트 단위로 논리 연산 수행
    
    ```javascript
    var x = 11;
    x << 1;        // 22 (11 * 2)
    x >> 1;        // 5 (11 / 2)
    ~x;            // -12 -(11 + 1)
    ```
    
    - `&`
      
      - 대응되는 비트가 모두 1이면 1을 반환
      
      - 비트 AND 연산
    
    - `|`
      
      - 대응되는 비트 중에서 하나라도 1이면 1을 반환
      
      - 비트 OR 연산
    
    - `^`
      
      - 대응되는 비트가 서로 다르면 1을 반환
      
      - 비트 XOR 연산
    
    - `~`
      
      - 비트를 1이면 0으로, 0이면 1로 반전
      
      - 비트 NOT 연산
    
    - `<<`
      
      - 지정한 수만큼 비트를 전부 왼쪽으로 이동
      
      - left shift 연산
    
    - `>>`
      
      - 부호를 유지하면서 지정한 수만큼 비트를 전부 오른쪽으로 이동
      
      - right shift 연산
    
    - `>>>`
      
      - 지정한 수만큼 비트를 전부 오른쪽으로 이동시키며, 새로운 비트는 전부 0

- 기타 연산자
  
  - 삼항 연산자 (ternary operator)
    
    - `표현식 ? 반환값1 : 반환값2`
  
  - typeof 연산자
    
    - 피연산자의 타입 반환
      
      ```javascript
      typeof undefined;    // 'undefined'
      typeof null;         // 'object'
      typeof new Date();   // 'object'
      ```
  
  - instanceof 연산자
    
    - 피연산자인 객체가 특정 객체의 인스턴스인지 아닌지를 확인해줌
    
    - 피연산자가 특정 객체의 인스턴스이면 참을 반환하고, 아니면 거짓을 반환
      
      ```javascript
      var str = new String("문자열");
      
      str instanceof Object;  // true
      str instanceof String;  // true
      str instanceof Array;   // false
      str instanceof Number;  // false
      str instanceof Boolean; // false
      ```
  
  - void 연산자
    
    - 피연산자로 어떤 타입의 값이 오든지 상관없이 `언제나 undefined 값을 반환`