- 프로그램적 해결법의 충족 조건
  
  - 가정
    
    - 모든 프로세스의 수행 속도는 0보다 빠름
    
    - 프로세스 간 상대적인 수행 속도는 가정하지 않음
  
  - Mutual Exclusion (상호 배제)
    
    - 프로세스가 critical section 부분을 수행 중이면 다른 모든 프로세스는 critical section에 들어가면 안됨
  
  - Progress (진행)
    
    - 아무도 critical section에 있지 않은 상태에서 critical section에 들어가고자 하는 프로세스가 있으면 critical section에 들어가게 해주어야 함
  
  - Bounded Waiting (유한 대기)
    
    - 프로세스가 critical section에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스가 critical section에 들어가는 횟수에 한계가 있어야 함

- 프로세스의 일반적인 구조
  
  ```c
  do {
      entry section
      critical section        # 공유하는 부분
      exit section
      remainder section
  } while (1);
  ```
  
  - 알고리즘1
    
    - 프로세스 i는 turn == i인 경우 critical section에 들어갈 수 있음
      
      - 프로세스 0의 경우
        
        ```c
        do {
            while (turn != 0);      # turn 값이 0이 아닌 경우 계속 while문 반복
                                    # turn 값이 0이 되면 아래의 critical section 실행
            critical section        # 공유하는 부분
            turn = 1;               # 프로세스 1이 동작할 수 있도록 turn 값 변경
            remainder section
        } while (1);
        ```
      
      - 프로세스 1의 경우
        
        ```c
        do {
            while (turn != 1);      # turn 값이 1이 아닌 경우 계속 while문 반복
                                    # turn 값이 1이 되면 아래의 critical section 실행
            critical section        # 공유하는 부분
            turn = 0;               # 프로세스 0이 동작할 수 있도록 turn 값 변경
            remainder section
        } while (1);
        ```
    
    - mutual exclusion은 만족하지만 progress는 만족하지 않음
      
      - 과잉양보
        
        - 반드시 한번씩 교대로 들어가야만 함
        
        - 특정 프로세스가 더 빈번히 critical section에 들어가야 하는 경우 문제 발생
        
        - 프로세스 0은 여러번 들어가야 하고 프로세스 1은 한번만 들어가는 경우 프로세스 0은 영원히 들어갈 수 없음
  
  - 알고리즘2
    
    - flag 변수 사용
      
      boolean flag[n];
      
      - 프로세스 i의 경우
        
        ```c
        do {
            flag[i] = true;         # 나 들어갈거야
            while (flag[j]);        # j번째 flag 확인해서 critical section 사용하는지 확인하고 true이면 끝날 때까지 기다림
            critical section
            flag[i] = false;        # 나 나왔어
            remainder section
        } while (1);
        ```
    
    - mutual exclusion은 만족하지만 progress는 만족하지 않음
      
      - 1행 수행 후 CPU를 넘겨준 경우 두 프로세스가 critical section에 들어가지 못하고 끊임없이 양보만 할 수 있음
  
  - 알고리즘3 (Peterson's Algorithm)
    
    - 알고리즘1과 알고리즘2 결합
      
      ```c
      do {
          flag[i] = true;         # 나 들어갈거야
          turn = j
          while (flag[j] && turn == j);
          critical section
          flag[i] = false;        # 나 나왔어
          remainder section
      } while (1);
      ```
      
      - 세 가지 충족 조건을 모두 만족
      
      - busy waiting (=spin lock) 문제 존재
        
        - 계속 CPU와 메모리를 쓰면서 기다리기 때문에 비효율적임
  
  - 하드웨어적으로 문제 해결하기
    
    - Test_and_set(a)
      
      - a를 읽고 a값을 1로 지정하는 명령을 한번에 처리
      
      ```c
      # Synchronization variable:
      boolean lock = false;
      
      # Process Pi
      do {
          while (Test_and_set(lock));
          # lock이 false인 경우 lock을 true(=1)로 바꾼 후 critical section 처리
          critical section
          lock = false;
          remainder section
      }
      ```
