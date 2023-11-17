## Scheduling Algorithms

- FCFS (First-Come First-Service)

- SJF (Shortest-Job-First)

- SRTF (Shortest-Remaining-Time-First)

- Priority Scheduling

- RR (Round Robin)

- Multilevel Queue

- Multilevel Feedback Queue

---

#### FCFS (First-Come First Service)

- 비선점형 스케줄링 (nonpreemptive)

- CPU를 오래 사용하는 프로그램이 CPU를 사용하고 있으면 프로세스가 다 끝날 때까지 기다려야 하기 때문에 비효율적임

- convoy effect (호위효과)
  
  - short process behind long process

### SJF (Shortest-Job-First)

- 각 프로세스의 다음번 CPU burst time을 가지고 스케줄링에 활용

- CPU burst time이 가장 짧은 프로세스를 제일 먼저 스케줄

- 최적의 방법임 (preemptive인 경우)
  
  - 주어진 프로세스에 대해 minimum average waiting time 보장

- 비선점형 스케줄링 (nonpreemptive)
  
  - 일단 CPU를 잡으면 CPU burst가 완료될 때까지 CPU 선점

- 선점형 스케줄링 (preemptive)
  
  - 현재 수행중인 프로세스의 남은 burst time보다 더 짧은 CPU burst time을 가지는 새로운 프로세스가 도착하면 CPU를 빼앗김 **->** SRTF (Shortest-Remaining-Time-First)

- 문제점
  
  - starvation
    
    - CPU 사용시간이 긴 프로세스는 영원히 CPU를 사용하지 못할 수도 있음
  
  - CPU burst time을 미리 알 수 없음
    
    - 추정 (estimate)만 가능
      
      - 과거의 CPU burst time이용해서 추정
        
        - exponential averaging

#### Priority Scheduling (우선순위 스케줄링)

- 우선순위가 가장 높은 프로세스에게 CPU를 할당
  
  - smallest integer == highest priority
  
  - 우선순위를 정의하는 방법은 다양함

- SJF는 priority scheduling에 포함됨

- 비선점형 스케줄링 (nonpreemptive)
  
  - 일단 CPU를 잡으면 CPU burst가 완료될 때까지 CPU 선점

- 선점형 스케줄링 (preemptive)
  
  - 현재 수행중인 프로세스의 우선순위보다 더 높은 우선순위를 가지는 새로운 프로세스가 도착하면 CPU를 빼앗김

- 문제점
  
  - starvation
    
    - CPU 사용시간이 긴 프로세스는 영원히 CPU를 사용하지 못할 수도 있음
    
    - 이를 해결하고자 aging 기법 도입
      
      - 기다리는 시간이 길수록 우선순위를 높여줌