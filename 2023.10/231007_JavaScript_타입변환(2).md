### 타입 변환

- 불리언 값을 문자열로 변환
  
  - String()
    
    ```javascript
    String(true);     // 'true'
    String(false);    // 'false'
    ```
  
  - toString()
    
    ```javascript
    true.toString();     // 'true'
    false.toString();    // 'false'
    ```

- 불리언 값을 숫자로 변환
  
  - Number()
    
    ```javascript
    Number(true);     // 1
    Number(false);    // 0
    ```

- 날짜를 문자열이나 숫자로 변환
  
  - String() 함수나 toString() 메소드 사용
    
    ```javascript
    String(Date());
    // 'Sat Oct 07 2023 23:28:51 GMT+0900 (한국 표준시)'
    Date().toString();
    // 'Sat Oct 07 2023 23:29:23 GMT+0900 (한국 표준시)'
    ```
  
  - 날짜 객체
    
    ```javascript
    var date = new Date();
    date.getDate();            // 7
    date.getDay();             // 6
    date.getFullYear();        // 2023
    date.getMonth();           // 9
    date.getTime();            // 1696689008911
    date.getHours();           // 23
    date.getMinutes();         // 30
    date.getSeconds();         // 8
    date.getMilliseconds();    // 911
    ```
    
    - getDate()
      
      - 날짜 중 일자를 숫자로 반환
    
    - getDay()
      
      - 날짜 중 요일을 숫자로 반환
        
        - 일요일 : 0, 토요일 : 6
    
    - getFullYear()
      
      - 날짜 중 연도를 4자리 숫자로 반환
    
    - getMonth()
      
      - 날짜 중 월을 숫자로 반환
    
    - getTime()
      
      - 1970년 1월 1일부터 현재까지의 시간을 밀리초(millisecond) 단위의 숫자로 반환
    
    - getHours()
      
      - 시간 중 시를 숫자로 반환
    
    - getMinutes()
      
      - 시간 중 분을 숫자로 반환
    
    - getSeconds()
      
      - 시간 중 초를 숫자로 반환
    
    - getMilliseconds()
      
      - 시간 중 초를 밀리초(millisecond) 단위의 숫자로 반환
      
      - 0 ~ 999