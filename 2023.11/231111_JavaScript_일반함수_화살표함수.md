# JavaScript 일반함수 화살표함수 차이

## 1. this

1. 일반함수

- 일반적으로 함수를 호출할 경우 global 객체를 가리킨다(기본적으로 window 객체)

```js
function func1() {
  console.log(this);
}
func1(); // window object
```

- 메소드함수를 호출할 경우 메소드를 소유한 객체를 가리킨다

```js
const obj = {
  name: '공작새',
  method() {
    console.log(this.name); // 공작새
  },
};
```

2. 화살표함수
   화살표 함수 내에서 자체적으로 가리키는 this가 없다.
   상위 스코프의 this를 가리킨다.

```js
let myObj = {
  age: 30,
  arrowFunc: () => {
    console.log(this.age);
  },
  regularFunc() {
    console.log(this.age);
  },
};
myObj.arrowFunc(); //undefinedmyObj.regularFun(); //30
```

myObj의 객체 내에 화살표 함수로 메소드를 정의 한 후 this.age 속성을 불러오면? 화살표 함수의 this를 모른다면 기대하는 값은 30이지만 결과는 undefined 이다.
화살표함수의 상위 스코프는 현재 myObj 객체가 아니라 상위스코프인 window 객체이기 때문이다
일반함수 메소드 안에서 this를 저장하기 위해 var self = this 요런 변수들을 많이 사용했었는데 화살표 함수를 쓰면 이런 방법을 사용 할 필요가 없다
또한 화살표 함수내에서 bind,call,apply를 사용하여 this바인딩을 할 수 없다.

## 2. Arguments

- 일반함수에서는 arguments의 사용이 가능하다

  ```js
  function regularFunc() { console.log(arguments,arguments[0]); //[1,2,3],1}regularFunc(1,2,3)

  ```

- 화살표함수에서 사용할 경우 에러가 난다

```js
const arrFunc = () => { console.log(arguments,arguments[0]); //arguments is not defined}arrFunc(1,2,3)

```

## 3. 생성자함수 사용

일반함수에선 생성자 함수 사용이 가능하다.

```js

function Cfunc(){ this.age = 20}const a = new Cfunc()console.log(a.age)// 20
```

화살표함수에선 생성자 함수 사용이 안된다.

```js
const CarrowFunc = () => { this.age = 20}const a = new CarrowFunc()
 // CarrowFunc is not a constructor

```
