# React svg 색상 변경하기

## 색상 변경 과정

### 1. React Component로 불러오기

```tsx
import { ReactComponent as Logo } from 'assets/images/logo.svg';
```

### 2. 원본 svg 파일의 fill 속성 변경하기

- `<path>`의 `fill="current"`로 변경
- 외부에서 지정하는 색상이 적용됨

```tsx
...
<path d="..." fill="current"/>
...
```

### 3. svg를 사용하는 컴포넌트에서 사용, 색상 지정

```tsx
<Logo fill="#ffffff" />
```

### 4. 만약 자식 컴포넌트에 넘겨준다면 : 타입 선언

- `ComponentType`으로 선언

```tsx
import React, { ComponentType } from 'react';
```

## 전체 코드

```tsx
import React, { ComponentType } from 'react';
import { ReactComponent as Logo } from 'assets/images/logo.svg';

function IconButton( Icon : ComponentType ) {
  return (
    <button>
      <Icon />
    </button>
  );
}

function App() {
  return (
    <div>
      <IconButton Icon={Logo}>
    </div>
  );
}
```
