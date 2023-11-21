### Process Synchronization

- race condition (경쟁 상태)
  
  - 여러 프로세스가 공유 데이터를 동시에 접근할 때 실행 순서에 따라 값이 달라지는 상황
  
  - 데이터의 최종 연산 결과는 마지막에 그 데이터를 다룬 프로세스에 따라 달라짐
  
  - OS에서 race condition이 발생하는 경우
    
    - kernel 수행 중 인터럽트 발생 시
      
      - 커널모드 running 중 interrupt가 발생하여 인터럽트 처리루틴 수행
      
      - 양쪽 다 커널 코드이므로 kernel address space 공유
      
      - 해결책
        
        - 공유데이터에서 작업이 진행되는 경우 interrupt를 막음
        
        - 이후 interrupt가 진행될 수 있도록
    
    - 프로세스가 system call을 하여 kernal 모드로 수행중인데 context switch가 일어나는 경우
      
      - system call을 하는 동안 kernel address space의 data를 공유할 수 있음
      
      - 해결책
        
        - 커널 모드에서 수행 중일 때는 CPU는 preempt하지 않음
        
        - 커널 모드에서 사용자 모드로 돌아갈 때 preempt
    
    - multiprocessor에서 shared memory 내의 kernel data
      
      - interrupt enable/disable로 해결되지 않음
      
      - 해결책 두 가지
        
        - 한번에 하나의 CPU만 커널에 들어갈 수 있도록 함
        
        - 커널 내부에 있는 각 공유 데이터에 접근할 때마다 그 데이터에 대한 lock / unlock을 하는 방법

- Process Synchronization 문제
  
  - **공유 데이터의 동시 접근**은 데이터의 불일치 문제를 발생시킬 수 있음
  
  - 일관성 유지를 위해서는 협력 프로세스 (cooperating process) 간 실행 순서를 정해주는 메커니즘 필요
  
  - race condition을 막기 위해서는 concurrent process가 동기화되어야 함

- Critical Section (임계구역) Problem
  
  - n개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우 각 프로세스의 code segment에 존재하는 **공유 데이터를 접근하는 코드**
  
  - 하나의 프로세스가 critical section에 있을 때 다른 모든 프로세스는 critical section에 들어갈 수 없어야 함


