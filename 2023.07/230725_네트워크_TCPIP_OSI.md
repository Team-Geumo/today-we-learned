### OSI 7계층과 TCP/IP 4계층

- 공통점
  
  - 컴퓨터 네트워크 프로토콜 스택의 구조를 설명하기 위해 만들어진 모델
  
  - 서로 다른 방식으로 계층을 정의하고 있으며, 각 계층은 특정 기능을 수행
  
  - 상위 계층은 하위 계층의 서비스를 이용하여 데이터를 전달

- 차이점
  
  - OSI 7계층
    
    - 국제 표준화 기구(ISO)에 의해 정의된 공식 표준 모델
    
    - 교육과 이론적인 이해를 위해 사용되는 경우가 많음
  
  - TCP/IP 4계층
    
    - 현재 인터넷에서 가장 많이 사용되는 프로토콜 스택
    
    - 인터넷의 발전과 함께 실질적인 표준이 됨

| OSI 7계층                    | TCP/IP 4계층                        |
| -------------------------- | --------------------------------- |
| 응용 계층(Application Layer)   | 응용 계층(Application Layer)          |
| 표현 계층(Presentation Layer)  |                                   |
| 세션 계층(Session Layer)       |                                   |
| 전송 계층(Transport Layer)     | 전송 계층(Transport Layer)            |
| 네트워크 계층(Network Layer)     | 인터넷 계층(Internet Layer)            |
| 데이터 링크 계층(Data Link Layer) | 네트워크 액세스 계층(Network Access Layer) |
| 물리 계층(Physical Layer)      |                                   |

#### OSI 7계층

1. 물리 계층(Physical Layer)
   
   - 비트 단위로 데이터를 전송하는 물리적인 특성과 연결을 다룸
   
   - 케이블 종류, 전압 등

2. 데이터 링크 계층(Data Link Layer)
   
   - 프레임 단위로 데이터를 전송하고 오류 검출과 흐름 제어를 수행
   
   - 이더넷, PPP 등의 프로토콜

3. 네트워크 계층(Network Layer)
   
   - IP 주소를 할당하고 라우터를 통해 목적지까지 패킷을 전달

4. 전송 계층(Transport Layer)
   
   - TCP와 UDP를 이용하여 데이터를 종단간에 전송
   
   - 에러 복구와 흐름 제어

5. 세션 계층(Session Layer)
   
   - 통신 세션을 설정, 유지, 종료하는 기능을 수행
   
   - 인증과 동기화

6. 표현 계층(Presentation Layer)
   
   - 데이터의 형식 변환, 압축, 암호화 등을 수행
   
   - 표준화된 형식으로 응용 계층에 전달

7. 응용 계층(Application Layer)
   
   - 최종 사용자의 인터페이스를 제공하고 응용 프로그램과 직접 상호 작용

#### TCP/IP 4계층

1. 네트워크 액세스 계층(Network Access Layer)
   
   - 하드웨어적인 요소들을 다루며, 데이터 링크 계층과 물리 계층으로 구성
   
   - 네트워크 장비와의 통신을 관리하고 물리적인 매체를 통해 데이터 전송을 처리

2. 인터넷 계층(Internet Layer)
   
   - IP(Internet Protocol)를 사용하여 데이터를 패킷 단위로 전송
   
   - 라우팅과 데이터의 경로 선택을 수행하며, IP 주소를 관리

3. 전송 계층(Transport Layer)
   
   - 데이터의 신뢰성과 흐름 제어
   
   - TCP와 UDP를 이용하여 포트를 통해 양 끝의 애플리케이션들 간에 데이터를 주고받음

4. 응용 계층(Application Layer)
   
   - 사용자와 네트워크 간의 상호 작용을 처리
   
   - HTTP, FTP, SMTP 등의 프로토콜