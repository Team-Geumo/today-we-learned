```
package prob05;

import java.util.ArrayList;

import java.util.List;
import java.util.Scanner;

public class LoginMain {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		List<User> joinUsers = new ArrayList<User>();
		joinUsers.add(new User("둘리", "1234"));
		joinUsers.add(new User("마이콜", "5678"));
		joinUsers.add(new User("또치", "4321"));
		joinUsers.add(new User("도우너", "8765"));

		System.out.print("아이디를 입력하시오 : ");
		String id = scanner.nextLine();

		System.out.print("비밀번호를 입력하시오 : ");
		String password = scanner.nextLine();
		try {
			login(joinUsers, new User(id, password));
			System.out.println("로그인 성공");
		} catch (UserNotFoundException ex) {
			System.out.println("사용자를 찾을 수 없습니다.");
			return;
		} catch (PasswordDismatchException ex) {
			System.out.println("비밀번호가 틀렸습니다.");
			return;
		} finally {
			scanner.close();
		}
	}

	public static void login(List<User> users, User user) throws PasswordDismatchException, UserNotFoundException {
		/* 코드 작성 */
		boolean userFound = false;
		for (User u : users) {
			if (u.getId().equals(user.getId())) {
				userFound = true;
				if (u.getPassword().equals(user.getPassword())) {
					return;
				} else {
					throw new PasswordDismatchException();
				}
			}
		}
		if (!userFound) {
			throw new UserNotFoundException();
		}
	}
}

```

```
package prob05;

@SuppressWarnings("serial")
public class PasswordDismatchException extends RuntimeException{
	public PasswordDismatchException() {

	}
}

```

```
package prob05;

public class User {
	private String id;
	private String password;

	public User(String id, String password) {
		this.id = id;
		this.password = password;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		User other = (User) obj;
		if (id == null) {
			if (other.id != null)
				return false;
		} else if (!id.equals(other.id))
			return false;
		return true;
	}


}

```

```
package prob05;

@SuppressWarnings("serial")
public class UserNotFoundException extends RuntimeException{
	public UserNotFoundException() { }
}

```
