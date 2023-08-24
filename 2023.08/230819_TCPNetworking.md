```
# TCP 네트워킹

- IP주소로 프로그램들이 통신할 때는 약속된 데이터 전송 규약이 있음
- 이를 전송용 프로토콜이라 부르며, 인터넷에서는 TCP(Tranmission Control Protocol), UDP (User Diagram Protocol)이 있음

- `TCP`는 연결형 프로토콜로, 상대방이 연결된 상태에서 데이터를 주고받음
- 클라이언트가 연결 요청을 하고 서버가 연결을 수락하면 통신 회선이 고정되고, 데이터는 고정 회선을 통해 전달됨
- 그렇기 때문에 `TCP`는 보낸 데이터가 순서대로 전달되며 `손실`이 발생하지 않는다.
- `TCP`는 `IP`와 함께 사용하기 때문에 `TCP/IP`라고도 한다. TCP는 웹 브라우저가 웹 서버에 연결할 때 사용 되며 이메일 전송, 파일 전송, DB 연동에도 사용 된다.
- `Java`는 `TCP 네트워킹`을 위해 `[java.net](http://java.net)` 패키지에서 `ServerSocket`과 `Socket`클래스를 제공
- `ServerSocket` 은 클라이언트의 연결을 수락하는 `서버`쪽 클래스이고, `Socket`은 `클라이언트`에서 연결 요청할 때와 클라이언트와 서버 양쪽에서 데이터를 주고 받을 때 사용되는 클래스이다.
- `ServerSocket`을 생성할 때는 `바인딩`할 `Port` 번호를 지정해야 한다. 서버가 실행 되면 클라이언트는 `Socket`을 이용해서 서버의 IP주소와 Port 번호로 연결 요청을 할 수 있다. `ServerSocket`은 `accept` 메소드로 연결 수락을 하고 통신용 Socket을 생성한다.
- 그리고 나서 클라이언트와 서버는 양쪽의 Socket을 이용해서 데이터를 주고받게 된다.
```