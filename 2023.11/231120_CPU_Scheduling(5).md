### 특이한 케이스에서의 CPU 스케줄링

- Multiple-Processor Scheduling
  
  - CPU가 여러 개인 경우 스케줄링은 더욱 복잡해짐
  
  - Homogeneous processor인 경우
    
    - 큐에 한 줄로 세워서 각 프로세서가 알아서 꺼내갈 수 있음
    
    - 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우 문제가 더 복잡해짐
  
  - Load sharing
    
    - 일부 프로세서에 일이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
    
    - 별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법
  
  - Symmetric Multiprocessing (SMP)
    
    - 각 프로세서가 각자 알아서 스케줄링 결정
  
  - Asymmetric Multiprocessing
    
    - 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

- Real-Time Scheduling
  
  - Hard real-time systems
    
    - 정해진 시간 안에 반드시 끝내도록 스케줄링 해야 함
  
  - Soft real-time computing
    
    - 일반 프로세스에 비해 높은 우선순위를 갖도록 해야 함

- Thread Scheduling
  
  - Local Scheduling
    
    - User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정
  
  - Global Scheduling
    
    - Kernel level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를 스케줄할지 결정

### Algorithm Evaluation

- Queueing models
  
  - 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 performance index 값을 계산

- Implementation & Measurement
  
  - 실제 시스템에 알고리즘을 구현하여 실제 작업에 대한 성능 측정 비교

- Simulation
  
  - 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과 비교