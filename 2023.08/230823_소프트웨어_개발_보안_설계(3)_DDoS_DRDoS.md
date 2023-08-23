### SW 공격기법 (2)

- DDoS (Distributed DoS) 공격
  
  - 개념
    
    - 분산 서비스 거부 공격
    
    - DoS 공격의 또 다른 형태로 여러 대의 공격자를 분산 배치하여 동시에 동작하게 함으로써 특정 사이트를 공격하는 기법
    
    - 해커의 취약한 인터넷 시스템에 대한 액세스가 이루어지면, 침입한 시스템에 소프트웨어를 설치하고 이를 실행시켜 원격에서 공격을 개시
  
  - DoS 공격과의 차이점
    
    - DoS
      
      - `1대의 공격자 컴퓨터`에서 타깃 시스템에 악성 패킷을 보내는 방식으로 공격
      
      - 타깃 시스템에서 공격자의 주소를 확인하고 차단하면 더 이상의 공격 불가능
    
    - DDoS
      
      - 공격자가 여러 대의 컴퓨터를 감염시켜 이를 이용해 타깃 시스템을 집중적으로 공격해서 서비스를 마비시킴
        
        - `수많은 감염 호스트를 통해 공격`
  
  - 구성요소
    
    - 핸들러 (Handler)
      
      - 마스터 시스템의 역할을 수행하는 프로그램
    
    - 에이전트 (Agent)
      
      - 공격 대상에 직접 공격을 가하는 시스템
    
    - 마스터 (Master)
      
      - 공격자에게 직접 명령을 받는 시스템
      
      - 여러 대의 에이전트를 관리
    
    - 공격자 (Attacker)
      
      - 공격을 주도하는 해커의 컴퓨터
    
    - 데몬 프로그램 (Daemon)
      
      - 에이전트 시스템 역할을 수행하는 프로그램
  
  - 도구
    
    - Trinoo
      
      - 많은 소스로부터 통합된 UDP flood 서비스 거부 공격을 유발하는 데 사용되는 도구
      
      - 몇 개의 서버 (혹은 마스터)와 많은 수의 클라이언트 (데몬)으로 이루어짐
    
    - Tribe Flood Network (TFN)
      
      - 많은 소스에서 하나 혹은 여러 개의 목표 시스템에 대해 서비스 거부 공격을 수행할 수 있는 도구
      
      - 공격자가 클라이언트 (마스터) 프로그램을 통해 공격 명령을 일련의 TFN 서버 (데몬)에게 보냄
      
      - UDP flood 공격 뿐 아니라 TCP SYN flood 공격, ICMP echo 요청 공격, ICMP 브로드캐스트 공격 (Smurf 공격) 수행 가능
    
    - Stacheldraht
      
      - 분산 서비스 거부 에이전트 역할을 하는 Linux 및 Solaris 시스템용 멀웨어 도구
      
      - ICMP flood, SYN flood, UDP flood와 Smurf 등의 공격에 의해 DDoS 공격 가능
  
  - 대응 방안
    
    - 차단 정책 업데이트, 좀비PC IP 확보, 보안 솔루션 운영, 홈페이지 보안 관리, 시스템 패치
  
  - 종류
    
    | 구분                       | 종류                          | 상세 공격 유형               |
    | ------------------------ | --------------------------- | ---------------------- |
    | 대역폭 소진 공격 (3~4계층)        | UDP/ICMP Traffic Flooding   | UDP/ICMP Flooding      |
    |                          |                             | DNS Query Flooding     |
    |                          | TCP Traffic Flooding        | SYN Flooding           |
    |                          |                             | SYN + ACK Flooding     |
    |                          | IP Flooding                 | LAND Attack            |
    |                          |                             | Teardrop               |
    | 서비스 (애플리케이션) 마비 공격 (7계층) | HTTP Traffic Flooding       | GET Flooding           |
    |                          |                             | GET with Cache-Control |
    |                          | HTTP Header/Option Spoofing | Slowris                |
    |                          |                             | Slowloris              |
    |                          |                             | Slow Read Attack       |
    |                          | Other L7 Service Flooding   | Hash DoS               |
    |                          |                             | Hulk DoS               |
    |                          |                             | FTP/SMTP Attack        |

- DRDoS (Distributed Reflection DoS) 공격
  
  - 개념
    
    - 공격자는 출발지 IP를 공격대상 IP로 위조하여 다수의 반사 서버로 요청 정보를 전송, 공격 대상자는 반사 서버로부터 다양의 응답을 받아 서비스 거부가 되는 공격
    
    - 본넷 기기가 직접 공격을 수행하는 것이 아니라 증폭 공격에 활용되는 서비스를 제공하는 서버 및 서버 역할을 할 수 있는 단말 장비 (네트워크 장비, 공유기 등)까지 공격기기로 이용
      
      - 본넷
        
        - 해커의 명령을 수행하는 감염된 디바이스의 대규모 집합
  
  - DDoS 공격과의 차이점
    
    - DRDoS는 DDoS에 비해 공격 근원지 파악이 어렵고, 공격 트래픽 생성 효율이 DDoS보다 훨씬 큼
  
  - 방식
    
    - 출발지 IP 변조
      
      - 공격자가 출발지 IP를 공격 대상자 IP로 Spoofing하여 SYN 패킷을 공격 경유지 서버로 전송
    
    - 공격 대상자 서버로 응답
      
      - 경유지 서버는 SYN 패킷을 받고 공격 대상자 서버로 SYN/ACK를 전송
    
    - 서비스 거부
      
      - 공격 대상자 서버는 수많은 SYN/ACK를 받게 되어 서비스 거부
  
  - 대응 방안
    
    - ISP(인터넷 서비스 사업자; Internet Service Provider)가 직접 차단
    
    - 반사 서버에서 연결을 완료하지 않은 SYN 출처 IP를 조사하여 블랙 리스트로 운영, 공격 서버를 사전에 차단
    
    - 공격대상 서버 IP와 포트를 변경, 필터링하여 운영