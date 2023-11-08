- CPU 스케줄링의 필요성
  
  - 프로그램은 CPU burst와 I/O burst의 연속
    
    - CPU burst
      
      - CPU를 사용하는 과정
        
        - load store, add store, read from file 등의 작업
    
    - I/O burst
      
      - I/O를 사용하는 과정
        
        - wait for I/O
  
  - 프로세스의 특성 분류
    
    - I/O bound process
      
      - I/O busrt가 중간중간 있어 CPU burst 지속시간이 짧은 프로세스
      
      - CPU burst가 짧은 잦음
    
    - CPU bound process
      
      - CPU burst 지속시간이 긴 프로세스
      
      - 계산 위주의 job
  
  - 컴퓨터 안에는 CPU bound job과 I/O bound job이 섞여있기 때문에 CPU 스케줄링이 필요함
    
    - I/O bound job은 상호작용이 필요한 job인데 CPU bound job이 CPU를 사용하고 있으면 I/O bound job이 너무 오래 기다려야 함
    
    - 효율성이 중요하기 때문에 I/O bound job에 우선권을 주어 빠르게 상호작용할 수 있도록 하기 위함

- CPU Scheduler & Dispatcher
  
  - 운영체제의 특정 기능
  
  - CPU Scheduler
    
    - Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고름
  
  - Dispatcher
    
    - CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘김
      
      - context switch

- CPU 스케줄링이 필요한 경우
  
  - 프로세스가 running에서 blocked된 경우
    
    - I/O를 요청하는 시스템 콜 등
    
    - **nonpreemptive** (비선점형)
      
      - 강제로 빼앗지 않고 자진으로 반납
  
  - 프로세스가 running에서 ready된 경우
    
    - 할당 시간 만료로 인해 timer interrupt가 발생한 경우
    
    - **preemptive** (선점형)
      
      - 강제로 빼앗음
  
  - 프로세스가 blocked에서 ready된 경우
    
    - I/O 완료 후 interrupt
    
    - preemptive (선점형)
  
  - 프로세스가 terminate된 경우
    
    - nonpreemptive (비선점형)
