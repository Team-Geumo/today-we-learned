# JavaScript 코딩 테스트 핵심 로직

## 1. 배열 순회

```js
const a = [1, 3, 45, 2, 10];
a.forEach((e, i) => {
  console.log(e, i);
});
```

## 2. 문자열 분해

```js
const str = 'Hello World';

const a = str.split(' '); // 공백 기준 분해
console.log(a); // ['Hello', 'World']

const joined = a.join(' '); // 공백으로 연결
console.log(joined); // Hello World
```

## 3. 정렬

```js
const numbers = [10, 1, 3, 5];

// 오름차순
a = numbers.sort((a, b) => a - b);
console.log(a); // [1, 3, 5, 10]

// 내림차순
b = numbers.sort((a, b) => (a - b) * -1);
console.log(b); // [10, 5, 3, 1]
```

## 4. 필터링

```js
const numbers = [1, 2, 3, 4, 5, 6];

const a = numbers.filter((e) => e % 2 == 0);
console.log(a); // [2, 4, 6]
```

## 5. 배열 재가공

```js
const numbers = [1, 2, 3, 4, 5, 6];

// map 사용 (권장)
const a = numbers.map((e) => e * 2);
console.log(a); // [2, 4, 6, 8, 10, 12]

// for 사용
let b = [];
for (let a of numbers) {
  b.push(a * a);
}
console.log(b); // [1, 4, 9, 16, 25, 36]
```

## 6. reduce

```js
const numbers = [1, 2, 3, 4, 5];
const a = numbers.reduce((total, e) => total + e, 0);
console.log(a); // 15
```

## 7. 그 외 기억해야 할 기본 문법

- 배열 탐색 : `find`, `findIndex`, `includes`
- 배열(문자열) 자르기 : `substring`(문자열), `slice`(배열, 문자열)
- 객체를 배열로 변환 : `Object.keys`, `Object.values`, `Object.entries`
- 배열 값 계산 : `Math.round`, `Math.ceil`, `Math.floor`, `Math.abs`
