# React useCallback

## useCallback은?

- 특정 함수를 새로 만들지 않고 재사용하고 싶을 때 사용하는 hook
- React 공식 문서에서 말하는 useCallback

  - 메모제이션된 함수를 반한하는 하는 함수입니다.

  - 인라인 콜백과 그것의 의존성 값의 배열을 전달하세요. useCallback은 콜백의 메모이제이션된 버전을 반환할 것입니다. 그 메모이제이션된 버전은 콜백의 의존성이 변경되었을 때에만 변경됩니다. 이것은, 불필요한 렌더링을 방지하기 위해 (예로 shouldComponentUpdate를 사용하여) 참조의 동일성에 의존적인 최적화된 자식 컴포넌트에 콜백을 전달할 때 유용합니다.

## useCallback을 사용하는 이유

- 현재 하위 컴포넌트에 전달하는 콜백 함수가 inline 함수로 사용되거나, 컴포넌트 내에서 함수를 생성하고 있다면 새로운 함수가 만들어지게 됨
- 한 번 만든 함수를 재 사용하고, 필요할 때만 재 생성 하는것은 중요함
- useCallback과 React.memo를 함께 사용한다면 컴포넌트를 최적화 할 수 있음
- 코드 예시 : useCallback 사용 전

  ```JSX
  import React, { useState } from "react";

  const CounterButton = function ({ onClicks, count }) {
  console.log("카운터 버튼 렌더링");
  return <button onClick={onClicks}>{count.num}</button>;
  };

  export default function Counter() {
  const [count1, setCount1] = useState({ num: 0 });

  const increament1 = () => {
  setCount1({ num: count1.num + 1 });
  };

  const [count2, setCount2] = useState({ num: 0 });

  const increament2 = () => {
  setCount2({ num: count2.num + 1 });
  };

  return (

  <div className="App">
  <div>{count1.num}</div>
  <div>{count2.num}</div>
  <CounterButton onClicks={increament1} count={count1} />
  <CounterButton onClicks={increament2} count={count2} />
  </div>
  );
  }
  ```

- 버튼을 클릭하면 CounterButton 컴포넌트가 2번 렌더링 됨 :
- 참고 : React가 리렌더링을 하는 조건

  - props가 변경되었을 때
  - state가 변경되었을 때
  - 부모 컴포넌트가 렌더링되었을 때
  - forceUpdate() 를 실행하였을 때
    다음 예제에서는 props, state,부모 컴포넌트의 변화가 있었기에 React가 리렌더링 되게 됩니다.

- 컴포넌트가 2번 렌더링 되는 과정

  1. 첫 렌더링이 되고 increament함수와 count state가 생성되어 렌더링 됨
  2. 버튼을 클릭하게 되면 increament함수가 작동하게 되고 setState로 인해 state가 변경됨
  3. state가 변경됐으니, 부모 컴포넌트는 리렌더링이 되게 되고, 변경된 props를 내려주게 됨
  4. 자식 컴포넌트는 props를 받아 다시 뿌려주게 됨

- 코드 예시 : useCallback 사용

```JSX
 //수정 전
 import {useCallback} from 'react';
 const increament1 = () => {
 setCount1({ num: count1.num + 1 });
 };
 //수정 후
 const increament1 = useCallback(() => {
 setCount1({ num: count1.num + 1 });
 },[count1]);
```

## useCallback 사용 방법

- `useCallback(fn, deps)`
- useCallback의 첫번째 인자로는 인라인 콜백과 의존성 값의 배열을 받음
- 의존성 배열인 deps에 변경을 감지해야할 값을 넣어주게 되면 count1이 변경될 때마다 콜백 함수를 새로 생성함
