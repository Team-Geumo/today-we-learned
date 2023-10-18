### 정규표현식 (regular expression)

- 정의
  
  - 문자열에서 특정한 규칙을 가지는 문자열의 집합을 찾아내기 위한 검색 패턴

- 생성
  
  - 정규 표현식 리터럴을 이용한 생성
    
    - 문법
      
      ```javascript
      /검색패턴/플래그
      ```
      
      - 플래그 (flag)
        
        - 기본 검색 설정을 하는 방법
        
        - 디폴트는 대소문자 구분
        
        - `i`
          
          - 검색 패턴을 비교할 때 대소문자를 구분하지 않도록 설정
        
        - `g`
          
          - 검색 패턴을 비교할 때 일치하는 모든 부분을 선택하도록 설정
        
        - `m`
          
          - 검색 패턴을 비교할 때 여러 줄의 입력 문자열을 그 상태 그대로 여러 줄로 비교하도록 설정
        
        - `y`
          
          - 대상 문자열의 현재 위치부터 비교를 시작하도록 설정
        
        - 예시
          
          ```javascript
          const targetStr = "abcABCbaCAB";
          
          const strReg1 = /CD/;
          console.log(targetStr.search(strReg1));     // -1
          
          const strReg2 = /AB/;
          console.log(targetStr.search(strReg2));     // 3
          
          const strRegi = /AB/i;
          console.log(targetStr.search(strRegi));    // 0
          
          const strRegg = /AB/g;
          console.log(targetStr.search(strRegg));    // 3
          console.log(targetStr.match(strRegg));     // ['AB', 'AB']
          
          const strRegig = /AB/ig;
          console.log(targetStr.search(strRegig));   // 0
          console.log(targetStr.match(strRegig));    // ['ab', 'AB', 'AB']
          ```
          
          - search() 메서드
            
            - 해당 문자열에서 인수로 전달받은 정규 표현식과 일치하는 첫 번째 문자열의 위치를 반환
            
            - 일치하는 부분 문자열이 없다면 -1 반환
    
    - 예시
      
      ```javascript
      const regStr = /ad-bc/;
      console.log(regStr);        // /ad-bc/
      ```