# Promise란?

```
✅ Promise는 자바스크립트 비동기 처리에 사용되는 객체입니다. 일반적으로 fetch 함수를 통해 데이터를 받아올 때 사용됩니다.
```

## 1. 자바스크립트 비동기 처리

- 자바스크립트는 싱글스레드 언어이고 기본적으로 동기적으로 코드를 처리함
  - 클라이언트에서 서버로 데이터를 요청했을 때 서버가 언제 그 요청에 대한 응답을 줄지도 모르는데, 마냥 다른 코드를 실행하지 않고 기다리게 됨
  - 이러한 문제점을 해결하기 위한 것이 비동기 처리
- **비동기 처리**: 특정 코드의 실행이 완료될 때까지 기다리지 않고, 다음 코드를 수행하는 것

  - 요청을 보낸 후 응답에 관계없이 다음 동작 실행

- 동기(Synchronous): 요청을 보낸 후 해당 응답을 받아야 다음 동작 실행
- 비동기(Asynchronous): 요청을 보낸 후 응답에 관계없이 다음 동작 실행

<br><br>

## 2. 자바스크립트 비동기 처리 문제점

- 비동기 특성상 특정 코드의 실행이 완료될 때까지 기다리지 않고, 다음 코드를 수행함
  - 클라이언트가 서버에 데이터를 요청했는데, 그 데이터가 다 오기도 전에 화면을 나타내서 화면에 아무것도 표시되지 않음
- 이러한 문제를 해결하는 방법 → `콜백함수`, `Promise`, `Async/Await`

<br><br>

## 3. Promise의 3가지 상태

- 상태: 프로미스의 처리 과정
- `new Promise()`로 프로미스를 생성하고 종료될 때까지 3가지 상태를 가짐

<br>

### 3.1. Pending(대기)

- **비동기 처리 로직이 아직 완료되지 않은 상태**
  ```jsx
  new Promise();
  ```
  - `new Promise()` 메서드를 호출하면 대기(Pending) 상태가 됨
  ```jsx
  new Promise(function (resolve, reject) {
    // ...
  });
  ```
  - `newPromise()` 메서드를 호출할 때 콜백 함수를 선언할 수 있고, 콜백 함수의 인자는 `resolve`, `reject`

<br>

### 3.2. Fulfilled(이행)

- **비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태**
  ```jsx
  new Promise(function (resolve, reject) {
    resolve();
  });
  ```
  - 콜백 함수의 인자 `resolve`를 실행하면 이행(Fulfilled) 상태가 됨
  ```jsx
  function getData() {
    return new Promise(function (resolve, reject) {
      const data = 100;
      resolve(data);
    });
  }

  // resolve() 의 결과 값 data를 resolvedData로 받음
  getData().then(function (resolvedData) {
    console.log(resolvedData); // 100
  });
  ```
  - 이행 상태가 되면 `then()`을 이용하여 처리 결과 값을 받을 수 있음

<br>

### 3.3. Rejected(실패)

- **비동기 처리가 실패하거나 오류가 발생한 상태**
  ```jsx
  new Promise(function (resolve, reject) {
    reject();
  });
  ```
  - `reject`를 호출하면 실패(Rejected) 상태가 됨
  ```jsx
  function getData() {
    return new Promise(function (resolve, reject) {
      reject(new Error("Request is failed"));
    });

    // reject()의 결과 값 Error를 err에 받음
    getData()
      .then()
      .catch(function (err) {
        console.log(err); // Error: Request is failed
      });
  }
  ```
  - 실패 상태가 되면 실패한 이유(실패 처리의 결과 값)를 `catch()`로 받을 수 있음
