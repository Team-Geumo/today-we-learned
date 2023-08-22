# 3-way handshake

1. TCP는 장치들 사이에 논리적인 접속을 성립(establish)하기 위하여 three-way handshake를 사용한다.
2. **TCP 3 Way Handshake는 TCP/IP프로토콜을 이용해서 통신을 하는 응용프로그램이 데이터를 전송하기 전에 먼저 정확한 전송을 보장하기 위해 상대방 컴퓨터와 사전에 세션을 수립하는 과정을 의미한다.**

Client > Server : **TCP SYN**

Server > Client : **TCP SYN, ACK**

Client > Server : **TCP ACK**

여기서 SYN은 'synchronize sequence numbers', 그리고 ACK는'acknowledgment' 의 약자이다.

이러한 절차는 TCP 접속을 성공적으로 성립하기 위하여 반드시 필요하다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8b6e04c-b447-46dc-a87e-a9da9dd60f17/Untitled.png)

## **TCP의 3-way Handshaking 과정**

1. A -> B : 내 말 들려?
2. B -> A : 잘 들려. 내 말은 들려?
3. A -> B : 잘 들려!

SYN (synchronize sequence numbers) - 연결 확인을 위해 보내는 무작위의 숫자값 (내 말 잘 들려?)

ACK (acknowledgements) - Client 혹은 Server로부터 받은 SYN에 1을 더해 SYN을 잘 받았다는 ACK (잘 들려)

ISN (Initial sequence numbers) - Client와 Server가 각각 처음으로 생성한 SYN

**[STEP 1]**

A클라이언트는 B서버에 접속을 요청하는 SYN 패킷을 보낸다.

이때 A클라이언트는 SYN 을 보내고 SYN/ACK 응답을 기다리는 **SYN_SENT** 상태, **B서버는 Wait for Client** 상태이다.

**[STEP 2]**

B서버는 SYN요청을 받고 A클라이언트에게 요청을 수락한다는 ACK 와 SYN flag 가 설정된 패킷을 발송하고

A가 다시 ACK으로 응답하기를 기다린다. 이때 **B서버**는 **SYN_RECEIVED** 상태가 된다.

**[STEP 3]**

A클라이언트는 B서버에게 ACK을 보내고 이후로부터는 연결이 이루어지고 데이터가 오가게 되는것이다.

이때의 **B서버 상태가 ESTABLISHED** 이다.

위와 같은 방식으로 통신하는것이 신뢰성 있는 연결을 맺어 준다는 TCP의 3 Way handshake 방식이다.

# 4-way handshake

4-Way handshake는 세션을 종료하기 위해 수행되는 절차입니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81ebc101-e01f-4b36-9f11-e46100760c6d/Untitled.png)

## **TCP의 4-way Handshaking 과정**

1. A -> B: 나는 다 보냈어. 이제 끊자!
2. B -> A: 알겠어! 잠시만~
3. B -> A: 나도 끊을게!
4. A -> B: 알겠어!

**[STEP 1]**

클라이언트가 연결을 종료하겠다는 FIN플래그를 전송한다. 이때 **A클라이언트는  FIN-WAIT** 상태가 된다.

**[STEP 2]**

B서버는 FIN플래그를 받고, 일단 확인메시지 ACK 보내고 자신의 통신이 끝날때까지 기다리는데 이 상태가

**B서버의 CLOSE_WAIT**상태다.

**[STEP 3]**

연결을 종료할 준비가 되면, 연결해지를 위한 준비가 되었음을 알리기 위해  클라이언트에게 FIN플래그를 전송한다. 이때 B서버의 상태는 **LAST-ACK**이다.

**[STEP 4]**

클라이언트는 해지준비가 되었다는 ACK를 확인했다는 메시지를 보낸다.

**A클라이언트의 상태가 FIN-WAIT ->TIME-WAIT** 으로 변경된다.

그런데 만약 "Server에서 FIN을 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN패킷보다 늦게 도착하는 상황"이 발생한다면 어떻게 될까요?

Client에서 세션을 종료시킨 후 뒤늦게 도착하는 패킷이 있다면 이 패킷은 Drop되고 데이터는 유실될 것입니다.

**A클라이언트**는 이러한 현상에 대비하여 Client는 Server로부터 FIN을 수신하더라도 일정시간(디폴트 240초) 동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정을 거치게 되는데 이 과정을 **"TIME_WAIT"** 라고 합니다. 일정시간이 지나면, 세션을 만료하고 연결을 종료시키며, **"CLOSE"** 상태로 변화합니다.

### **[Time-Wait?](https://seongonion.tistory.com/74#Time-Wait%-F)**

먼저 연결을 끊는 (active closer) 쪽에 생성되는 소켓으로, 혹시 모를 패킷 전송 실패에 대비하기 위하여 존재하는 소켓이다.

### **[Time-wait이 없다면?](https://seongonion.tistory.com/74#Time-wait%EC%-D%B-%--%EC%--%--%EB%-B%A-%EB%A-%B-%-F)**

패킷의 손실이 발생하거나 통신자 간 연결 해제가 제대로 이루어지지 않을 수 있다!

EX) Passive closer에서 보낸 FIN 메시지에 대해 Active closer가 보낸 ACK를 Passive closer가 받지 못한 경우

1. Passive Closer의 FIN 메시지 전송
2. Active Closer가 수신 후 ACK 메시지 전송 후, 통신 끊음 (Time-wait X)
3. Passive Closer가 ACK를 수신하지 못함
4. 일정 시간 후, ACK를 수신하지 못한 Passive Closer가 다시 FIN 메시지 전송.
5. Active Closer는 이미 Closed 상태이기 때문에 FIN 메시지 수신 불가
6. TCP 통신이 제대로 끊기지 않음
