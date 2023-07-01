# Queue

## 1. 설명

- stack과 달리 마지막에 추가된 항목을 제거하는 대신, 제일 먼저 queue에 추가된 항목을 제거
- **선입선출(FIFO)**
- 자바스크립트에서 지원하지 않으므로 간단하게 배열을 사용해서 구현 가능

```javascript
const queue = [];

// item을 제일 "마지막"에 추가
queue.push("value");

// item을 제일 "앞부터" 제거
const firstItem = queue.shift();
```

<br>

## 2. 현실 세계에서의 예시: 알림

- 실무에서 계속해서 위에 쌓이는 알림을 표시할 때 queue를 사용할 수 있음
- 화면 하단에 알림창이 나타났다가 일정 시간이 흐른 후에 사라지는 알림
- 사용자가 가상 커뮤니티에 가입할 때마다 알림창이 나타나는 경우 고려

<img src="https://media.graphassets.com/qINezXxwSPqGDLqZdGAS"/>

- 버튼을 클릭하면 `notifications` 배열(우리가 만든 queue)에 메세지가 추가됨
- queue에서 알림을 삭제하는 timeout이 설정되어 있음

```javascript
import { faker } from "@faker-js/faker";
import { useState } from "react";

function ButtonAddingNotifications() {
  const [notifications, setNotifications] = useState([]);

  const addNotification = () => {
    setNotifications((previous) => {
         // Array.push() 대신 불변한 Array.concat()를 사용합니다
=      return previous.concat(`${faker.name.firstName()} joined!`);
    });
    setTimeout(() => {
        // Array.shift() 대신 불변한 Array.slice()를 사용합니다
      setNotifications((previous) => previous.slice(1));
    }, 1000);
  };

  return (
    <>
      <button onClick={() => addNotification()}>
        Invite User To Community
      </button>

      <aside>
        {notifications.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </aside>
    </>
  );
}
```
