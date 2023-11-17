# [Firebase] Authentication - 계정 생성 구현하기

### 3.1. 사용자 입력 폼 구성

기능을 구현하기 전에 css를 먼저 구현했다.

사용자가 자신의 이름과 이메일, 비밀번호를 입력하는 폼을 만들었다. 이름과 이메일, 비밀번호는 모두 `required`로 설정했기 때문에 하나라도 작성하지 않으면 계정을 생성할 수 없다.

```typescript
// create-account.tsx

// ...

export default function CreateAccount() {
  const [isLoading, setIsLoading] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const {
      target: { name, value },
    } = e;
    if (name === "name") {
      setName(value);
    } else if (name === "email") {
      setEmail(value);
    } else if (name === "password") {
      setPassword(value);
    }
  };

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); // 화면 새로고침 방지
    try {
      // create an account
      // set the name of the user
      // redirect to the home page
    } catch (e) {
      // setError
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Wrapper>
      <Title>Join 𝕏</Title>
      <Form onSubmit={onSubmit}>
        <Input
          onChange={onChange}
          name="name"
          value={name}
          placeholder="Name"
          type="text"
          required
        />
        <Input
          onChange={onChange}
          name="email"
          value={email}
          placeholder="Email"
          type="email"
          required
        />
        <Input
          onChange={onChange}
          name="password"
          value={password}
          placeholder="Password"
          type="password"
          required
        />
        <Input
          type="submit"
          value={isLoading ? "Loading..." : "Create account"}
        />
      </Form>
      {error !== "" ? <Error>{error}</Error> : null}
    </Wrapper>
  );
}
```

![join 페이지](https://velog.velcdn.com/images/yeguu037/post/f9b74c9a-7ab1-476c-915b-ca6ca4de61a9/image.png)

> ❗ `e.preventDefault()` 사용하는 이유

이 코드에서 `e.preventDefault()`는 폼이 실제로 서버로 데이터를 보내지 않도록 하고, 대신에 `onSubmit` 함수에서 정의된 로직을 실행한다.

`e.preventDefault()`는 폼이 제출될 때 브라우저의 기본 동작을 중단시키는 역할을 한다. 기본적으로 HTML 폼이 제출되면 페이지가 새로고침되며, 이는 일반적으로 서버로 데이터를 전송하고 페이지를 다시 로드하는 동작을 수반한다. 하지만 React에서는 SPA의 일환으로, 페이지 전체를 다시 로드하지 않고도 애플리케이션의 상태를 업데이트하고 필요한 작업을 수행할 수 있다.

<br>

### 3.2. join 구현하기

`try` 안에 위에서 주석으로 작성해 둔 부분을 구현했다.

#### 3.2.1. create an account

```typescript
const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    // ...
    // 로딩중이거나 하나라도 작성하지 않았다면 함수 종료
    if (isLoading || name === "" || email === "" || password === "") return;
    try {
      // Firebase Authentication을 사용하여 사용자 계정 생성
      const credentials = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );
      // 계정 생성에 성공하면 사용자의 자격 증명을 받게 되고,
      // 계정이 이미 존재하거나 패스워드가 유요하지 않은 경우에 계정 생성에 실패함
    }
    // ...
  };
```

`createUserWithEmailAndPassword()`는 Firebase Authentication에서 제공하는 함수로, 이메일과 비밀번호를 사용하여 사용자 계정을 생성하는 데 사용된다. 계정 생성에 성공하면 사용자의 자격 증명을 받게 되고, 계정이 이미 존재하거나 패스워드가 유효하지 않은 경우에 계정 생성에 실패한다.

`createUserWithEmailAndPassword()`가 이메일과 비밀번호를 매개변수로 받기 때문에, 로딩 중이거나 `name`, `email`, `password` 중 하나라도 비어있는 경우 함수를 종료하도록 조건문을 작성했다.

<br>

#### 3.2.2. set the name of the user

사용자의 계정이 성공적으로 생성되면, 해당 사용자의 프로필을 업데이트하는 작업을 수행한다. 이 부분은 `updateProfile()` 메서드를 사용해서 구현했다.

```typescript
const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    // ...
    try {
      // ...
      // Firebase Authentication을 사용하여 사용자 프로필 업데이트
      await updateProfile(credentials.user, {
        displayName: name,
      });
      // Firebase의 사용자는 이름을 포함해서 작은 아바타 이미지의 URL을 가지는 미니 프로필을 갖게 됨
    }
    // ...
  };
```

`updateProfile()` 매서드는 Firebase Authentication에서 제공하는 함수로, 사용자의 프로필 정보를 업데이트한다. 위의 코드에서는 `displayName`을 사용해서 사용자의 이름을 설정했다.

<br>

#### 3.2.3. redirect to the home page

마지막으로, 사용자 계정 생성과 프로필 업데이트가 성공적으로 이뤄진 후에는 사용자를 애플리케이션의 홈 화면으로 리다이렉트해야 한다. 이를 위해 `navigate("/")`를 사용해서 화면을 전환헀다.

```typescript
export default function CreateAccount() {
  const navigate = useNavigate();
  // ...

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    try {
      // ...
      // 사용자가 계정 생성 및 프로필 업데이트 후에는 애플리케이션의 홈 화면으로 리다이렉트
      navigate("/");
    }
    // ...
  };

```

`navigate("/")`는 React Router의 `useNavigate` 훅을 사용해서 지정된 경로로 이동시키는 역할을 한다. 따라서 사용자는 계정 생성이 성공하면 즉시 애플리케이션의 홈 화면으로 이동하게 된다.

<br>

추가된 코드는 다음과 같다.

```typescript
// create-app.tsx

// ...

export default function CreateAccount() {
  const navigate = useNavigate();
  // ...

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (isLoading || name === "" || email === "" || password === "") return;

    try {
      setIsLoading(true);
      const credentials = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );

      await updateProfile(credentials.user, {
        displayName: name,
      });

      navigate("/");
    } catch (e) {
     // setError
    } finally {
      setIsLoading(false);
    }
  };

  return (
    // ...
  );
}
```
