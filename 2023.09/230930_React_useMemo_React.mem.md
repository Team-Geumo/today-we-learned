# React.memo와 useMemo

## React.memo

- React.memo는 Higher-Order Components(HOC)이다.

- Higher-Order Components(HOC)란 컴포넌트를 인자로 받아 새로운 컴포넌트롤 다시 return해주는 함수이다.

```jsx
const NewComponent = higherOrderComponent(WrappedComponent);
```

- 일반 컴포넌트는 인자로 받은 props를 UI에 활용하는 반면에, higher-order component는 인자로 받은 컴포넌트를 새로운 별도의 컴포넌트로 만든다. HOC는 리액트의 API가 아니라 리액트가 컴포넌트를 구성하는데 있어서의 일종의 패턴이라고 보면된다.

- React.memo의 사용법은 다음과 같다.

```jsx
const MyComponent = React.memo((props) => {
  return /*컴포넌트 렌더링 코드*/;
});
```

- 만약 컴포넌트가 같은 props를 받을 때 같은 결과를 렌더링한다면 React.memo를 사용하여 불필요한 컴포넌트 렌더링을 방지할 수 있다.

- 즉, 컴포넌트에 같은 props가 들어온다면 리액트는 컴포넌트 렌더링 과정을 스킵하고 마지막에 렌더링된 결과를 재사용한다.

- React.memo는 오직 props가 변경됐는지 아닌지만 체크한다. 만약 React.memo에 감싸진 함수형 컴포넌트가 함수 내부에서 useState나 useContext같은 훅을 사용하고 있다면, state나 context가 변경될 때마다 리렌더링된다.

- 기본적으로 props로 들어온 object는 shallow compare로 비교한다. 즉, props로 들어온 number, string과 같은 scarlar 값은 실제 값이 동일한가를 비교하지만, object의 경우 scarlar 값과 달리 같은 값을 'reference(참조)'하고 있는지를 비교 한다.

- 만약 비교방식을 커스텀하고 싶다면 아래 코드처럼 비교함수를 React.memo의 두번째 인자로 넣어주면 된다.

```jsx
function MyComponent(props) {
  /* 컴포넌트 렌더링 코드 */
}
function areEqual(prevProps, nextProps) {
  /*
만약 전달되는 nextProps가 prevProps와 같다면 true를 반환, 같지 않다면 false를 반환
*/
}

export default React.memo(MyComponent, areEqual);
```

## useMemo

- useMemo는 메모이즈된 값을 return하는 hook이다.

- 인자로 함수와 의존 값(dependencies)을 받는다. useMemo는 두번째 인자로 준 의존 인자 중에 하나라도 변경되면 값을 재 계산한다. 이를 통해 매 렌더시마다 소요되는 불필요한 계산을 피할 수 있다. 만약 dependencies 인자로 아무것도 전달되지 않는다면, 렌더시마다 항상 값을 새롭게 계산하여 return한다.

- 아래의 코드는 a, b값이 변할 때만 첫번째 인자로 들어온 함수가 실행되어 재계산이 되고, 그렇지 않은 경우에는 메모이즈된 값을 return한다.

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

## 공통점

- React.memo와 useMemo 모두 props가 변하지 않으면(이전 props와 동일하면) 인자로 넘긴 함수는 재실행되지 않고, 이전의 메모이즈된 결과를 반환한다는 점에서 공통점이있다.

- 아래 React.memo와 useMemo를 사용한 코드를 보면 두가지 코드는 props.name의 값이 변하지 않는다면 리렌더링 되지 않고 이전의 값을 반환한다는 점에서 동일하게 동작한다.

```jsx
/*별도로 두번째 인자를 넘기지 않을 경우 props가 변하지 않는다면 재렌더링 되지 않음*/
const NameTag = React.memo((props) => <div>{props.name}</div>);

/*만약 두번째 인자로 특정 props.name값이 같지 않을때만 재렌더링 하도록 커스텀 비교 함수를 넣어주고 싶을 때*/
const NameTag = React.memo(
  (props) => <div>{props.name}</div>,
  (prevProps, nextProps) => prevProps.name === nextProps.name,
);
function NameTag(props) {
  return useMemo(() => <div>{props.name}</div>, [props.name]);
}
```

## 차이점

1. React.memo는 HOC, useMemo는 hook이다.

2. React.memo는 HOC이기 때문에 클래스형 컴포넌트, 함수형 컴포넌트 모두 사용 가능하지만, useMemo는 hook이기 때문에 오직 함수형 컴포넌트 안에서만 사용 가능하다.
