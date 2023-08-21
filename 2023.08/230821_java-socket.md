# 직관적으로 이해로 Java.io를 활용한 채팅 정복

- io의 모든 정보를 아는 것이 아니라 필요한 것부터 익혀나가자.

- 코드를 보며 흐름을 이해해보자.

# 1. 서버

```java
package chat;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ChatServer {
	public static final int PORT = 9999;

	public static void main(String[] args) {
		ServerSocket serverSocket = null;
		List<ChatServerThread> userList = Collections.synchronizedList(new ArrayList<>());
		try {
			serverSocket = new ServerSocket();
			# 0.0.0.0은 서버소켓을 모든 사용 가능한 네트워크 인터페이스에서 서버가 수신대기
			serverSocket.bind(new InetSocketAddress("0.0.0.0", PORT));
			System.out.println("[SERVER] start [port : " + PORT + "]");

			while (true) {
				Socket socket = serverSocket.accept();
				new ChatServerThread(socket, userList).start();
			}
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}

}
```

먼저 서버 코드를 보자.

우리는 지금 **다중 채팅**을 만들어보려고 한다.

필요한 요소는

1. 서버를 열어줄 ServerSocket 클래스
2. 유저를 담을 동기화된 공간(userList)
3. bind - accept를 while문 안에 사용하여 지속적으로 클라이언트의 연결을 수락할 바운더리
4. 유저마다 생성될 `thread`

이걸 생각해보며 몇번씩 따라쳐보자.

# 2. thread

```java
package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketException;
import java.util.List;

public class ChatServerThread extends Thread {
	private String nickname;
	private Socket socket;
	private List<ChatServerThread> userList;

	public ChatServerThread(Socket socket, List<ChatServerThread> list) {
		this.socket = socket;
		this.userList = list;
	}

	@Override
	public void run() {
		try {
			PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
			BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));
			String msg = null;
			while ((msg = br.readLine()) != null) {
				System.out.println(msg);
				String[] tokens = msg.split(":");
				if (tokens[0].equals("join")) {
					join(tokens[1].trim(), pw);
					System.out.println("현재 인원: " + userList.size());
				} else if (tokens[0].equals("chat")) {
					message(tokens[1].trim());
				} else if (tokens[0].equals("quit")) {
					quit();
					break;
				}
			}

		} catch (SocketException e) {
			System.out.println("[ServerError] : " + e);
		} catch (IOException e) {
			System.out.println("[ServerError] : " + e);
		} finally {
			try {
				socket.close();
			} catch (IOException e) {
				System.out.println("[ServerError] : " + e);
			}
			userList.remove(this);
		}
	}

	public void notifyAllClients(String message) {
			try {
				for (ChatServerThread client : userList) {
					PrintWriter pw = new PrintWriter(new OutputStreamWriter(client.socket.getOutputStream()), true);
					pw.println(message);
				}
			} catch (IOException e) {
				System.out.println("[ServerError] : " + e);
			
		}

	}

	private void join(String nickname, PrintWriter user) {
		this.nickname = nickname;
		userList.add(this);
		log(nickname + "님이 입장하였습니다");
		user.println("입장: 확인");
		notifyAllClients(nickname + "님이 입장 하였습니다.");
	}
	

	private void message(String message) {
		log(nickname + " : " + message);
		System.out.println(nickname + " : " + message);
		notifyAllClients(nickname + ": " + message);
	}

	private void quit() {
		notifyAllClients(nickname + "님이 채팅방을 나갔어요.");
		log(nickname + "님이 퇴장하였음");
		userList.remove(this);
	}

	private void log(String message) {
		System.out.println("[EchoServer#" + nickname + "]" + " " + message);
		System.out.println("현재 인원: " + userList.size());
	}
}
```

큰 틀을 생각해보자

우리의 서버는 클라이언트와 “주고 받는” 것이 핵심이다. 이는 클라이언트에서도 핵심이 되는 내용이다.

`주고 받는` 것을 `PrintWriter`와 `BufferdReader` 를 생성하여 클라이언트와 통신할 수 있는 스트림을 설정한다!

# 2-1 근데 이걸 왜 쓰냐???? 이거 굉장히 의문입니다.

### **PrintWriter**

**`PrintWriter`** 클래스는 텍스트 데이터를 출력하기 위해 사용됩니다. 이 클래스의 장점은 다음과 같습니다.

- **인코딩 지원**: **`OutputStreamWriter`**와 함께 사용하면, 원하는 문자 인코딩을 지정할 수 있어 다양한 문자셋을 처리할 수 있습니다.
- **자동 플러시 지원**: **`true`**를 두 번째 매개변수로 전달하면, **`println`** 메서드를 호출할 때마다 버퍼의 내용이 자동으로 플러시되어 전송됩니다. 이로 인해 실시간으로 메시지를 클라이언트에 전송할 수 있게 됩니다.
- **편리한 메서드**: **`print`**와 **`println`** 메서드를 사용하면, 문자열뿐만 아니라 다양한 데이터 타입을 쉽게 출력할 수 있습니다.

### **BufferedReader**

**`BufferedReader`** 클래스는 텍스트 데이터를 읽기 위해 사용됩니다. 이 클래스의 장점은 다음과 같습니다.

- **버퍼링**: 내부 버퍼를 사용하므로, 매번 데이터를 직접 읽는 것보다 효율적입니다. 이는 네트워크 지연 등을 줄여 성능을 향상시킵니다.
- **편리한 읽기 메서드**: **`readLine`** 메서드를 사용하면, 한 줄씩 텍스트를 읽을 수 있으므로 텍스트 기반 프로토콜의 처리가 간편해집니다.

채팅 서버와 같은 애플리케이션에서 **`PrintWriter`**와 **`BufferedReader`**는 텍스트 기반의 통신을 간단하고 효과적으로 수행하기 위해 사용됩니다. 문자열 데이터를 손쉽게 읽고 쓸 수 있으며, 버퍼링과 인코딩 처리 등의 세부 사항을 자동으로 관리해줍니다.

```java
PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
```

- **`socket.getOutputStream()`**: 소켓의 출력 스트림을 반환합니다. 이 스트림을 통해 클라이언트에 데이터를 보낼 수 있습니다.
- **`new OutputStreamWriter(socket.getOutputStream(), "utf-8")`**: 출력 스트림을 UTF-8 인코딩으로 변환합니다. 이렇게 하면, 서버에서 클라이언트로 보내는 문자열이 UTF-8로 인코딩됩니다.
- **`new PrintWriter(..., true)`**: **`OutputStreamWriter`**를 사용하여 **`PrintWriter`** 객체를 생성합니다. **`true`** 매개변수는 자동 플러시 옵션을 활성화하며, **`println`** 메서드가 호출될 때마다 버퍼의 내용이 자동으로 전송됩니다.

```java
BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));
```

- **`socket.getInputStream()`**: 소켓의 입력 스트림을 반환합니다. 이 스트림을 통해 클라이언트로부터 데이터를 받을 수 있습니다.
- **`new InputStreamReader(socket.getInputStream(), "utf-8")`**: 입력 스트림을 UTF-8 인코딩으로 읽습니다. 이렇게 하면, 클라이언트에서 보낸 UTF-8로 인코딩된 문자열을 올바르게 해석할 수 있습니다.
- **`new BufferedReader(...)`**: **`InputStreamReader`**를 사용하여 **`BufferedReader`** 객체를 생성합니다. **`BufferedReader`**는 버퍼링을 사용하여 입력을 효율적으로 읽을 수 있게 해줍니다.

이런 의미에서 사용되는 `InputStream` 과 `OutputStream` `Reader` 클래스의 한 종류라고 보면 될 것 같습니다. 다른 종류의 스트림 클래스는 따로 공부해보세요!

# 2-2 그 이후는 쉽습니다.

서버와 클라이언트는 지속적으로 통신해야 합니다. 우리는 지속적 통신을 위해 바보상자인 컴퓨터에게 어떤 것을 출력하기 위해 보낼지, 출력 된 것을 받아올 지를 정해야 합니다.

```java
String msg = null;
			while ((msg = br.readLine()) != null) {
				System.out.println(msg);
				String[] tokens = msg.split(":");
				if (tokens[0].equals("join")) {
					join(tokens[1].trim(), pw);
					System.out.println("현재 인원: " + userList.size());
				} else if (tokens[0].equals("chat")) {
					message(tokens[1].trim());
				} else if (tokens[0].equals("quit")) {
					quit();
					break;
				}
			}
```

cmd창에서 실행했다고 했을 때, 첫 들어올 메시지를 null로 설정하고, cmd에서 들어올 메시지가 있고, null이 아닌 동안에 계속해서 돌리면 됩니다.

```java
try {
			socket = new Socket();
			socket.connect(new InetSocketAddress(SERVER_IP, ChatServer.PORT));

			PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
			BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));

			scanner = new Scanner(System.in);

			System.out.println("닉네임을 입력하세요>>");
			String nickname = scanner.nextLine();
			pw.println("join:" + nickname);
```

잠시 클라이언트 코드를 보자면, 저는 유저가 들어오면 → scanner로 입력을 받아오고,  이를 서버에 

`"join"` 을 default로 붙여 보내고, 유저가 편하게 닉네임만 입력할 수 있게 구성한 것입니다.

그 코드가 마지막 줄의 `pw.println` 코드입니다.

이렇게 클라이언트가 서버로 본인의 닉네임을 보내고 나면,

```java
String[] tokens = msg.split(":");
				if (tokens[0].equals("join")) {
					join(tokens[1].trim(), pw);
```

이를 통해 msg에 들어온 값을 `split`을 통해 분리하여 사용하는 것입니다.

그리고 `join` 함수는,

```java
private void join(String nickname, PrintWriter user) {
		this.nickname = nickname;
		userList.add(this);
		log(nickname + "님이 입장하였습니다");
		user.println("입장: 확인");
		notifyAllClients(nickname + "님이 입장 하였습니다.");
	}
```

서버에서 nickname을 지정하여 값을 가지고 있고, userList에 추가하고, PrintWriter객체인 user에 `println`을 통해 클라이언트에 이를 승인하겠다는 명령을 던져줍니다.

그래서 클라이언트는

```java
String confirm = br.readLine();
if (confirm.equals("입장: 확인")) {
				System.out.println("채팅방에 입장했어요.");	
			}
```

서버에서 또다시 날아온 메시지를 readLine메시지를 통해 읽으며 변수에 담아 주는 방식으로 진행됩니다.

위에서도 말했듯이, 서버와 클라이언트가 필요한 것을 

`서버`도 `printWriter`를 통해 `println`으로 전달하고,  

초기 필요한 값을 제외하고는 이것을 `클라이언트`가 스레드를 통해 `br.readLine()`을 통해 받는 형식입니다.

반대로,

`클라이언트`가 `pw.println`으로 `서버`에 전달하고, 이를 `서버`가 `br.readLine()`으로 받아오는 것의 연속된 형태인 것입니다.

따라서 이를 이해하면 클라이언트와 서버의 전체 코드를 이해하는데 도움이 될 것입니다.

```java

package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ConnectException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
	private static final String SERVER_IP = "127.0.0.1";

	public static void main(String[] args) {
		Socket socket = null;
		Scanner scanner = null;

		try {
			socket = new Socket();
			socket.connect(new InetSocketAddress(SERVER_IP, ChatServer.PORT));

			PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
			BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));

			scanner = new Scanner(System.in);

			System.out.println("닉네임을 입력하세요>>");
			String nickname = scanner.nextLine();
			pw.println("join:" + nickname);

			String confirm = br.readLine();
	
			if (confirm.equals("입장: 확인")) {
				System.out.println("채팅방에 입장했어요.");
	
			}
			# 입력 받았으니 채팅 시작
			new ChatClientThread(socket).start();

			while (true) {
				String msg = scanner.nextLine();
				if (msg.toLowerCase().equals("quit")) {
					pw.println("quit");
					break;
				}
				if (msg.equals("") == false) {
					pw.println("chat:" + msg);
				}
				if (scanner.hasNextLine() == false) {
					continue;
				}
			}

		} catch (ConnectException e) {
			System.out.println("[ClientError] : " + e);
		} catch (IOException e) {
			System.out.println("[ClientError] : " + e);
		} finally {
			try {
				if (scanner != null) {
					scanner.close();
				}
				if (socket != null && socket.isClosed() == false) {
					socket.close();
				}
			} catch (IOException e) {
				System.out.println("[ClientError] : " + e);
			}
		}
	}
}
```

```java
package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.SocketException;

public class ChatClientThread extends Thread {
	private Socket socket;

	public ChatClientThread(Socket socket) {
		this.socket = socket;
	}

	@Override
	public void run() {
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
			String msg;
			while ((msg = br.readLine()) != null) {
				System.out.println(msg);
			}
		} catch (SocketException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
```