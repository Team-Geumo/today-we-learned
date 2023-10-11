### 제어문 (control flow statements)

- 프로그램의 순차적인 흐름을 제어해야 할 때 사용하는 실행문

- [조건문](./231009_JavaScript_조건문.md)

- [반복문](./231010_JavaScript_반복문.md)

- 기타 제어문
  
  - label 문
    
    - 프로그램 내의 특정 영역을 식별할 수 있도록 해주는 식별자
    
    - continue 문과 break 문의 동작이 프로그램의 흐름을 턱정 영역으로 이동시킬 수 있음
    
    - 문법
      
      ```javascript
      label:
          식별하고자 하는 특정 영역
      ```
    
    - 예시
      
      ```javascript
      let i, j;
      
      loop1:
      for (i = 0; i < 3; i++) {
          console.log(i);
          loop2:
          for (j = 0; j < 2; j++) {
              if (i === 1 && j === 1) {
                  continue loop1;
              }
              console.log(i, j);
          }
          console.log('---');
      }
      
      // 0
      // 0 0
      // 0 1
      // ---
      // 1
      // 1 0
      // 2
      // 2 0
      // 2 1
      // ---
      ```
      
      ```javascript
      let i, j;
      
      loop1:
      for (i = 0; i < 3; i++) {
          console.log(i);
          loop2:
          for (j = 0; j < 2; j++) {
              if (i === 1 && j === 1) {
                  break loop1;
              }
              console.log(i, j);
          }
          console.log('---');
      }
      
      // 0
      // 0 0
      // 0 1
      // ---
      // 1
      // 1 0
      ```
  
  - continue 문
    
    - 루프 내에서 사용하여 해당 루프의 나머지 부분을 건너뛰고, 바로 다음 표현식의 판단으로 넘어가게 함
    
    - 보통 특정 조건에 대한 처리를 제외하고자 할 때 사용
    
    - 문법
      
      ```javascript
      continue;
      continue 라벨이름;
      ```
    
    - 예시
      
      ```javascript
      const num = 2;
      for (var i = 0; i <= 10; i++) {
          if (i % num == 0)
              continue;
          console.log(i);
      }
      
      // 1
      // 3
      // 5
      // 7
      // 9
      ```
  
  - break 문
    
    - 루프 내에서 해당 반복문을 종료시키고 다음 실행문으로 프로그램의 흐름을 이동시킴
    
    - 문법
      
      ```javascript
      break;
      break 라벨이름;
      ```
    
    - 예시
      
      ```javascript
      const num = 2;
      for (var i = 1; i <= 10; i++) {
          if (i % num == 0) {
              console.log(i);
              break;
          }
      }
      
      // 2
      ```