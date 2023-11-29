- deadlock의 처리 방법
  
  - deadlock이 생기지 않도록 미연에 방지하는 방법
    
    - deadlock prevention
      
      - 자원 할당 시 deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 하는 것
    
    - deadlock avoidance
      
      - 자원 요청에 대한 부가적인 정보를 이용해서 deadlock의 가능성이 없는 경우에만 자원 할당
      
      - 시스템 state가 원래 state로 돌아올 수 있는 경우에만 자원 할당
  
  - deadlock이 생기도록 놓아두는 방법
    
    - deadlock detection and recovery
      
      - deadlock 발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견 시  recover
    
    - deadlock ignorance
      
      - deadlock을 시스템이 책임지지 않음
      
      - UNIX를 포함한 대부분의 OS가 채택하는 방법

- deadlock prevention
  
  - 자원 할당 시 deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 하는 것
  
  - mutual exclusion
    
    - 공유해서는 안되는 자원의 경우 반드시 성립해야 함
  
  - hold and wait
    
    - 프로세스가 자원을 요청할 때 다른 어떤 자원도 가지고 있지 않아야 함
    
    - 방법1
      
      - **프로세스 시작 시** 모든 필요한 자원을 할당받게 하는 방법
      
      - 비효율적
    
    - 방법2
      
      - **자원이 필요할 경우** 보유 자원을 모두 놓고 다시 요청
  
  - no preemption
    
    - process가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨
    
    - 모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작됨
    
    - state를 쉽게 save하고 restore할 수 있는 자원에서 주로 사용 (CPU, memory)
  
  - circular wait
    
    - 모든 자원 유형에 할당 순서를 정하여 정해진 순서대로만 자원 할당
  
  - utilization 저하, throughput 감소, starvation 문제