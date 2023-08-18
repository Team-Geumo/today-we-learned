# React useContext

## useContext란?

컴포넌트에서 context를 전달하고 사용하는 React Hook

## useContext 사용 방법

1. `creactContext()`로 context 생성
2. 생성한 context의 `Provider`를 사용해 context를 전달할 컴포넌트를 감싸줌
3. 하위 컴포넌트에서 `useContext()`를 사용해 context 가져오기

- 주의 : `useContext()`는 항상 호출하는 컴포넌트의 상위에서 가장 가까운 공급자를 찾음

```jsx
import { createContext, useContext } from 'react';

// createContext()로 context 생성
const ThemeContext = createContext(null);

export default function MyApp() {
  return (
    // Provider로 컴포넌트 감싸기
    <ThemeContext.Provider value="dark">
      <Form />
    </ThemeContext.Provider>
  );
}

function Form() {
  return (
    <Panel title="Welcome">
      <Button>Sign up</Button>
      <Button>Log in</Button>
    </Panel>
  );
}

function Panel({ title, children }) {
  // useContext()로 context 가져오기
  const theme = useContext(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      <h1>{title}</h1>
      {children}
    </section>
  );
}

function Button({ children }) {
  // useContext()로 context 가져오기
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return <button className={className}>{children}</button>;
}
```
