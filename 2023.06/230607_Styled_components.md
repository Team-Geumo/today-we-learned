# Styled Components 사용하기

## 1. 개요

React, Vue, Angular와 같은 라이브러리, 프레임워크가 인기를 끌면서 재활용 가능한 컴포넌트 기반 개발이 주류가 되고 있다. 여러 컴포넌트로 분리하고, 각 컴포넌트에 HTML, CSS, JavaScript를 모두 담는 코드를 많이 사용하고 있다. React는 이미 JSX를 통해 HTML을 포함하고 있고, Styled Components 라이브러리를 사용하여 CSS를 JavaScript에 삽입할 수 있다.

<br>

## 2. 설치

`npm install --save styled-components`

<br>

## 3. Styled-Components

- CSS in JavaScript 기술로, JavaScript 내에 CSS를 작성하는 라이브러리
- 스타일 정의를 CSS 파일이 아닌 JavaScript로 작성된 **컴포넌트**에 바로 삽입하는 스타일 기법
- 클래스명을 해시값으로 자동 생성하고, 클래스명 오염을 방지할 수 있음
- 자바스크립트의 동적인 값들을 온전하게 사용이 가능

<br>

## 4. 사용법

### 4.1. styled-components 작성 방법

```javascript
// Getting Started

import styled from "styled-components";

return (
  <Wrapper>
    <Title>Hello World!</Title>
  </Wrapper>
);

const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
`;

const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;
```

- 코드 가독성을 위해서 컴포넌트를 먼저 선언하고 하단에 styled-components 작성
- Template Literal을 사용하여 작성하며, `const 컴포넌트명 = styled.태그명`으로 이루어짐

<br>

### 4.2.1. styled-components에 props 사용 및 조건식 사용하기

```javascript
// Adapting based on props

return (
  <div>
    <Button>Normal</Button>
    <Button width="100">Primary</Button>
  </div>
);

const Button = styled.button`
  background: ${(props) => (props.width < 200 ? "palevioletred" : "white")};
  color: ${(props) => (props.primary ? "white" : "palevioletred")};
  font-size: 1em;
  margin: 1em;
`;
```

- Button의 props인 width가 200보다 작으면 "palevioletred"색을, 크다면 "white"색을 배경으로 지정
- 변수에 따라서 스타일을 바꿀 수 있다는 장점 있음
- `&&`, `||` 연산자를 이용해서 스타일을 적용 가능

<br>

### 4.2.2. 심화

```javascript
return (
  <ExampleWrap active={email.length}>
    <Button>Hello</Button>
    <NewButton color="blue">Im new Button</NewButton>
  </ExampleWrap>
);

const ExampleWrap = styled.div`
  background: ${({ active }) => {
    if (active) {
      return "white";
    }
    return "#eee";
  }};
  color: black;
`;

const Button = styled.button`
  width: 200px;
  padding: 30px;
`;
```

<br>

### 4.3. 생성한 styled-component 재사용하기

```javascript
// Extending styles

return (
  <div>
    <Button>Normal Button</Button>
    <TomatoAnchorButton>Tomato Button</TomatoAnchorButton>
  </div>
);

const Button = styled.div`
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

// Button의 속성을 상속 받아 새로운 anchor 태그 생성
const TomatoAnchorButton = styled(Button.withComponent("a"))`
  color: tomato;
  border-color: tomato;
`;
```

- 스타일 상속 : `const 컴포넌트명 = styled(스타일컴포넌트명)`

<br>

### 4.4. Mixin css props

```javascript
import styled, { css } from "styled-components"; // css 사용!

const FlexCenter = css`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const FlexBox = div`
${FlexCenter}`;

const RingVariant = (radius, stroke = "10") => css`
  position: absolute;
  border-radius: 50%;
  height: ${radius * 2}px;
  width: ${radius * 2}px;
  border: ${stroke}px soloid rgba(0, 0, 0, 0.5);
`;
```

- styled-components는 자주 사용하는 css를 관리하기 위해 css props를 사용
