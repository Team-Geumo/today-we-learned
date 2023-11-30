## 프로미스

내용은 실행이 되었지만 결과를 아직 반환하지 않은 객체

콜백 지옥(Callback Hell)의 해결책

**프로미스 문법**

```js
const condition = true;
const promise = new Promise((resolve, reject) => {
    if (condition) {
        resolve('성공');
    } else {
        reject('실패');
    }
});
```

-   Promise 내부
    -   `resolve` : 성공 시 리턴 값 설정
    -   `reject` : 실패 시 리턴 값 설정
-   Promise 외부
    -   `then` : 성공 시 리턴 값을 받아 함수 실행 (`resolve`와 연결)
    -   `catch` : 실패 시 리턴 값을 받아 함수 실행 (`reject`와 연결)
    -   `finally` : 성공 / 실패 여부에 관계 없이 항상 실행

**프로미스 체이닝**

-   프로미스의 `then`을 연달아서 사용할 수 있음

```js
const promise = new Promise((resolve, reject) => {
    if (condition) {
        resolve('성공');
    } else {
        reject('실패');
    }
});

promise
    .then((message) => {
        return new Promise((resolve, reject) => {
            resolve(message);
        });
    })
    .then((message2) => {
        console.log(message2);
        return new Promise((resolve, reject) => {
            resolve(message2);
        });
    })
    .then((message3) => {
        console.log(message3);
        return new Promise((resolve, reject) => {
            resolve(message3);
        });
    })
    .catch((error) => {
        console.error(error);
    });
```
