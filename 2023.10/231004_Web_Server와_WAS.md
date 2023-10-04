### Web Server

- 개념
  
  - Http 프로토콜을 기반으로, 클라이언트의 요청을 서비스
  
  - **정적 컨텐츠만 처리**하도록 기능 분배를 해서 서버 부담을 줄임
    
    - 정적 컨텐츠(.html .jpeg .css 등) 제공
      
      - WAS를 거치지 않고 바로 자원 제공
    
    - 동적 컨텐츠 제공을 위한 요청 전달
      
      - 클라이언트 요청을 WAS에 보내고, WAS에서 처리한 결과를 클라이언트에게 전달

- 종류
  
  - Apache, Nginx, Microsoft IIS 등

### WAS (Web Application Server)

- 개념
  
  - DB 조회 및 다양한 로직 처리 요구시 **동적인 컨텐츠**를 제공하기 위해 만들어진 애플리케이션 서버
  
  - HTTP를 통해 애플리케이션을 수행해주는 미들웨어

- 역할
  
  - Web Server + Web Container

- 기능
  
  - 프로그램 실행 환경 및 DB 접속 기능 제공
  
  - 여러 트랜잭션 관리 기능
  
  - 업무 처리하는 비즈니스 로직 수행

- 종류
  
  - Tomcat, JBoss 등