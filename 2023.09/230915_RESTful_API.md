### REST (Representational State Transfer)

- 개념
  
  - 자원을 이름(자원의 표현)으로 구분해 해당 자원의 상태(정보)를 주고 받는 모든 것
    
    - 자원의 식별
      
      - URI 등
      
      - Client는 URI를 이용해 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청
    
    - 자원의 행위
      
      - HTTP Method 등
    
    - 자원의 표현
      
      - 자원과 행위를 통해 궁극적으로 표현되는 결과물
      
      - Client와 Server가 데이터를 주고받는 형태
      
      - JSON, XML, TEXT, RSS 등

- 특징
  
  - Server-Client (서버-클라이언트 구조)
    
    - 자원이 있는 쪽이 Server, 자원을 요청하는 쪽이 Client
    
    - 역할을 구분함으로써 서로 간 의존성 줄임
      
      - Server
        
        - API 제공, 비즈니스 로직 처리 및 저장
      
      - Client
        
        - 사용자 인증 등을 직접 관리하고 책임짐
  
  - 무상태 (Stateless)
    
    - Server가 Client의 상태를 보존하지 않음
      
      - Client의 context를 Server에 저장하지 않음
      
      - Server는 각각의 요청을 별개의 것으로 인식하고 처리
  
  - 캐시 처리 가능 (Cacheable)
    
    - 웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용할 수 있음
  
  - 계층화 (Layered System)
    
    - Client는 REST API Server만 호출
    
    - Client는 대상 서버에 직접 연결되었는지 중간 서버를 통해 연결되었는지 인지할 수 없음
    
    - 중간 서버 (로드 밸런싱, 공유 캐시)를 제공함으로써 시스템 규모 확장성이 향상
  
  - 인터페이스 일관성 (Uniform Interface)
    
    - 리소스는 URI로 식별됨
    
    - HTTP 메시지를 통해 리소스를 조작할 수 있음
    
    - 느슨한 결합 (Loosely Coupling)

### RESTful API

- RES의 설계 규칙을 잘 지켜서 설계된 API
  
  - API (Application Programming Interface)

- 특징
  
  - URI에 동사보다는 명사를,대문자보다는 소문자 사용
  
  - 마지막에 슬래시 (/) 포함하지 않음
  
  - 언더바 (_) 대신 하이픈 (-) 사용
  
  - 파일 확장자 포함하지 않음
  
  - URI에 행위 포함하지 않음
