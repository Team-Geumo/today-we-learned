- 프로세스와 관련한 시스템 콜
  
  - fork()
    
    - create a child (copy)
    
    - creates a new address space that is a duplicate of the caller
      
      ```c
      int main()
      {
          int pid;
          pid = fork();
          // child
          if (pid == 0)
              printf("\n Hello, I am a child!\n");
          // parent
          else if (pid > 0)
              printf("\n Hello, I am a parent!\n")
      }
      ```
      
      - 부모의 fork의 반환값 (return value)은 양수이고, 자식은  fork의 반환값이 0
      
      - 자식이 복제되었을 때 `int main()`부터 실행되는 것이 아니고 `if (pid == 0)` 줄부터 실행됨
        
        - 부모와 진행과정도 동일한 상태에서 시작
  
  - exec()
    
    - overlay new image
    
    - replaces the memory image of the caller `with a new program`
      
      ```c
      int main()
      {
          int pid;
          pid = fork();
          if (pid == 0)
          {
              printf("\n Hello, I am a child! Now I'll run date \n");
              execlp("/bin/date", "/bin/date", (char *) 0);
          }
          else if (pid > 0)
              printf("\n Hello, I am a parent!\n")
      }
      ```
      
      - execlp
        
        - exec 시스템 콜을 하는 함수
        
        - 이전의 기억은 잊고 새로운 프로그램으로 덮어 씌우는 것
      
      ```c
      int main()
      {
          printf("\n Hello, I am a child! Now I'll run date \n");
          execlp("/bin/date", "/bin/date", (char *) 0);
          printf("\n Hello, I am a parent!\n")
      }
      ```
      
      - exce 이후의 코드는 실행 불가능
        
        - `printf("\n Hello, I am a parent!\n")`는 실행되지 않음