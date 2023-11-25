- classical problems of synchronization
  
  - bounded-buffer problem (producer-consumer problem)
  
  - readers and writers problem
  
  - dining-philosophers problem

- readers and writers problem
  
  - 한 프로세스가 공유데이터 (여기서는 DB)에 write 중일 때 다른 프로세스가 접근하면 안됨
  
  - read는 동시에 여럿이 가능
  
  - 해결 방법
    
    - writer가 DB에 접근 허가를 아직 얻지 못한 상태에서는 모든 대기중인 reader를 다 DB에 접근 가능하도록
    
    - writer는 대기 중인 reader가 하나도 없을 때 DB 접근 허용
    
    - writer가 DB 접근 중이면 reader 접근은 금지
    
    - writer가 DB를 빠져나가야만 reader 접근 허용
  
  - shared data
    
    - DB 자체
    
    - readcount
      
      - 현재 DB에 접근 중인 reader의 수
  
  - synchronization variables
    
    - mutex
      
      - critical section의 mutual exclusion 보장을 위해 사용
    
    - db
  
  - 수도코드
    
    ```c
    # Shared data
    int readcount = 0;
    DB 자체;
    
    # Synchronization variables
    semaphore mutex = 1, db = 1;
    
    # Writer
    P(db);
    ...
    writing DB performed
    ...
    V(db);
    # starvation 가능
    
    # Reader
    P(mutex);                     # readcount lock 설정
    readcount++;
    if (readcount == 1) P(db);    # block writer
    V(mutex);                     # readcount lock 해제
    ...
    reading DB performed
    ...
    P(mutex);                     # readcount lock 설정
    readcount--;
    if (readcount == 0) V(db);    # 마지막 reader인 경우 enable writer
    V(mutex);                     # readcount lock 해제
    ```