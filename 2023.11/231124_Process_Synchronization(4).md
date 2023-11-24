- classical problems of synchronization
  
  - bounded-buffer problem (producer-consumer problem)
  
  - readers and writers problem
  
  - dining-philosophers problem

- bounded-buffer problem (producer-consumer problem)
  
  - buffer
    
    - 임시로 데이터를 저장하는 공간
  
  - producer은 shared memory에 empty buffer가 있으면 데이터 추가
    
    - empty buffer가 있는지 확인 (없으면 기다림)
    
    - 공유데이터에 lock 걺
    
    - empty buffer에 데이터 입력 및 buffer 조작
    
    - lock을 풂
    
    - full buffer 하나 증가
  
  - consumer는 shared memory에 데이터가 있는 buffer가 있으면 사용
    
    - full buffer가 있는지 확인 (없으면 기다림)
    
    - 공유데이터에 lock 걺
    
    - full buffer에서 데이터 꺼내고 buffer 조작
    
    - lock 풂
    
    - empty buffer 하나 증가
  
  - shared data
    
    - buffer 자체 및 buffer 조작 변수 (empty/full buffer의 시작 위치)
  
  - synchronization variables
    
    - mutual exclusion
      
      - need binary semaphore
      
      - shared data의 mutual exclusion
    
    - resource count
      
      - need integer semaphore
      
      - 남은 empty/full buffer의 수 표시
  
  - 수도코드
    
    - synchronization variables
      
      ```c
      semaphore full = 0, empty = n, mutex = 1;
      ```
    
    - producer
      
      ```c
      do {
          ...
          produce an item in x
          ...
          P(empty);
          P(mutex);
          ...
          add x to buffer
          ...
          V(mutex);
          V(full);
      } while (1);
      ```
    
    - consumer
      
      ```c
      do {
          P(full);
          P(mutex);
          ...
          remove an item from buffer to y
          ...
          V(mutex);
          V(empty);
          ...
          consume the item in y
          ...
      } while (1);
      ```