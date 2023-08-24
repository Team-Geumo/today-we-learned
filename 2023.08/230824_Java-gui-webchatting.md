```
package chat.gui;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Panel;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.net.SocketException;

import javax.print.DocFlavor.BYTE_ARRAY;

public class ChatWindow {

	private Frame frame;
	private Panel pannel;
	private Button buttonSend;
	private TextField textField;
	private TextArea textArea;

	private Socket socket;
	private PrintWriter pw;
	private BufferedReader br;

	public ChatWindow(String nickname, Socket socket) {
		frame = new Frame(nickname);
		pannel = new Panel();
		buttonSend = new Button("Send");
		textField = new TextField();
		textArea = new TextArea(30, 80);
		this.socket = socket;
	}

	public void show() {
		// Button
		buttonSend.setBackground(Color.GRAY);
		buttonSend.setForeground(Color.WHITE);
		buttonSend.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent actionEvent) {
				sendMessage();
//				System.out.println("click");
			}
		});
//		buttonSend.addActionListener((ActionEvent e) -> {
//			
//		});
		// Textfield
		textField.setColumns(80);
		textField.addKeyListener(new KeyAdapter() {

			@Override
			public void keyPressed(KeyEvent e) {
				char keyCode = e.getKeyChar();
				if (keyCode == KeyEvent.VK_ENTER) {
					sendMessage();
				}
			}
		});
		// Pannel
		pannel.setBackground(Color.LIGHT_GRAY);
		pannel.add(textField);
		pannel.add(buttonSend);
		frame.add(BorderLayout.SOUTH, pannel);

		// TextArea
		textArea.setEditable(false);
		frame.add(BorderLayout.CENTER, textArea);

		// Frame
		frame.addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				// 닫았을 때 catch
				finish();
			}
		});
		frame.setVisible(true);
		frame.pack();

		// IOStream 받아오기
		try {
			pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
			br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));
		} catch (UnsupportedEncodingException e1) {
			e1.printStackTrace();
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		// ChatClientThread 생성하고 실행하는 코드
		new ChatClientThread().start();
	}

	private void finish() {
		try {
			if (socket != null && socket.isClosed()) {
				socket.close();
			}
			pw.println("quit");
			System.exit(0);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	private void quit() {
		String message = textField.getText();
		if ("quit".equals(message)) {
			pw.println("quit");
		}
	}

	private void sendMessage() {
		String message = textField.getText();
		System.out.println(message);
		if ("quit".equals(message)) {
			quit();
		}
		pw.println("chat:" + message);
		textField.setText("");
		textField.requestFocus();
	}

	private void updateTextArea(String message) {
		textArea.append(message);
		textArea.append("\n");
	}

	private class ChatClientThread extends Thread {
		@Override
		public void run() {
			String msg = null;
			try {
				while ((msg = br.readLine()) != null) {
					if (!"입장: 확인".equals(msg)) {
						updateTextArea(msg);
					}
				}
			} catch (SocketException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			} finally {
				finish();
			}
		}
	}
}

```

```
package chat.gui;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ConnectException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.Scanner;

public class ChatClientApp {
	private static final String SERVER_IP = "127.0.0.1";
	private static final int PORT = 9999;

	public static void main(String[] args) {
		String name = null;
		Scanner scanner = new Scanner(System.in);
		Socket socket = null;
		String nickname = null;
		try {
			while (true) {
				System.out.println("대화명을 입력하세요.");
				System.out.print(">>> ");
				nickname = scanner.nextLine();

				if (nickname.isEmpty() == false) {
					break;
				}
				System.out.println("대화명은 한글자 이상 입력해야 합니다.\n");
			}

			scanner.close();

			socket = new Socket();

			socket.connect(new InetSocketAddress(SERVER_IP, PORT));
			PrintWriter pw = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "utf-8"), true);
			BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream(), "utf-8"));

			new ChatWindow(nickname, socket).show();
			pw.println("join: " + nickname);
		} catch (ConnectException e) {
			System.out.println("[Connection Error] : " + e);
		} catch (IOException e) {
			System.out.println("[IO Error] : " + e);
		} finally {
			if (scanner != null) {
				scanner.close();
			}
		}

	}

}

```

```
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

```
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
		userList.remove(this);
		notifyAllClients(nickname + "님이 채팅방을 나갔어요.");
		log(nickname + "님이 퇴장하였음");

	}

	private void log(String message) {
		System.out.println("[EchoServer#" + nickname + "]" + " " + message);
		System.out.println("현재 인원: " + userList.size());
	}
}

```

수정 완성