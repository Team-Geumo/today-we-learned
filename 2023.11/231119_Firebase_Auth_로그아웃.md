# [Firebase] Authentication - Log Out

로그인을 구현하기 전에 임시로 `Home` 컴포넌트에 로그아웃을 구현헀다.

```typescript
// Home.tsx

import { auth } from "../firebase";

export default function Home() {
  const logOut = () => {
    auth.signOut();
  };

  return (
    <h1>
      <button onClick={logOut}>Log Out</button>
    </h1>
  );
}
```

> ❗ `auth.signOut()`

현재 로그인한 사용자를 로그아웃하는 역할을 한다. 위의 코드에서 `logout` 함수는 이 메서드를 호출해서 사용자를 로그아웃시킨다.
