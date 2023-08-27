# styled-components에서의 animation

## 1. styled-components 안에서 animation 주는 방법

- helper function을 import 하기
  ex) `keyframes`

  ```javascript
  // App.js

  import styled, { keyframes } from "styled-components";

  const Wrapper = styled.div`
    display: flex;
  `;

  const rotationAnimation = keyframes`
    0% { 
      transform: rotate(0deg);
      border-radius: 0px;
    } 
    50% {
      border-radius: 100px;
    }
    100% {
      transform: rotate(365deg);
      border-radius: 0px;
    }
  `;

  const Box = styled.div`
    height: 200px;
    width: 200px;
    background-color: tomato;
    animation: ${rotationAnimation} 1s linear infinite;
  `;

  function App() {
    return (
      <Wrapper>
        <Box />
      </Wrapper>
    );
  }

  export default App;
  ```

  - 회전하면서 사각형이었다가 동그라미가 되는 animation

<br>

## 2. 모든 component에 styled-components 처리 하지 않아도 됨

- components만 `styled` 처리하고 다른 건 `target` 처리 가능

  ```javascript
  // App.js

  import styled, { keyframes } from "styled-components";

  const Wrapper = styled.div`
    display: flex;
  `;

  const rotationAnimation = keyframes`
    0% { 
      transform: rotate(0deg);
      border-radius: 0px;
    } 
    50% {
      border-radius: 100px;
    }
    100% {
      transform: rotate(365deg);
      border-radius: 0px;
    }
  `;

  const Box = styled.div`
    height: 200px;
    width: 200px;
    background-color: tomato;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: ${rotationAnimation} 1s linear infinite;
    span {
      font-size: 36px;
      /* span: hover  와 동일 */
      &:hover {
        font-size: 48px;
      }
      /* span: acitve 와 동일 */
      /* active: 클릭하고 있을 때 */
      &:active {
        opacity: 0;
      }
    }
  `;

  function App() {
    return (
      <Wrapper>
        <Box>
          {/* 아래 이모지는 styled compoentns 안에 있지 X */}
          <span>🤩</span>
        </Box>
      </Wrapper>
    );
  }

  export default App;
  ```

<br>

### 3. styled-components 안의 element 선택하는 벙법

- 태그명에 의존하지 않는 방법

  - **styled component 자체를 target 가능**

  ```javascript
  import styled, { keyframes } from "styled-components";

  const Wrapper = styled.div`
    display: flex;
  `;

  const rotationAnimation = keyframes`
    // ...
  `;

  const Emoji = styled.span`
    font-size: 36px;
  `;

  const Box = styled.div`
    // ...
    animation: ${rotationAnimation} 1s linear infinite;
    /* Emoji target 하고 있음 */
    ${Emoji}:hover {
      font-size: 98px;
    }
  `;

  function App() {
    return (
      <Wrapper>
        <Box>
          {/* Emoji가 span이든 p이든 상관X */}
          <Emoji as="p">🤩</Emoji>
        </Box>
        {/* Box 밖에 있기 때문에 hover했을 떄 조건문 성립X */}
        <Emoji as="p">🤩</Emoji>
      </Wrapper>
    );
  }

  export default App;
  ```
