# JavaScript Symbol

- 심볼은 유일한 식별자(unique identifier)를 만들고 싶을 때 사용할 수 있음
- `Symbol()`을 사용하여 심볼값을 만들 수 있음

```js
const person = Symbol('철수');
console.log(person);
// Symbol(철수)
```

## 심볼의 고유성

- 심볼 값은 동일하더라도 각 심볼은 고유하기때문에 동일 연사자(==)로 비교 시 false가 반환됨

```js
const me = Symbol('철수');
const clone = Symbol('철수');

console.log(me == clone);
// 출력 : false
```

## 심볼이 객체 속성일때

- 심볼을 사용해서 객체 속성에 대한 식별자를 만들 수 있음
- people 객체에서 이름이 같은. 즉, 속성이 같을때 겹치는 것을 피하기 위해서 심볼을 사용할 수 있음

```js
const people = {
  철수: 'friend',
  영미: 'friend',
  철수: 'brother',
};

for (person in people) {
  console.log(person);
}
// 출력 : 철수
//        영미
```

- 아래와 같은 경우 심볼은 for...in에서 배제되어 열거할 수 없기 때문에 `undefined` 출력

```js
const people = {
  [Symbol('철수')]: 'friend',
  [Symbol('영미')]: 'friend',
  [Symbol('철수')]: 'brother',
};

for (person in people) {
  console.log(person);
}
// 출력 : undefined
```

- 객체의 속성들의 배열을 얻는 방법 : `Object.getOwnPropertySymbols()`

```js
const people = {
  [Symbol('철수')]: 'friend',
  [Symbol('영미')]: 'friend',
  [Symbol('철수')]: 'brother',
};

const symbols = Object.getOwnPropertySymbols(people);
console.log(symbols);
// 출력 : (3) [Symbol(철수), Symbol(영미), Symbol(철수)]
```

- 배열이기 때문에 속성에 접근을 하기 위해서는 `map`을 사용

```js
const symbols = Object.getOwnPropertySymbols(people);
const value = symbols.map(symbol => people[symbol]);
console.log(value);
// 출력 :
(3) ['friend', 'friend', 'brother']
0: "friend"
1: "friend"
2: "brother"
length: 3
```
