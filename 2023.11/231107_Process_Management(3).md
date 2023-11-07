- 프로세스와 관련한 시스템 콜
  
  - wait()
    
    - sleep until child is done
    
    - 프로세스 A가 wait() 시스템 콜을 호출하면 커널은 자식이 종료될 때까지 프로세스 A를 block 상태로 재우고 자식 프로세스가 종료되면 ready 상태로 깨움
    
    - 프로세스 수행 시 자식이 종료될 때까지 부모가 기다리는 모델에 해당
  
  - exit()
    
    - frees all the resources, notify parent
    
    - 프로세스의 종료
      
      - 자발적 종료
        
        - exit() 시스템 콜을 통한 방법
        
        - 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어줌
      
      - 비자발적 종료
        
        - 부모 프로세스가 자식 프로세스를 강제 종료시킴
          
          - 자식 프로세스가 한계치를 넘어서는 자원 요청
          
          - 자식에게 할당된 태스크가 더 이상 필요하지 않음
        
        - 키보드로 kill, break 등을 친 경우
        
        - 부모가 종료하는 경우
          
          - 부모 프로세스가 종료하기 전 자식이 먼저 종료됨

- 프로세스 간 협력
  
  - 독립적 프로세스 (Independent process)
    
    - 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함
  
  - 협력 프로세스 (Cooperating process)
    
    - 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음
  
  - 프로세스 간 협력 메커니즘 (IPC: Interprocess Communication)
    
    - message passing
      
      - **커널**을 통해 메시지 전달
      
      - 프로세스 사이에 공유 변수 (shared variable)를 일체 사용하지 않고 통신하는 시스템
        
        - direct communication
          
          - 통신하려는 프로세스의 이름을 명시적으로 표시
        
        - indirect communication
          
          - 커널에 존재하는 mailbox 또는 port를 통해 메시지를 간접적으로 전달
    
    - shared memory
      
      - 서로 다른 프로세스 간에도 **일부 주소 공간을 공유**하게 하는 메커니즘
      
      - 커널에 shared memory를 한다는 시스템 콜을 보내어 매핑을 한 후 공유
    
    - <<참고>> thread
      
      - thread는 사실상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 프로세스를 구성하는 thread 간에는 주소 공간을 공유하므로 협력 가능