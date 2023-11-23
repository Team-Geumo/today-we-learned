- Semaphores
  
  - 일종의 추상화
  
  - 정수값을 가질 수 있음
    
    - 자원의 갯수 의미
  
  - P 연산과 V 연산 존재
    
    - P 연산
      
      - Semaphore 값 (공유 데이터)을 획득하는 과정
      
      - lock을 거는 과정
        
        ```c
        # P(S):
        
        while (S <= 0) do no-op;    # wait
        S--;
        ```
    
    - V 연산
      
      - Semaphore 값 (공유 데이터)을 반납하는 과정
      
      - lock을 푸는 과정
        
        ```c
        # V(S):
        
        S++;
        ```
  
  - critical section of n processes
    
    ```c
    # Synchronization variable
    semaphore mutex;        # 처음은 1 : 1개가 CS에 들어갈 수 있음
    
    # Process Pi
    do {
        P(mutex);
        critical section
        V(mutex);
        remainder section
    } while (1);
    ```
    
    - busy wait는 효율적이지 못함 (=spin lock)
  
  - block / wakeup implementation
    
    - semaphore 정의
      
      ```c
      typedef struct
      {
          int value;            # semaphore
          struct process *L;    # process wait queue
      } semaphore;
      ```
      
      - P 연산
        
        ```c
        S.value--;
        if (S.value < 0) {    # 자원의 여분이 없음
            add this process to S.L;
            block();
        }
        ```
      
      - V 연산
        
        ```c
        S.value++;
        if (S.value <= 0) {
            remove a process P from S.L;
            wakeup(P);
        }
        ```
    
    - block과 wakeup 가정
      
      - block
        
        - 커널은 block을 호출한 프로세스를 suspend 시킴
        
        - 이 프로세스의 PCB를 semaphore에 대한 wait queue에 넣음
      
      - wakeup(P)
        
        - block된 프로세스 P를 wakeup 시킴
        
        - 이 프로세스의 PCB를 ready queue로 옮김
  
  - busy-wait vs block/wakeup
    
    - critical section의 길이가 긴 경우 block/wakeup이 적당
    
    - critical section의 길이가 매우 짧은 경우 block/wakeup 오버헤드가 busy-wait보다 더 커질 수 있음
    
    - 일반적으로는 block/wakeup 방식이 더 좋음
  
  - Two types of semaphores
    
    - counting semaphores
      
      - 도메인이 0 이상인 임의의 정수값
      
      - 주로 resource counting에 사용
    
    - binary semaphore (mutex)
      
      - 0 또는 1 값만 가질 수 있는 semaphore
      
      - 주로 mutual exclusion (lock/unlock)에 사용