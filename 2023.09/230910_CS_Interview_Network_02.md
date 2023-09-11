### **04 HTTP에 대해 설명해 주세요.**

HTTP는 Hyper-Text Transfer Protocol의 약자로, Hypertext인 HTML을 주고받기 위한 규약(protocol)입니다. HTTPS에서 마지막의 S는 over **S**ecure socket Layer의 약자로 HTTP에서 보안이 강화된 버전이다. SSL 프로토콜 위에서 돌아가는 HTTP 프로토콜

[https://velog.io/@dong5854/HTTPS와-SSL인증서-대칭키-공개키비대칭키](https://velog.io/@dong5854/HTTPS%EC%99%80-SSL%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%8C%80%EC%B9%AD%ED%82%A4-%EA%B3%B5%EA%B0%9C%ED%82%A4%EB%B9%84%EB%8C%80%EC%B9%AD%ED%82%A4)

**➕ 공개키와 대칭키에 대해 설명해 주세요.**

- 공개키 방식은 두개의 키를 갖게 되는데 A키를 사용해 암호화를 하면 B키로 복호화를 할수 있고, B키로 암호화를 하면 A키로 복호화를 할 수 있는 방식.즉, 키A를 통해 암호화한 내용은 키A를 이용해 복호화 하는 것은 불가능하고 키A와 쌍을 이루는 키B를 사용해야만 복호화가 가능하다. 두개의 키 중 하나를 비공개키(private key, 개인키, 비밀키라고도 부른다)로 하여 자신만이 가지고 있고, 나머지를 공개키로 지정하여 대중에게 공개한다.
- 대칭키는 암호화에 사용되는 키와 복호화에 사용되는 키가 동일일 암호화 기법이다.
- [https://velog.io/@dong5854/HTTPS와-SSL인증서-대칭키-공개키비대칭키](https://velog.io/@dong5854/HTTPS%EC%99%80-SSL%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%8C%80%EC%B9%AD%ED%82%A4-%EA%B3%B5%EA%B0%9C%ED%82%A4%EB%B9%84%EB%8C%80%EC%B9%AD%ED%82%A4)

**➕ 왜 HTTPS Handshake 과정에서는 인증서를 사용하는 것 일까요?**

- [https://velog.io/@ann0905/HTTPS-2.-HTTPS와-SSL-Handshake](https://velog.io/@ann0905/HTTPS-2.-HTTPS%EC%99%80-SSL-Handshake)

**➕ SSL과 TLS의 차이는 무엇인가요?**

- SSL(Secure Sockets Layer)과 TLS(Transport Layer Security)의 차이는 우선 TLS가 SSL의 업그레이드 된 버전이며, TLS가 SSL보다 알림 메시지의 유형이 다양하며 이 알림 메시지까지 암호화 됩니다. 그리고 메시지 인증은 SSL은 MAC, TLS는 HMAC을 사용하고, TLS에서는 고급화 된 암호화 알고리즘을 사용한다는 차이점이 있습니다.
- https://aws.amazon.com/ko/compare/the-difference-between-ssl-and-tls/

### **05 웹소켓과 소켓 통신의 차이에 대해 설명해 주세요.**

웹소켓은 소켓 통신에 기반하여 웹 어플리케이션에 맞게 발전한 형태로 소켓 통신을 합니다. 차이점으로는 OSI 7계층 기준으로 소켓은 인터넷 프로토콜에 기반하므로 TCP, UDP가 속한 4계층에 위치하며 웹 소켓은 TCP에 의존하지만 HTTP에 기반하므로 7계층에 위치합니다. 그리고 TCP에 기반한 소켓 통신은 단순히 바이트 스트림을 통한 데이터 전송이므로 바이트로 이루어진 데이터를 다뤄야하지만, 웹소켓 통신은 어플리케이션 계층인 7계층에 기반하기 때문에 메시지 형식의 데이터를 다루게 됩니다.

https://gusrb3164.github.io/web/2021/10/28/websocket-socket/

**➕ 소켓과 포트의 차이가 무엇인가요?**

- 소켓은 컴퓨터 네트워크의 노드 내에서 데이터를 보내고 받기 위한 내부 엔드포인트고, 포트는 통신의 엔드포인트에서 각 응용 프로그램에 할당되는 숫자입니다. 소켓이 특정 포트를 통해 데이터를 주고받는 인터페이스 역할이라면 포트는 특정 어플리케이션이나 프로세스를 식별하는 데 도움을 줍니다.
- https://tigercoin.tistory.com/189

**➕ 여러 소켓이 있다고 할 때, 그 소켓의 포트 번호는 모두 다른가요?**

- 아니요. 하나의 포트로 여러 개의 소켓을 열 수 있기 때문에, 포트 번호가 동일할 수 있습니다. 이런 경우 상대측 포트 번호로 소켓을 구분할 수 있습니다.
- [https://aal-izz-well.tistory.com/entry/포트와-소켓의-차이-및-호스트](https://aal-izz-well.tistory.com/entry/%ED%8F%AC%ED%8A%B8%EC%99%80-%EC%86%8C%EC%BC%93%EC%9D%98-%EC%B0%A8%EC%9D%B4-%EB%B0%8F-%ED%98%B8%EC%8A%A4%ED%8A%B8)
- [https://velog.io/@jehpark/Socket과-Port-Port는-같지만-Socket이-다를때는](https://velog.io/@jehpark/Socket%EA%B3%BC-Port-Port%EB%8A%94-%EA%B0%99%EC%A7%80%EB%A7%8C-Socket%EC%9D%B4-%EB%8B%A4%EB%A5%BC%EB%95%8C%EB%8A%94)
