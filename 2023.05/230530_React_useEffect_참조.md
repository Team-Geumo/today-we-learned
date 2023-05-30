# useEffect

## 1. Overview

- `useEffect`는 컴포넌트를 외부 시스템과 동기화할 수 있는 React Hook이다.

```javascript
useEffect(setup, dependencies?)
```

<br><br>

## 2. Reference

### `useEffect(setup, dependencies?)`

컴포넌트의 최상위 레벨에서 `useEffect`를 호출하여 Effect를 선언한다.

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

<br>

### 2.1. Parameters

- `setup` : Effect의 로직이 포함된 함수다. setup 함수는 선택적으로 클린업 함수를 반환할 수도 있다. React는 컴포넌트다 DOM에 추가되면 셋업 함수를 실행한다. 의존성이 변경되어 다시 렌더링할 때마다 React는 (클린업 함수가 있는 경우) 먼저 이전 값으로 클린업 함수를 실행한 다음, 새 값으로 setup 함수를 실행한다. 컴포넌트가 DOM에서 제거되면, React는 마지막으로 클린업 함수를 실행한다.

- optional `dependencies` : setup 코드 내에서 참조된 모든 반응형 값의 목록이다. 반응형 값은 props, state, 컴포넌트 본문 내부에서 직접 선언한 모든 변수와 함수를 포함한다. [React용으로 구성된](https://react-ko.dev/learn/editor-setup#linting) linter는 모든 반응형 값이 의존성에 잘 지정되었는지 확인한다. React는 각 의존성에 대해 [`Object.is`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is)로 이전 값과 비교한다. 의존성을 전혀 지정하지 않으면 컴포넌트를 다시 렌더링할 때마다 Effect가 다시 실행된다. [의존성 배열을 전달할 때, 빈 배열을 전달할 때, 그리고 의존성을 전혀 전달하지 않을 때의 차이를 확인해보라.](https://react-ko.dev/reference/react/useEffect#examples-dependencies)

<br>

### 2.2. Returns

`useEffect`는 `undefined`를 반환한다.

<br>

### 2.3. Caveats

- `useEffect`는 hook이므로 **컴포넌트의 최상위 레벨 또는 자체 hook**에서만 호출할 수 있다. 반복문이나 조건문 내부에서는 호출할 수 없다. 필요한 경우 새 컴포넌트를 추출하고 state를 그 안으로 옮겨라

- **외부 시스템과 동기화하려는 목적이 아니라면** [Effect가 필요하지 않을지도 모른다.](https://react-ko.dev/learn/you-might-not-need-an-effect)

- Strict 모드가 켜져있으면 React는 첫 번째 실제 setup 전에 **개발 전용의 setup + cleanup cycle**을 한 번 더 실핸한다. 이는 cleanup 로직을 "미러링"하고 setup이 수행 중인 모든 작업을 중지하거나 최소하는지를 확인하는 스트레스 테스트이다. 문제가 발생하면 [cleanup function을 구현해야 한다.](https://react-ko.dev/learn/synchronizing-with-effects#how-to-handle-the-effect-firing-twice-in-development)

- 의존성 중 일부가 컴포넌트 내부에 정의된 객체 또는 함수인 경우 **Effect가 필요 이상으로 자주 다시 실행될 위험이 있다.** 이 문제를 해결하려면 불필요한 [객체](https://react-ko.dev/reference/react/useEffect#removing-unnecessary-object-dependencies) 및 [함수](https://react-ko.dev/reference/react/useEffect#removing-unnecessary-function-dependencies) 의존성을 제거하라. 혹은 Effect 외부에서 [state 업데이트 추출](https://react-ko.dev/reference/react/useEffect#updating-state-based-on-previous-state-from-an-effect) 및 [비반응형 로직](https://react-ko.dev/reference/react/useEffect#reading-the-latest-props-and-state-from-an-effect)을 제거할 수도 있다.

- Effect가 상호작용(ex: click)으로 인한 것이 아니라면, **React는 브라우저각 Effect를 실행하기 전에 업데이트된 화면을 먼저 그리도록 한다.** Effect가 시각적인 작업(ex: tooltip 위치 지정)을 하고 있고, 지연이 눈에 띄는 경우(ex: 깜빡임), `useEffect`를 [`useLayoutEffect`](https://react-ko.dev/reference/react/useLayoutEffect)로 대체해야 한다.

- Effects는 **클라이언트에서만 실행된다.** 서버 렌더링 중에는 실행되지 않는다.



