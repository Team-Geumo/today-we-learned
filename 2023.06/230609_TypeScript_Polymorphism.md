# TypeScript Polymorphism

## 다형성(Polymorphism)이란?

- poly는 '많다, 많음' 라는 뜻이고 morp-는 '구조, 형태' 라는 뜻
- 따라서 Polymorphism, 다형성이란 여러가지 다양한 구조, 모양, 형태 라는 뜻
- 타입스크립트에서 이런한 다형성을 가능하게 해주는 것은 바로 제네릭(Generics) 타입

## 제네릭(Generic)이란?

- 제네릭이란 타입을 마치 함수의 파라미터처럼 사용하는 것을 의미
- 제네릭은 선언 시점이 아니라 생성 시점에 타입을 명시해 단일 타입만이 아닌 다양한 타입을 사용할 수 있도록 하는 기법
- 그리하여 인터페이스, 함수 등의 재사용성을 높일 수 있다는 장점이 있음
- 제네릭을 선언할 때 관용적으로 사용되는 식별자로 T 또는 V를 많이 사용을 함
- 이것을 타입 파라미터(Type parameter)라 함

## 제네릭 사용하기

### Call(=Function) Signatures로 사용하기

```ts
type SuperPrint = {
  <T>(arr: T[]): void; // <T> = generic
};
const superPrint: SuperPrint = (arr) => {
  arr.forEach((i) => console.log(i));
};

type SuperReturn = <T>(arr: T[]) => T;
const superReturn: SuperReturn = (arr) => arr[0];

superPrint([1, 2, 3, 4]); // output> 1, 2, 3, 4
superPrint(["a", "b", "c", "d"]); // output> a, b, c, d
superPrint([1, 2, false, true]); // output> 1, 2, false, true
console.log(superReturn([1, 2, 3, 4])); // output> 1
console.log(superReturn([1, 2, false, true])); // output> 1
```

### 함수에서 사용하기

```ts
function number<T>(a: T[]) {
  return a[0];
}
console.log(number(["1a", "2a", 3, 4]));
// output> 1a
```

### 화살표함수에서 사용하기

```ts
const arr = <T>(a: T[]) => a[0]
console.log(arr(['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']))
// type> string, output> ㄱ
console.log(arr([1, 2, 3, 4]
// type> number, output> 1
```

### 다양한 예시

- 제네릭 타입을 이용하여 원하는대로 코드 확장 및 타입 생성 가능
- 다른 타입 안에 제네릭 타입을 생성할 수 있음

```ts
type PlayName<E> = {
  name: string;
  extraInfo: E; // 제네릭
};

type ExtraInfo = { age: number };

type MeInfo = PlayName<ExtraInfo>;

const johan: MeInfo = {
  name: "johan",
  extraInfo: {
    age: 23,
  },
};

const kova: PlayName<null> = {
  name: "johan",
  extraInfo: null,
};
```
