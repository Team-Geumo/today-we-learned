- classical problems of synchronization
  
  - bounded-buffer problem (producer-consumer problem)
  
  - readers and writers problem
  
  - dining-philosophers problem

- dining-philosophers problem
  
  - 수도코드
    
    ```c
    # Synchronization variables
    semaphore chopstick[5];        # initially all values are 1
                                   # [1, 1, 1, 1, 1]
    
    # Philosopher i
    do {
        P(chopstick[i]);
        P(chopstick[(i+1) % 5]);
        ...
        eat();
        ...
        V(chopstick[i]);
        V(chopstick[(i+1) % 5]);
        ...
        think();
        ...
    } while(1);
    ```
    
    - deadlock 가능성 있음
      
      - deadlock
        
        - 둘 이상의 프로세스가 서로 상대방에 의해 충족될 수 있는 이벤트를 무한히 기다리는 현상
      
      - 모든 철학자가 동시에 왼쪽 젓가락을 집은 경우
    
    - 해결 방안
      
      - 4명의 철학자만 동시에 앉을 수 있도록
      
      - 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있도록
        
        ```c
        enum {thinking, hungry, eating} state[5];
        # 젓가락 권한 (1이면 권한 있음, 0이면 없음)
        semaphore self[5] = 0;
        semaphore mutex = 1;
        
        # test
        void test(int i) {
            if (state[(i+4) % 5] != eating && state[i] == hungry && state[(i+1) % 5] != eating) {
                state[i] = eating;
                V(self[i]);
            }
        }
        
        # pickup
        void pickup(int i) {
            P(mutex);
            state[i] = hungry;
            test(i);
            V(mutex);
            P(self[i]);
        }
        
        # putdown
        void putdown(int i) {
            P(mutex);
            state[i] = thinking;
            test((i+4) % 5);
            test((i+1) % 5);
            V(mutex);
        }
        
        # Philosopher i
        do {
            pickup(i);
            eat();
            putdown(i);
            think();
        } while(1);
        ```
      
      - 짝수 철학자는 왼쪽 젓가락부터 집도록하고 홀수 철학자는 오른쪽 젓가락부터 집도록