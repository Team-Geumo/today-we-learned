# useMemo vs. useCallback

```
✅ useMemo와 useCallback은 React 애플리케이션에서 성능 최적화를 위해서 사용되는 Hook입니다.

useMemo는 특정 결과 값을 캐시하여 재사용하고자 할 때 사용됩니다.
이는 함수의 결과를 기억하고, 종속성(dependency) 배열에 있는 값들이 변경되었을 때만 결과를 다시 계산합니다.

반면, useCallback은 특정함수를 메모이제이션하여 새로운 함수 인스턴스를 생성하지 않고 재사용하고자 할 때 사용됩니다.
이는 종속성(dependency) 배열에 있는 값들 중 하나라도 변경되면 해당 함수를 다시 생성하며, 변경이 없을 경우 이전에 생성된 함수를 계속 사용합니다.
```

<br><br>

## 1. Memoization

- 컴퓨터가 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산을 하지 않도록 하며, 속도를 높이는 기술
- **애플리케이션의 최적화를 위해 사용**

<br><br>

## 2. useMemo

> **useMemo is a React Hook that lets you cache the result of a calculation between re-renders.**

```javascript
const cachedValue = useMemo(calculateValue, dependencies);
```

<br>

### 2.1. Reference

```javascript
import { useMemo } from "react";

function TodoList({ todos, tab }) {
  const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);
  // ...
}
```

- 컴포넌트의 최상위 레벨에서 `useMemo`를 호출하여 재랜더링 중에 계산 결과를 캐시할 수 있음

<br>

### 2.2. Parameters

- **`calculateValue`**
  - 캐시하려는 값을 계산하는 함수
  - pure해야 하며 argument(인수)를 받지 않아야 하며, 모든 유형의 값을 반환해야 함
  - React는 초기 렌더링 중에 함수를 호출함
  - 다음 render에서는 `dependencies`가 마지막 render 이후로 변경되지 않았다면 동일한 값을 반환함
  - 그렇지 않으면 `calculateValue`를 호출하고 결과를 반환하여 나중에 재사용할 수 있도록 저장함
- **`dependencies`**
  - `calculateValue` 코드 내에서 참조된 모든 reactive value의 배열
  - reactive value에는 props, state 및 component body에서 직접 선언된 모든 변수와 함수가 포함됨
  - linter(ex: ESLint)가 React용으로 구성된 경우, linter는 모든 reactive value이 올바르게 `dependency`로 지정되었는지 확인함
  - `dependencies` 배열은 `[dep1, dep2, dep3]`와 같이 inline으로 작성되어야 하며, 항상 일정한 항목 수를 가져야 함
  - React는 각 `dependency`를 이전 값과 `Object.is` 비교(두 값이 같은 값인지 비교)를 사용하여 비교함

<br>

### 2.3. Returns

- 초기 렌더링에서 `useMemo`는 인수 없이 `calculateValue`를 호출한 결과를 반환함
- 다음 렌더에서는 `dependencies`가 변경되지 않았다면 이미 저장된 값을 반환하거나, 변경되었다면 `calculateValue`를 다시 호출하고 `calculateValue`의 결과를 반환함

<br>

### 2.4. 주의 사항

- Strict Mode에서는 React가 예상치 못한 부작용을 찾아 도울 목적으로 **`calculation function`을 두 번 호출**할 것임
  - 이는 개발 중에만 발생하며 프로덕션에는 영향을 미치지 않음
  - `calculation function`이 pure하다면, 이는 로직에 영향을 미치지 않음
  - 두 호출 중 하나의 결과는 무시됨

<br><br>

## 3. useCallback

> **useCallback is a React Hook that lets you cache a function definition between re-renders.**

```javascript
const cachedFn = useCallback(fn, dependencies);
```

<br>

### 3.1. Reference

```javascript
import { useCallback } from 'react';

export default function ProductPage({ productId, referrer, theme }) {
  const handleSubmit = useCallback((orderDetails) => {
    post('/product/' + productId + '/buy', {
      referrer,
      orderDetails,
    });
  }, [productId, referrer]);
```

- 컴포넌트의 최상위 레벨에서 `useCallback`을 호출하여 함수 정의를 재렌더링 중에 캐시할 수 있음

<br>

### 3.2. Parameters

- **`fn`**
  - 캐시하려는 함수 값
  - 어떤 인수(argument)도 취할 수 있으며 어떤 값을 반환할 수 있음
  - **React는 초기 렌더링 중에 함수를 반환함(호출❌)**
  - 다음 render에서는 `dependencies`가 마지막 render 이후로 변경되지 않았다면 동일한 함수 반환
  - 그렇지 않으면 현재 render 중에 전달한 함수를 반환하고 나중에 재사용할 수 있도록 저장함
  - React는 함수를 호출하지 않음
  - 함수는 호출 여부와 호출 시기를 사용자가 결정할 수 있도록 반환됨
- **`dependencies`**
  - `fn` 코드 내에서 참조된 모든 reactive value의 배열
  - reactive value에는 props와 state, 컴포넌트 body에서 직접 선언된 모든 변수와 함수가 포함됨
  - linter가 React용으로 구성된 경우, 모든 reactive value가 올바르게 `dependency`로 지정되었는지 확인함
  - `dependencies` 배열은 `[dep1, dep2, dep3]`와 같이 인라인으로 작성되어야 하며, 항상 일정한 항목 수를 가져야 함
  - React는 `dependendy`를 이전 값과 `Object.is` 비교를 사용하여 비교함

<br>

### 3.3. Returns

- 초기 렌더링에서 `useCallback`은 전달한 `fn` 함수를 반환함
- 다음 render에서는 `dependencies`가 변경되지 않았다면 이미 저장된 `fn` 함수를 반환하거나, 변경되었다면 현재 render 중에 전달한 `fn`함수를 반환함

<br><br>

## 4. useMemo, useCallback 공통 주의 사항

- `useMemo`와 `useCallback`은 Hook이므로 **컴포넌트의 최상위 레벨**이나 사용자 고유의 Hooks에서만 호출 가능
  - 루프나 조건문 안에서 호출 불가
    - 필요하다면 새 컴포넌트를 추출하고 `stats`를 옮겨야 함
- React는 **캐시된 값을 특별한 이유가 없으면 throw away하지 않음**
  - 예를 들어 개발 중에 React는 컴포넌트 파일을 편집할 때 캐시를 throw away함
  - 개발 및 프로덕션 모두에서 React는 초기 마운트 중에 컴포넌트가 중단되면 캐시를 throw away함
  - `useMemo`와 `useCallback`을 성능 최적화 수단으로만 사용하는 경우에는 괜찮지만, 그렇지 않으면 상태 변수나 `ref`가 더 적절할 수 있음

<br><br>

## 5. 참고

[useMemo – React 공식문서](https://react.dev/reference/react/useMemo)

[useCallback – React 공식문서](https://react.dev/reference/react/useCallback)
