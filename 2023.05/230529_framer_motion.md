# framer motion

## framer motion이란?

- 리액트에서 애니메이션과 제스쳐를 쉽게 다룰 수 있도록 해주는 라이브러리
- animate props에 값을 세팅하면 CSS transitions를 자동생성하는 방법으로 애니메이션을 만들어줌
- drag나 hover 등의 제스쳐를 지원함
- 단일 애니메이션 prop으로 하위 트리까지 이어지는 애니메이션을 적용할 수 있음

## 설치 - 선언하기

`npm install framer-motion`
`import { motion } from 'framer-motion'`

```JSX
<motion.div animate={{ scale: 0.5 }} />
```

## 사용 방법

### motion components

- html 요소나 svg 요소에 대응할 수 있는 컴포넌트
  ```JSX
  <motion.div
  animate={{
      x: 0,
      backgroundColor: "#000",
      boxShadow: "10px 10px 0 rgba(0, 0, 0, 0.2)",
      position: "fixed",
      transitionEnd: {
        display: "none",
      },
    }}
  />
  ```
- 참고 : transform 속성으로 CSS 애니메이션을 구현하면 브라우저가 GPU를 활용하기 때문에 left 대신 x 옵션을 사용하는 것이 더 빠름

  ```JSX
  // GPU accelerated (fast)
  <motion.div style={{ x: 0 }} animate={{ x: 100 }} />

  // CPU drawing (slower)
  <motion.div style={{ left: 0 }} animate={{ left: 100 }} />
  ```

## Animation

```JSX
<motion.div animate={{ scale: 2 }} />
```

- animate prop는 값을 객체로 받고 이 값이 지정되면 첫 렌더링시에, 또는 변경되면 변경된 값으로 motion 컴포넌트를 애니메이팅 함
- 예시
  ```JSX
  Keyframes
  <motion.div
  animate={{
      scale: [1, 2, 2, 1, 1],
      rotate: [0, 0, 270, 270, 0],
      borderRadius: ["20%", "20%", "50%", "50%", "20%"],
  }}
  />
  ```
- 값을 array로 넣게 되면 순서대로 실행됨
- 기본적으로는 동일한 시간으로 실행되나 transition 프로퍼티를 조정해서 시간값을 수정 가능

## Variants

- variants props를 활용하면 선언적 방법으로 돔 전체에 전파되는 애니메이션을 만들 수 있음
- 예시 : animate가 open일 경우 motion.nav와 motion.ul의 variants 값 중 open값들을 실행

  ```JSX
  const [isOpen, setIsOpen] = useState(false)
  <motion.nav
  animate={isOpen ? "open" : "closed"}
  variants={{
      open: { opacity: 1, x: 0 },
      closed: { opacity: 0, x: "-100%" },
  }}

  > <Toggle onClick={() => setIsOpen(!isOpen)} />
  > <motion.ul variants={{

      open: { /* */ },
      closed: { /* */ },
      }}

  />
  </motion.nav>
  ```

## Gesture

- 드래그가 가능한 요소를 지정할 수 있음
- 드래그 가능한 영역을 ref를 넘겨주거나 top, left 등을 특정 값으로 넘겨서 지정할 수 있음

  ```JSX
  <motion.button
  whileHover={{ scale: 1.1 }}
  whileTap={{ scale: 0.9 }}
  />
  motion 컴포넌트는 whileHover이나 whileTap같은 제스처 헬퍼 props를 가지고 있다.

      Drag
      const dragAreaRef = useRef(null)
      <motion.div ref={dragAreaRef} />
      <motion.div drag dragConstraints={dragAreaRef} />

  ```

## 공식 사이트

- 이 외 자세한 사항은 framer motion 공식 사이트 참고
- https://www.framer.com/
