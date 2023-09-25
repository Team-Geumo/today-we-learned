# ES12(2021), ES13(2022), ES14(2023)

## ES12(ECMAScript 2021)

### 1. String.prototype.replaceAll()

기존 `replace()`는 정규식(`RegExp`) 패턴이 아닌 단순 문자열 패턴을 사용할 때는 일치하는 첫 번째 항목만 교체 가능함<br>

```js
const str = 'I like my dog, my dog loves me';
const newStr = str.replace('dog', 'cat');

newStr;
// 'I like my cat, my dog loves me"
```

`replaceAll()`은 문자열 패턴을 대체할 때 일치하는 모든 패턴을 찾아내서 교체함<br>
즉, `RegExp`를 사용하지 않고도 하위 문자열의 모든 패턴을 쉽게 교체할 수 있음<br>

```js
const str = 'I like my dog, my dog loves me';
const newStr = str.replaceAll('dog', 'cat');

newStr;
// 'I like my cat, my cat loves me"
```

### 2. Promise.any()

`Promise.any()`는 주어진 프로미스 중 하나라도 성공하면 실행이 완료되지만 그렇지 않다면 모든 프로미스가 실패할 때까지 계속됨<br>
`Promise.any()` 내부의 모든 프로미스가 실패하면, 모든 프로미스의 실패 이유가 포함된 `AggregateError`가 발생함<br>

```js
Promise.any(promises).then(
  (first) => {
    //프로미스 중 하나라도 완료된 경우
  },
  (error) => {
    //모든 프로미스가 실패한 경우
  },
);
```

### 3. 논리연산자와 할당 표현식

논리연산자(`&&`, `||`, `??`)와 할당 표현식(`=`)을 결합할 수 있게 됨

```js
a ||= b;
// a = a || b와 동일

c &&= d;
// c = c && d와 동일

e ??= f;
// e = e ?? f와 동일
```

### 4. 숫자 구분 기호

숫자 구분 기호(`_`)가 도입되어 큰 숫자의 자릿수를 구분해 숫자를 더 쉽게 읽을 수 있게 됨

```js
x = 100_000;
// 100,000과 동일

fraction = 0.000_1;
// 1/10000
```

### 5. 약한 참조

**약한 참조** : 가비지 콜렉터에서 객체를 회수하는 것을 방지하지 않는 참조<br>
`WeakRef` 클래스를 사용하여 객체에 대한 약한 참조를 만들 수 있게 됨<br>
참고 : https://github.com/tc39/proposal-weakrefs

### 6. Intl.ListFormat

`Intl.ListFormat` 객체는 각종 언어별로 목록 서식을 활성화하는 객체의 생성자임

```js
const list = ['Apple', 'Orange', 'Banana'];

new Intl.ListFormat('en.GB, {style: 'long', type: 'conjunction}).format(list);
// Apple, Orange and Banana

new Intl.ListFormat('en.GB, {style: 'long', type: 'disjunction}).format(list);
// Apple, Orange or Banana
```

## ES13(ECMAScript 2022)

### 1. await

`async`/`await` 함수에서 `async`를 제외하고 `await`만 작성해도 됨

```js
(async() => {
    await AsyncFunction();
});
// 기존 : async/await을 함께 작성

(() => {
    await AsyncFunction();
})
// 변경 : await만 작성
```

### 2. cause field

`Error` 객체에 `cause`가 추가되어 `Error`를 체계적으로 핸들링할 수 있게 됨

```js
throw new Error('SERVER ERROR', { cause: 'DB CONNECTION ERROR' });
```

### 3. Array.prototype.at()

`at`이 추가되어 음수 인덱스를 사용할 수 있게 됨<br>
마지막 인덱스의 값을 가져오는 것이 편해짐<br>

```js
let arr = [1, 2, 3];
arr[arr.length - 1];
// 기존

arr.at(-1);
// 변경
```

<br>

**class 관련 변경 사항(4, 5, 6번)은 node.js와 웹 브라우저에서 이미 구현되어 있는 상태에서 ES13부터 정식 지원을 받게 됨**

### 4. constructor 없이 변수 초기화 가능 (정식 지원)

```js
class A {
  constructor() {
    foo = 'a';
  }
}
// 기존

class A {
  foo = 'a';
}
// 정식 지원
```

### 5. private 접근 제한자 지원 (정식 지원)

```js
class A {
  #foo = 'a';
  #bar() {
    console.log(foo);
  }
}
```

### 6. static method 지원 (정식 지원)

```js
class A {}
    A.foo() {
        console.log('hello')
}
// 기존

class A {
    static foo () {
        console.log('hello');
    }
}
// 정식 지원
```

## ES14(ECMAScript 2023)

### 1. Array.prototype.findLast()

`findLast()`는 배열을 역순으로 반복하면서 testing function을 만족하는 첫 번째 값을 반환하고 만족하는 값이 없으면 `undefined`를 반환함<br>

```js
const arr = [5, 12, 50, 130, 44];
const result = arr.findLast((element) => element > 45);

result; // 130
```

### 2. Array.prototype.findLastIndex()

`findLastIndex()`는 배열을 역순으로 반복하면서 testing function을 만족하는 첫 번째 값의 인덱스를 반환하고 만족하는 값이 없으면 `-1`을 반환함<br>

```js
const arr = [5, 12, 50, 130, 44];
const result = arr.findLastIndex((element) => element > 45);

result; // 3
```

### 3. Symbols as WeakMap keys

이전 버전에서는 오직 `Objects`만이 `WeakMap`의 키가 될 수 있었지만 `Symbols`도 사용할 수 있게 됨

```js
const wm = new WeakMap();
const key = Symbol('key'); // 다른 곳에서 등록되지 않아야 함
wm.set(key, 'hi!');

wm.get(key); // hi!
```

### 4. Change Array by Copy

원본 배열의 변형 없이 새로 복사된 배열을 반환하는 `toReversed()`, `toSorted()`, `toSpliced()`, `with()`가 추가됨<br>

**toReversed(), toSorted(), toSpliced()**

각각 `reverse()`, `sort()`, `splice()`와 같은 기능을 함

```js
const arr = [1, 2, 3];
arr.reverse(); // [3, 2, 1]
arr; // [3, 2, 1] (원본 배열 변형)

[...arr].reverse(); // [5, 12, 50] (복사)
arr; // [3, 2, 1] (원본 배열 변형 X)

// 기존 : 원본 배열의 변형이 일어나며 변형을 막으려면 복사 필요

arr.toReversed(); // [1, 2, 3]
arr; // [3, 2, 1]

// 변경 : 원본 배열의 변형 없이 새로 복사된 배열을 반환
```

**with()**

`with()`는 해당 인덱스의 값이 새로운 값으로 바뀐 배열을 반환함

```js
const arr = [1, 2, 3];

arr.with(1, 100); // [1, 100, 3]
arr; // [1, 2, 3]
```
