# async/await란?

```
✅ async/await는 ES8에 도입된 문법으로서, 비동기적인 작업을 수행할 때 Promise를 더 쉽고 간결하게 사용할 수 있게 해줍니다. 이를 통해 비동기 코드를 동기식으로 표현할 수 있으며, try/catch 문을 사용하여 에러 처리가 가능하고, Promise 객체를 반환합니다.
```

<br>

## 1. JavaScript 비동기 처리 3가지 방식

- 비동기 처리는 백그라운드로 동작하기 때문에 그 결과가 언제 반환될지 알 수 없어, 완료되면 결과를 받아 처리하기 위해 사용되는 대표적인 방법으로 **콜백 함수(Callback)** 와 이를 개선한 **프로미스 객체(Promise)** 가 있음
- 하지만 서비스 규모가 커질수록 코드가 복잡해짐에 따라 코드를 중첩해서 사용하다가 가독성이 떨어지고 유지보수가 어려워지는 상황이 발생하게 되는데, 이를 **Callback Hell**, **Promise Hell**이라고 부름
  ```jsx
  // Callback Hell -> 보기가 엉성함
  getData (function (x) {
    getMoreData (x, function (y) {
      getMoreData (y, function (z) {
        ...
      });
    });
  });
  ```
  ```jsx
  // Promise Hell -> 구현하고자 하는 의도 파악하기 힘듦
  fetch("https://example.com/api")
    .then((response) => response.json())
    .then((data) => fetch(`https://example.com/api/${data.id}`))
    .then((response) => response.json())
    .then((data) => fetch(`https://example.com/api/${data.id}/details`))
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
  ```
- 자바스크립트 async/await는 이런 문제를 해결하기 위해 탄생
- 문법에 있어서도 훨씬 단순해져 가독성과 유지보수성을 향상시켜줌
  ```jsx
  async function getData() {
    const response = await fetch("https://example.com/api");
    const data = await response.json();
    const response2 = await fetch(`https://example.com/api/${data.id}`);
    const data2 = await response2.json();
    const response3 = await fetch(`https://example.com/api/${data.id}/details`);
    const data3 = await response3.json();
    console.log(data3);
  }

  getData();
  ```

<br><br>

## 2. async / await

- ES2017에 도입된 문법
- Promise 로직을 더 쉽고 간결하게 사용할 수 있게 해줌
- **Promise를 대체하기 위한 기능이 아님**
  - 내부적으로 여전히 Promise를 사용해서 비동기를 처리
  - 단지 코드 작성 부분을 프로그래머가 유지보수하기 편하게 **보이는 문법만 다르게 해줄 뿐**임

<br><br>

## 3. async / wait 기본 문법

```jsx
async function 함수명() {
  await 비동기_처리_메소드_이름();
}
```

- 함수의 앞에 `async` 예약어 붙임
- 함수의 내부 로직 중 HTTP 통신을 하는 비동기 처리 코드 앞에 `await` 붙임
  - 비동기 처리 메서드가 꼭 프로미스 객체를 반환해야 `await`가 의도대로 동작함
  - 일반적으로 `await` 의 대상이 되는 비동기 처리 코드는 `axios` 등 프로미스를 반환하는 API 호출 함수

<br>

### 3.1. async

- function 앞에 `async`를 붙이면 해당 함수는 항상 프로미스 반환
  - Promise가 아닌 값을 반환하더라도 이행상태의 Promise로 값을 감싸 이행된 프로미스가 반환되도록 함
- 화살표 함수, 함수 표현식으로도 정의 가능

<br>

### 3.2. await

- `async` 함수 안에서만 동작
- JavaScript는 `await`를 만나면 Promise 처리가 될 때까지 기다리고 결과는 그 이후에 반환됨

<br><br>

## 4. async / await 예외처리

- try/catch문 사용
  ```jsx
  function Data() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        return resolve("성공");
      }, 1000);
    });
  }

  async function loadData() {
    try {
      const result = await Data();
      console.log(result);
    } catch (e) {
      console.log(e);
    }
  }

  loadData();
  ```
