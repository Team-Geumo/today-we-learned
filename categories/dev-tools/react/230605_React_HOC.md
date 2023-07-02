# HOC

- 고차 컴포넌트(HOC, Higher Order Component)
- HOC는 컴포넌트를 인자로 받아 새로운 컴포넌트를 반환하는 함수
- 컴포넌트 로직을 재사용 하기 위한 방식
- HOC의 이름은 `with이름지정` 규칙을 따름
- ex) 리덕스 - `connect()` 함수 / 라우터 - `withRouter()`

<br>

## 1. HOC의 장점

- 반복적인 코드 재사용 용이

<br>

## 2. HOC의 단점

- 속성 값의 암묵적 전달. 예 : `redux-connect()` 사용 시 넘기지 않은 `this.props.dispatch`를 사용할 수 있는 점
- 동명의 props를 생성/사용할 때 충돌발생
  - 서로 다른 HOC에서 동일 props 이름 사용
  - InputCompo의 props와 HOC의 props에서 동일 이름 사용
  - ex: `redux-dispatch`를 사용, `withMyHOC-dispatch` 사용으로 충돌 => 마지막 값으로 덮어쓰기
- 의례적 절차 필요
  - 항상 함수로 감싸줘야 함
  - displayName 설정해야함(`recompose/getDisplayName` 패키지로 InputCompo의 displayName 불러와야 함)
  - 정적메서드 호출 설정해야함 (`hoist-non-react-statics` 패키지 사용해야 함)
  - typescript와 같은 정적타입언어를 사용할 때 타입 정의가 까다롭다

<br>

