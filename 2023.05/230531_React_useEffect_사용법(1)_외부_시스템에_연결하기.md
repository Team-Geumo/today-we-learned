# useEffect 사용법 (1)

## 3. Usage

### 3.1. 외부 시스템에 연결하기

때로는 컴포넌트가 페이지에 표시되는 동안 네트워크, 일부 브라우저 API 또는 타사 라이브러리에 연결 상태를 유지해야 할 수도 있다. 이러한 시스템은 React에서 제어되지 않으므로 _외부(external)_ 라고 한다.

[컴포넌트를 외부 시스템에 연결하려면](https://react-ko.dev/learn/synchronizing-with-effects) 컴포넌트의 최상위 레벨에서 `useEffect`를 호출하라.

<br>

```javascript
import { useEffect } from "react";
import { createConnection } from "./chat.js";

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState("https://localhost:1234");

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [serverUrl, roomId]);
  // ...
}
```

`useEffect`에는 두 개의 인자를 전달해야 한다.

1. 해당 시스템에 연결하는 <span style='background-color:#fff5b1'>setup code</span>가 포함된 _setup function_

   - 해당 시스템과의 연결을 끊는 <span style='background-color:#fff5b1'>cleanup code</span>가 포함된 *cleanup function*을 반환해야 한다.

2. 해당 함수 내부에서 사용되는 컴포넌트의 모든 값을 포함한 <span style='background-color:#fff5b1'>의존성 목록</span>

<details>
<summary>Setup, Cleanup 이란?</summary>
<div markdown="1">

- **Setup**

  - `useEffect` 함수의 본문에서 이루어지는 작업
  - 사이드 이펙트를 발생시키는 곳
  - 여기서 API를 호출할 수 있으며, 이벤트 리스너를 설정하거나, 타이머를 설정하는 등의 작업이 이루어짐

- **Cleanup**

  - `useEffect`에서 반환하는 함수에서 이루어지는 작업
  - 컴포넌트가 unmount되거나, 또는 다음 `useEffect` 실행 전에 호출
  - 이 부분에서는 보통 setup 단계에서 설정한 사이드 이펙트를 *청소*하는 작업이 이루어짐
  - ex: 설정한 이벤트 리스너를 제거하거나, 설정한 타이머를 제거하는 등의 작업을 수행

- **예제**

  ```javascript
  useEffect(() => {
    // Setup
    const timerID = setInterval(() => {
      console.log("This will run after a specified interval.");
    }, 1000);

    // Cleanup
    return () => {
      clearInterval(timerID);
      console.log("Cleanup: The interval has been cleared.");
    };
  }, []);
  ```

  - 위 예제에서 `setInterval`은 setup 단계에서 타이머를 설정하고, `clearInterval`은 cleanup 단계에서 타이머를 제거함
  - 이를 통해 `useEffect`는 컴포넌트의 라이프사이클 중 적절한 시점에 사이드 이펙트를 실행하고 청소할 수 있음

</div>
</details>

<br>

**React는 필요할 때마다 setup 및 cleanup function을 호출하는데, 이는 여러 번 발생할 수 있다.**

1. 컴포넌트가 페이지에 추가될 때(_mount_) 마다 <span style='background-color:#fff5b1'>setup code</span>를 실행한다.

2. 컴포넌트가 페이지에서 제거되면(_unmount_) 마지막으로 한 번 <span style='background-color:#fff5b1'>cleanup code</span>를 실행한다.

<br>

**위의 예에서 이 시퀀스를 설명해 보겠다.**

위의 `ChatRoom` 컴포넌트가 페이지에 추가되면 초기 `serverUrl` 및 `roomId`로 채팅방에 연결된다. 다시 렌더링한 결과 `serverUrl` 또는 `roomId`가 변경되면(ex: 사용자가 드롭다운에서 다른 채팅방을 선택하는 경우) Effect는 이전 채팅방과의 _연결을 끊고_ 다음 채팅방에 연결한다. `ChatRoom` 컴포넌트가 페이지에서 제거되면 Effect는 마지막으로 연결을 끊는다.

<br>

버그를 찾는 데 도움을 주기 위해 **개발 환경에서 React는 실제 setup 전에 setup 및 cleanup을 한 번 더 실행한다.** 이는 Effect의 로직이 올바르게 구현되었는지 확인하는 스트레스 테스트다. 이로 인해 눈에 보이는 문제가 발생하면 cleanup function에 일부 로직이 누락된 것이다. cleanup function은 setup function이 수행하던 작업을 중지하거나 취소해야 한다. 사용자 경험상 상용에서 setup이 한 번 호출되는 것과, 개발 환경에서 setup -> cleanup -> setup 순서로 호출되는 것을 구분할 수 없어야 한다. [일반적인 해결 방법](https://react-ko.dev/learn/synchronizing-with-effects#how-to-handle-the-effect-firing-twice-in-development)을 참고하라.

[모든 Effect를 독립적인 프로세스로 작성하고](https://react-ko.dev/learn/lifecycle-of-reactive-effects#each-effect-represents-a-separate-synchronization-process) [한 번에 하나의 setup/cleanup 주기만 생각하라.](https://react-ko.dev/learn/lifecycle-of-reactive-effects#thinking-from-the-effects-perspective) 컴포넌트가 mount, update, unmount 중 어느 단계에 있는지는 중요하지 않다. cleanup 로직이 setup 로직을 올바르게 "미러링"하고 있다면, 필요한 만큼 자주 setup과 cleanup을 실행하더라도 Effect는 탄력적으로 작동한다.

<br><br>

#### 3.1.1. 외부 시스템에 연결하는 예시

#### Example. 모달 제어하기

이 예시에서 외부 시스템은 브라우저 DOM이다. `ModalDialog` 컴포넌트는 `<dialog>` element를 렌더링한다. 이 컴포넌트는 Effect를 사용해 `isOpen` prop을 `showModal()` 및 `close()` 메서드 호출에 동기화한다.

```javascript
// App.js

import { useState } from "react";
import ModalDialog from "./ModalDialog.js";

export default function App() {
  const [show, setShow] = useState(false);
  return (
    <>
      <button onClick={() => setShow(true)}>Open dialog</button>
      <ModalDialog isOpen={show}>
        Hello there!
        <br />
        <button
          onClick={() => {
            setShow(false);
          }}
        >
          Close
        </button>
      </ModalDialog>
    </>
  );
}
```

```javascript
// ModalDialog.js

import { useEffect, useRef } from "react";

export default function ModalDialog({ isOpen, children }) {
  const ref = useRef();

  useEffect(() => {
    if (!isOpen) {
      return;
    }
    const dialog = ref.current;
    dialog.showModal();
    return () => {
      dialog.close();
    };
  }, [isOpen]);

  return <dialog ref={ref}>{children}</dialog>;
}
```

<img src="./image/useEffect_modal.gif"/>

<br><br>


