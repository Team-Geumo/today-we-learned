### predefined functions (이미 정의된 전역 함수)

- eval()
  
  - 문자열로 표현된 자바스크립트 코드를 실행하는 함수
  
  - 예시
    
    ```javascript
    const x = 1, y = 2;
    const a = eval("x + y");
    console.log(a);                // 3
    const b = eval("2*x + 3*y");
    console.log(b);                // 8
    ```

- isFinite()
  
  - 전달된 값이 유한한 수인지를 검사하여 그 결과를 반환
  
  - 예시
    
    ```javascript
    console.log(isFinite(1));         // true
    console.log(isFinite(1e100));     // true
    console.log(isFinite(0));         // true
    console.log(isFinite(true));      // true
    console.log(isFinite(false));     // true
    console.log(isFinite(null));      // true
    console.log(isFinite("123"));     // true
    console.log(isFinite(""));        // true
    
    console.log(isFinite("문자"));     // false
    console.log(isFinite(undefined)); // false
    console.log(isFinite(NaN));       // false
    ```

- isNaN()
  
  - 전달된 값이 NaN인지를 검사하여 그 결과를 반환
  
  - 예시
    
    ```javascript
    console.log(isNaN(1));         // false
    console.log(isNaN(1e100));     // false
    console.log(isNaN(0));         // false
    console.log(isNaN(true));      // false
    console.log(isNaN(false));     // false
    console.log(isNaN(null));      // false
    console.log(isNaN("123"));     // false
    console.log(isNaN(""));        // false
    
    console.log(isNaN("문자"));     // true
    console.log(isNaN(undefined)); // true
    console.log(isNaN(NaN));       // true
    ```
    
    - 숫자를 강제 변환하여 예상하지 못한 결과를 얻을 수 있음
      
      - Number.isNaN() 사용을 권장
        
        ```javascript
        console.log(Number.isNaN(1));         // false
        console.log(Number.isNaN(1e100));     // false
        console.log(Number.isNaN(0));         // false
        console.log(Number.isNaN(true));      // false
        console.log(Number.isNaN(false));     // false
        console.log(Number.isNaN(null));      // false
        console.log(Number.isNaN("123"));     // false
        console.log(Number.isNaN(""));        // false
        console.log(Number.isNaN("문자"));     // false
        console.log(Number.isNaN(undefined)); // false
        
        console.log(Number.isNaN(NaN));       // true
        ```

- parseFloat()
  
  - 문자열을 파싱하여 부동 소수점 수로 반환
  
  - 예시
    
    ```javascript
    console.log(parseFloat("123"));        // 123
    console.log(parseFloat("123.000"));    // 123
    console.log(parseFloat("123.400"));    // 123.4
    console.log(parseFloat("123.456"));    // 123.456
    console.log(parseFloat("12 34 56"));   // 12
    console.log(parseFloat(" 123 "));      // 123
    console.log(parseFloat("123 문자"));    // 123
    console.log(parseFloat("문자 123"));    // NaN
    ```

- parseInt()
  
  - 문자열을 파싱하여 정수로 반환
  
  - 예시
    
    ```javascript
    console.log(parseInt("123"));        // 123
    console.log(parseInt("123.000"));    // 123
    console.log(parseInt("123.800"));    // 123
    console.log(parseInt("123.456"));    // 123
    console.log(parseInt("12 34 56"));   // 12
    console.log(parseInt(" 123 "));      // 123
    console.log(parseInt("123 문자"));    // 123
    console.log(parseInt("문자 123"));    // NaN
    
    console.log(parseInt("10", 10));     // 10
    console.log(parseInt("10", 8));      // 8
    console.log(parseInt("10", 16));     // 16
    console.log(parseInt("0x10"));       // 16
    ```

- encodeURI()와 encodeURIComponent()
  
  - encodeURI()
    
    - URI에서 주소를 표시하는 특수문자를 제외한 모든 문자를 이스케이스 시퀀스 (escape sequences) 처리하여 부호화
      
      - 이스케이스 시퀀스
        
        - `\a`, `\n`, `\t`, `\\`, `\’`, `\”` 등
  
  - encodeURIComponent()
    
    - URI에서 주소를 표시하는 특수문자를 포함한 모든 문자를 이스케이스 시퀀스 처리하여 부호화
  
  - 예시
    
    ```javascript
    const uri = "https://search.naver.com/search.naver?ie=UTF-8&query=javascript&sm=chr_hty";
    
    const enc1 = encodeURI(uri);
    console.log(enc1);
    // https://search.naver.com/search.naver?ie=UTF-8&query=javascript&sm=chr_hty
    const enc2 = encodeURIComponent(uri);
    console.log(enc2);
    // https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fie%3DUTF-8%26query%3Djavascript%26sm%3Dchr_hty
    ```

- decodeURI()와 decodeURIComponent()
  
  - decodeURI()
    
    - encodeURI() 함수나 다른 방법으로 만들어진 URI를 해독
  
  - decodeURIComponent()
    
    - encodeURIComponent() 함수나 다른 방법으로 만들어진 URI 컴포넌트를 해독
  
  - 예시
    
    ```javascript
    const uri = "https://search.naver.com/search.naver?ie=UTF-8&query=javascript&sm=chr_hty";
    
    const enc1 = encodeURI(uri);
    const dec1 = decodeURI(enc1);
    console.log(dec1);
    // https://search.naver.com/search.naver?ie=UTF-8&query=javascript&sm=chr_hty
    const enc2 = encodeURIComponent(uri);
    const dec2 = decodeURIComponent(enc2);
    console.log(dec2);
    // https://search.naver.com/search.naver?ie=UTF-8&query=javascript&sm=chr_hty
    ```

- escape()와 unescape()
  
  - escape()
    
    - 전달받은 문자열에서 특정 문자들을 16진법 이스케이프 시퀀스 문자로 변환
    
    - 자바스크립트 1.5버전부터는 지원하지 않음
  
  - unescape()
    
    - 전달받은 문자열에서 escape() 함수나 다른 방법으로 만들어진 16진법 이스케이프 시퀀스 문자를 원래의 문자로 변환
    
    - 자바스크립트 1.5버전부터는 지원하지 않음
  
  - 예시
    
    ```javascript
    const str = "문자!@#$%^&";
    
    const esc = escape(str);
    console.log(esc);            // %uBB38%uC790%21@%23%24%25%5E%26
    const une = unescape(esc);
    console.log(une);            // 문자!@#$%^&
    ```

- Number()
  
  -  전달받은 객체의 값을 숫자로 반환
  
  - 예시
    
    ```javascript
    console.log(Number("123"));        // 123
    console.log(Number("123.000"));    // 123
    console.log(Number("123.400"));    // 123.4
    console.log(Number("123.456"));    // 123.456
    console.log(Number("12 34 56"));   // NaN
    console.log(Number(" 123 "));      // 123
    console.log(Number("123 문자"));    // NaN
    console.log(Number("문자 123"));    // NaN
    console.log(Number(true));          // 1
    console.log(Number(false));         // 0
    console.log(Number(new Date()));    // 1697554480959
    console.log(Number(null));          // 0
    ```

- String()
  
  - 전달받은 객체의 값을 문자열로 반환
  
  - 예시
    
    ```javascript
    console.log(String("123"));        // 123
    console.log(String("123.000"));    // 123.000
    console.log(String("123.400"));    // 123.400
    console.log(String("123.456"));    // 123.456
    console.log(String("12 34 56"));   // 12 34 56
    console.log(String(" 123 "));      //  123 
    console.log(String("123 문자"));    // 123 문자
    console.log(String("문자 123"));    // 문자 123
    console.log(String(true));          // true
    console.log(String(false));         // false
    console.log(String(Boolean(1)));    // true
    console.log(String(Boolean(0)));    // false
    console.log(String(new Date()));    // Tue Oct 17 2023 23:55:53 GMT+0900 (한국 표준시)
    console.log(String(null));          // null
    ```