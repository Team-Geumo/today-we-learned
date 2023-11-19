## Scheduling Algorithms

- FCFS (First-Come First-Service)

- SJF (Shortest-Job-First)

- SRTF (Shortest-Remaining-Time-First)

- Priority Scheduling

- RR (Round Robin)

- Multilevel Queue

- Multilevel Feedback Queue

---

### RR (Round Robin)

- 현대적인 컴퓨터 시스템에서 사용하는 CPU 스케줄링은 RR에 기반하고 있음

- 각 프로세스는 동일한 크기의 할당 시간 (time quantum)을 가짐
  
  - 일반적으로 10-100 milliseconds

- 할당 시간이 지나면 프로세스는 선점 (preempted) 당하고 ready queue의 제일 뒤에 가서 줄 섬

- n개의 프로세스가 ready queue에 있고 할당 시간이 q time unit인 경우 각 프로세스는 최대 q time unit 단위로 CPU 시간의 1/n을 얻음
  
  - 어떤 프로세스도 (n-1)q time unit 이상 기다리지 않음

- 대기 시간이 각 프로세스의 CPU 사용시간에 비례
  
  - CPU를 길게 쓰는 프로세스는 기다리는 시간도 길어지고 CPU를 짧게 쓰는 프로세스는 기다리는 시간이 짧아짐

- 응답 시간이 빠르다는 장점

- q값에 따른 수행
  
  - q가 큰 경우
    
    - FCFS와 같음
  
  - q가 작은 경우
    
    - context switch가 빈번하게 발생하여 오버헤드가 커짐

- 일반적으로 SJF보다 average turnaround time이 길지만 response time은 더 짧음

### Multilevel Queue

- Ready queue를 여러 개로 분할
  
  - foreground (interactive)
  
  - background (batch - no human interaction)

- 각 큐는 독립적인 스케줄링 알고리즘을 가짐
  
  - foreground - RR
    
    - interactive 하기 때문
  
  - background - FCFS
    
    - CPU를 계속 사용하는 작업이 많기 때문

- 큐에 대한 스케줄링 필요
  
  - Fixed priority scheduling
    
    - foreground를 우선으로 처리하고 background 수행
    
    - starvation 있을 수도 있음
  
  - Time slice
    
    - 각 큐에 CPU time을 적절한 비율로 할당

### Multilevel Feedback Queue

- 프로세스가 다른 큐로 이동 가능

- aging을 이와 같은 방식으로 구현할 수 있음

- 파라미터
  
  - Queue의 수
  
  - 각 큐의 scheduling 알고리즘
  
  - 프로세스를 상위 큐로 보내는 기준
  
  - 프로세스를 하위 큐로 내쫓는 기준
  
  - 프로세스가 CPU 서비스를 받으려 할 때 들어갈 큐를 결정하는 기준