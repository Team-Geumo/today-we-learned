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
    
    - 괄호 (bracket)
      
      - `()`
        
        - `a(b)c`
          
          - 전체 패턴을 검색한 후 괄호 안에 명시된 문자열을 저장
          
          - 위의 경우 abc를 검색한 후 b를 저장
      
      - `[]`
        
        - `[ab]`
          
          - 대괄호 안의 문자 검색
          
          - 위의 경우 ab 검색
        
        - `[1-2]`
          
          - 대괄호 안의 숫자 검색
          
          - 위의 경우 1에서 2 숫자 검색
        
        - `[\b]`
          
          - 백스페이스 문자 검색
      
      - `{}`
        
        - `{n}`
          
          - 앞의 문자가 정확히 n번 나타나는 경우를 검색
        
        - `{m, n}`
          
          - 앞의 문자가 최소 m번 이상 최대 n번 이하로 나타나는 경우를 검색
    
    - 위치 문자
      
      - `^a`
        
        - 단어의 맨 앞에 위치한 해당 패턴만을 검색
        
        - 예시
          
          ```javascript
          const regStr1 = "banana";
          const regStr2 = "Banana";
          
          const strRegb = /^b/;
          console.log(regStr1.match(strRegb));
          // ['b', index: 0, input: 'banana', groups: undefined]
          console.log(regStr2.match(strRegb));
          // null
          
          const strRegB = /^B/;
          console.log(regStr1.match(strRegB));
          // null
          console.log(regStr2.match(strRegB));
          // ['B', index: 0, input: 'Banana', groups: undefined]
          ```
      
      - `a$`
        
        - 단어의 맨 뒤에 위치한 해당 패턴만을 검색
        
        - 예시
          
          ```javascript
          const regStr1 = "bananA";
          const regStr2 = "Banana";
          
          const strRega = /a$/;
          console.log(regStr1.match(strRega));
          // null
          console.log(regStr2.match(strRega));
          // ['a', index: 5, input: 'Banana', groups: undefined]
          
          const strRegA = /A$/;
          console.log(regStr1.match(strRegA));
          // ['A', index: 5, input: 'bananA', groups: undefined]
          console.log(regStr2.match(strRegA));
          // null
          ```