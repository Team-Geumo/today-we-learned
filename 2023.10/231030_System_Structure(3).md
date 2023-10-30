- Computer
  
  - DMA (Direct Memory Access)
    
    - 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
    
    - cpu의 중재 없이 device controller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송
    
    - 바이트 단위가 아니라 block 단위로 인터럽트를 발생시킴

- 동기식 입출력과 비동기식 입출력
  
  - 동기식 입출력 (synchronous I/O)
    
    - I/O 요청 후 입출력 작업이 완료된 후에 제어가 사용자 프로그램에 넘어감
      
      - I/O는 커널을 통해서만 가능
    
    - 구현 1
      
      - I/O가 끝날 때까지 cpu 낭비
      
      - 매 시점 하나의 I/O만 일어날 수 있음
    
    - 구현 2
      
      - I/O가 완료될 때까지 해당 프로그램에게서 cpu를 빼앗음
      
      - I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
      
      - 다른 프로그램에 cpu를 줌
        
        - 여러 I/O장치를 사용할 수 있음
    
    - I/O의 완료는 인터럽트로 알려줌
  
  - 비동기식 입출력 (asynchronous I/O)
    
    - I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감
    
    - I/O의 완료는 인터럽트로 알려줌

- 입출력 명령을 하는 방법
  
  - I/O를 수행하는 special instruction에 의해
    
    - 일반적인 방법
    
    - memory에 접근하는 instruction과 I/O를 위한 special instruction이 따로 있음
  
  - Memory Mapped I/O에 의해
    
    - I/O 장치도 메모리 주소의 연장 주소를 주어 메모리 주소를 통해 명령하는 방법