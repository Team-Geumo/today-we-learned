- Monitor
  
  - semaphore의 문제점
    
    - 코딩 어려움
    
    - 정확성 입증 어려움
    
    - 자발적 협력 필요
    
    - 한 번의 실수가 모든 시스템에 치명적 영향
  
  - monitor
    
    - 동시 수행중인 프로세스 사이에서 abstract data type의 안전한 공유를 보장하기 위한 high-level synchronization construct
      
      - semaphore에서의 lock이 필요하지 않음
        
        ```c
        monitor monitor-name
        {
            shared variable declarations
            procedure body P1(...) {
                ...
            }
            procedure body P2(...) {
                ...
            }
            ...
            procedure body Pn(...) {
                ...
            }
            {
                initialization code
            }
        }
        ```
    
    - 모니터 내에서는 한 번에 하나의 프로세스만 활동 가능
    
    - 프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요 없음
    
    - 프로세스가 monitor 안에서 기다릴 수 있도록 하기 위해 condition variable 사용
      
      - condition variable은 **wait**와 **signal** 연산에 의해서만 접근 가능
      
      - x.wait();
        
        - x.wait()을 invoke한 프로세스는 다른 프로세스가 x.signal()을 invoke하기 전까지 suspend됨
      
      - x.signal();
        
        - 정확하게 하나의 suspend된 프로세스를 resume
        
        - suspend된 프로세스가 없으면 아무 일도 일어나지 않음
  
  - bounded-buffer problem
    
    ```c
    monitor bounded_buffer
    {
        int buffer[N];
        # condition variable은 값을 가지지 않고 자신의 큐에 프로세스를 매달아서 sleep시키거나 큐에서 프로세스를 깨우는 역할만 함
        condition full, empty;
    
        void produce(int x) {
            if there is no empty buffer
                empty.wait();
            add x to an empty buffer
            full.signal();
        }
    
        void consume(int *x) {
            if there is no full buffer
                full.wait();
            remove an item from buffer and store it to *x
            empty.signal();
        }
    }
    ```
  
  - dining philosophers example
    
    ```c
    monitor dining_philosopher
    {
        enum {thinking, hungry, eating} state[5];
        condition self[5];
    
        void pickup(int i) {
            state[i] = hungry;
            test(i);
            if (state[i] != eating) {
                self[i].wait();
            }
        }
    
        void putdown(int i) {
            state[i] = thinking;
            test((i+4) % 5);
            test((i+1) % 5);
        }
    
        void test(int i) {
            if ((state[(i+4) % 5] != eating) && (state[i] == hungry) && (state[(i+1) % 5] != eating)) {
                state[i] = eating;
                self[i].signal();
            }
        }
    
        void init() {
            for (int i = 0; i < 5, i++) {
                state[i] = thinking;
            }
        }
    }
    
    Philosopher(i):
    {
        pickup(i);
        eat();
        putdown(i);
        think();
    } while(1)
    ```