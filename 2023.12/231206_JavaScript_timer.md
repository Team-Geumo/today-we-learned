# JavaScript timer

## 타이머 함수

자바스크립트에서 다루는 타이머 함수는 일정 시간이 지난 후 특정 코드 또는 함수가 실행될 수 있도록 해주는 함수와 일정 시간마다 함수가 실행될 수 있도록 해주는 함수

## 타이머 함수 종류

`setTimeout(함수, 시간)`: 일정 시간 후 함수 실행

`setInterval(함수, 시간)`: 시간 간격마다 함수 실행

`clearTimeout()`: 설정된 Timeout 함수를 종료

`clearInterval()`: 설정된 Interval 함수를 종료

## 타이머 함수 사용 방법

setTimeout & clearTimeout

```js
// 'gogo'라는 글자가 3초뒤에 나타난다.
const timer = setTimeout(() => {
    console.log('gogo');
}, 3000);
```

```js
// 'h1El'을 클릭하면 함수가 종료된다.
const h1El = document.querySelector('h1');
h1El.addEventListener('click', () => {
    clearTimeout(timer);
});
```

setInterval & clearInterval

```js
// 'gogo'라는 글자가 3초마다 나타난다.
const timer = setInterval(() => {
    console.log('gogo');
}, 3000);

// 'h1El'을 클릭하면 함수가 종료된다.
const h1El = document.querySelector('h1');
h1El.addEventListener('click', () => {
    clearInterval(timer);
});
```
