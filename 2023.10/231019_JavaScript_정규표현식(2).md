### 정규표현식 (regular expression)

- 정의
  
  - 문자열에서 특정한 규칙을 가지는 문자열의 집합을 찾아내기 위한 검색 패턴

- 생성
  
  - 정규 표현식 리터럴을 이용한 생성
    
    - 문법
      
      ```javascript
      /검색패턴/플래그
      ```
    
    - 예시
      
      ```javascript
      const regStr = /ad-bc/;
      console.log(regStr);        // /ad-bc/
      ```
    
    - 특수문자 (special characters)
      
      - 숫자만을 검색하거나, 띄어쓰기를 찾는 등 정확히 일치하는 패턴보다 더 복잡한 조건을 사용할 때 필요
      
      - `\`
        
        - 일반 문자가 나오면 이스케이프 문자로 해석하고, 특수 문자가 나오면 일반 문자로 해석
      
      - `\d`
        
        - 숫자 검색
        
        - `/[0-9]/`와 동일
        
        - 예시
          
          ```javascript
          const targetStr = "a1b2c3d4";
          
          const reg1 = /\d/;        // 0부터 9까지의 숫자 검색
          console.log(targetStr.search(reg1));    // 1
          const reg2 = /[3-7]/;     // 3부터 7까지의 숫자 검색
          console.log(targetStr.search(reg2));    // 5
          ```
      
      - `\D`
        
        - 숫자가 아닌 문자 검색
        
        - `/[^0-9]/`와 동일
      
      - `\w`
        
        - 언더스코어(_)를 포함한 영문자 및 숫자 검색
        
        - `/[A-Za-z0-9_]/`와 동일
      
      - `\W`
        
        - 언더스코어(_), 영문자, 숫자가 아닌 문자를 검색
        
        - `/[^A-Za-z0-9_]/`와 동일
      
      - `\s`
        
        - 띄어쓰기, 탭, 줄 바꿈 문자 등의 공백 문자 검색
        
        - 예시
          
          ```javascript
          const targetStr = "abc 123";
          
          const reg = /\w\s\w/;
          // 공백 문자를 사이에 두는 언더스코어(_)를 포함한 영문자 및 숫자로 이루어진 문자열을 검색함.
          console.log(targetStr.search(reg));    // 2
          console.log(targetStr.match(reg));
          // ['c 1', index: 2, input: 'abc 123', groups: undefined]
          ```
      
      - `\S`
        
        - 띄어쓰기, 탭, 줄 바꿈 문자 등의 공백 문자가 아닌 문자 검색
      
      - `\b`
        
        - 단어의 맨 앞이나 맨 뒤가 패턴과 일치하는지 검색
      
      - `\xhh`
        
        - 16진수 hh에 해당하는 유니코드 문자 검색
      
      - `\uhhhh`
        
        - 16진수 hhhh에 해당하는 유니코드 문자 검색
    
    - 양화사 (quantifier)
      
      - 수량을 나타내는 경우 필요
      
      - `n*`
        
        - 바로 앞의 문자가 0번 이상 나타나는 경우 검색
      
      - `n+`
        
        - 바로 앞의 문자가 1번 이상 나타나는 경우 검색
      
      - `n?`
        
        - 바로 앞의 문자가 0번 또는 1번만 나타나는 경우 검색
      
      - 예시
        
        ```javascript
        const targetStr = "Hello World!";
        
        // 문자 'l' 다음에 문자 'o'가 0번 이상 나타나는 경우 검색
        const zeroReg = /lo*/;
        // 문자 'l' 다음에 문자 'o'가 1번 이상 나타나는 경우 검색
        const oneReg = /lo+/;
        // 문자 'l' 다음에 문자 'o'가 0 또는 1번만 나타나는 경우 검색
        const zeroOneReg = /lo?/;
         
        console.log(targetStr.search(zeroReg));    // 2
        console.log(targetStr.search(oneReg));     // 3
        console.log(targetStr.search(zeroOneReg)); // 2
        ```