# Built-in React Hooks

Hook을 사용하면 컴포넌트에서 다양한 React 기능을 사용할 수 있다. Built-in Hook을 사용하거나 조합하여 자신만의 hoook을 만들 수도 있다. 이 페이지에는 모든 React built-in hook이 나열되어 있다.

<br><br>

## 1. State Hooks

*State*를 사용하면 컴포넌트가 [사용자 입력과 같은 정보를 기억할 수 있다.](https://react-ko.dev/learn/state-a-components-memory) 예를 들어, form 컴포넌트는 state를 사용하여 입력 값을 저장하고, 이미지 갤러리 컴포넌트는 state를 사용하여 선택한 이미지의 인덱스를 저장할 수 있다.

컴포넌트에 state를 추가하려면 다음 hook 중 하나를 사용한다.

- [`useState`](https://react-ko.dev/reference/react/useState)는 직접 업데이트할 수 있는 state 변수를 선언한다.
- [`useReducer`](https://react-ko.dev/reference/react/useReducer)는 [reducer function](https://react-ko.dev/learn/extracting-state-logic-into-a-reducer) 안에 업데이트 로직이 있는 state 변수를 선언한다.

```javascript
function ImageGallery() {
  const [index, setIndex] = useState(0);
  // ...
}
```

<br><br>

## 2. Context Hooks

*context*를 사용하면 컴포넌트가 [prop으로 전달하지 않고 멀리 떨어진 부모로부터 정보를 받을 수 있다.](https://react-ko.dev/learn/passing-props-to-a-component) 예를 들어, 앱의 최상위 컴포넌트는 아무리 깊이 있더라도 현재 UI 테마를 아래의 모든 컴포넌트에 전달할 수 있다.

- `useContext`는 context 를 읽고 구독한다.

```javascript
function Button() {
  const theme = useContext(ThemeContext);
  // ...
}
```

<br><br>

## 3. Ref Hooks

*ref*는 컴포넌트가 DOM 노드나 timeout ID와 같이 [렌더링에 사용되지 않는 일부 정보를 보유할 수 있게](https://react-ko.dev/learn/referencing-values-with-refs) 해준다. state와 달리 ref를 업데이트해도 컴포넌트가 다시 렌더링되지는 않는다. ref는 React 패러다임에서 "탈출구"다. 브라우저 빌트인 API와 같이 React가 아닌 시스템에서 작업해야 할 때 유용하다.

- `useRef`는 ref를 선언한다. 어떤 값을 담을 수 있지만, 대부분 DOM 노드를 담는 데 사용된다.
- `useImperativeHandle`을 사용하면 컴포넌트가 노출하는 ref를 사용자가 직접 정의할 수 있다. 이 함수는 거의 사용되지 않는다.

```javascript
function Form() {
  const imputRef = useRef(null);
  // ...
}
```

<br><br>

## 4. Effect Hooks

*Effect*는 컴포넌트가 [외부 시스템에 연결하고 동기화할 수 있도록](https://react-ko.dev/learn/synchronizing-with-effects) 한다. 여기에는 네트워크, 브라우저 DOM, 애니메이션, 다른 UI 라이브러리를 사용하여 작성된 위젯 및 기타 non-React code를 처리하는 것이 포함된다.

- `useEffect`는 컴포넌트를 외부 시스템에 연결한다.

```javascript
function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);
  // ...
}
```

Effect는 React 패러다임에서 "탈출구"다. 애플리케이션의 데이터 흐름을 조율하기 위해 Effect를 사용하지 마라. 외부 시스템과 상호작용하지 않는다면, Effect가 필요하지 않을 수도 있다.

사용 타이밍에 차이가 있지만 특수한 경우에 사용되는 두 가지 `useEffect` 변형이 있다.

- 브라우저가 화면을 다시 그리기 전에 `useLayoutEffect`가 실행된다. 여기에서 레이아웃을 측정할 수 있다.
- React가 DOM을 변경하기 전에 `useInsertionEffect`가 실행된다. 라이브러리는 여기에 동적 CSS를 삽입할 수 있다.

<br><br>

## 5. Performance Hooks

리렌더링 성능을 최적화하는 일반적인 방법은 불필요한 작업을 건너뛰는 것이다. 예를 들어, 캐시된 계산을 재사용하거나 이전 렌더링 이후 데이터가 변경되지 않은 경우 리렌더링을 건너뛰도록 React에 지시할 수 있다.

계산과 불필요한 리렌더링을 건너뛰려면 다음 hook 중 하나를 사용하라.

- `useMemo`를 사용하면 비용이 많이 드는 계산 결과를 캐시할 수 있다.
- `useCallback`을 사용하면 함수 정의를 캐시한 후 최적화된 컴포넌트를 전달할 수 있다.

```javascript
function TodoList({ todos, tab, theme }) {
  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);
  // ...
}
```

화면이 실제로 업데이트되어야 하기 때문에 렌더링을 건너뛸 수 없는 경우도 있다. 이 경우 입력과 같이 동기화되어야 하는 차단 업데이트와 차트 업데이트와 같이 사용자 인터페이스를 차단할 필요가 없는 비차단 업데이트를 분리하여 성능을 향상시킬 수 있다.

렌더링 우선순위를 지정하려면 다음 hook 중 하나를 사용한다.

- `useTransition`을 사용하면 state 전환을 비차단 state로 표시하고 다른 업데이트가 이를 중단하도록 허용할 수 있다.
- `useDeferredValue`를 사용하면 UI의 중요하지 않은 부분의 업데이트를 연기하고 다른 부분이 먼저 업데이트되도록 할 수 있다.

<br><br>

## 6. Other Hooks

- 아래의 hook은 대부분 라이브러리 작성자에게 유용하며 애플리케이션 코드에서는 일반적으로 사용되지 않는다.

- `useDebugValue`를 사용하면 커스텀 훅에 대해 React 개발자 도구가 표시하는 레이블을 사용자가 직접 정의할 수 있다.
- `useId`는 컴포넌트가 자신과 고유 ID를 연결할 수 있게 해준다. 일반적으로 접근성 API와 함께 사용된다.
- `useSyncExternalStore`는 컴포넌트가 외부 스토어에 구독하도록 한다.

