# JavaScript closure

## 클로저(closure)란?

- 클로저는 독립적인 (자유) 변수를 가리키는 함수
- 클로저 안에 정의된 함수는 만들어진 환경을 기억함
- 흔히 함수 내에서 함수를 정의하고 사용하면 클로저라고 하지만, 대개는 정의한 함수를 리턴하고 사용은 바깥에서 하게됨

```js
function getClosure() {
  var text = "variable 1";
  return function () {
    return text;
  };
}

var closure = getClosure();
console.log(closure()); // 'variable 1'
```

- 위에서 정의한 getClosure()는 함수를 반환하고, 반환된 함수는 getClosure() 내부에서 선언된 변수를 참조함
- 또한 이렇게 참조된 변수는 함수 실행이 끝났다고 해서 사라지지 않았고, 여전히 제대로 된 값을 반환함

```js
var base = "Hello, ";
function sayHelloTo(name) {
  var text = base + name;
  return function () {
    console.log(text);
  };
}

var hello1 = sayHelloTo("승민");
var hello2 = sayHelloTo("현섭");
var hello3 = sayHelloTo("유근");
hello1(); // 'Hello, 승민'
hello2(); // 'Hello, 현섭'
hello3(); // 'Hello, 유근'
```

- 출력된 결과를 보면 text 변수가 동적으로 변화하고 있는 것처럼 보임
- 실제로는 text라는 변수 자체가 여러 번 생성된 것임. 즉, hello1()과 hello2(), hello3()은 서로 다른 환경을 가지고 있음

## 클로저를 통한 은닉화

- 일반적으로 JavaScript에서 객체지향 프로그래밍을 말한다면 Prototype을 통해 객체를 다루는 것을 말함

- Prototype을 통한 객체를 만들 때의 주요한 문제 중 하나는 Private variables에 대한 접근 권한 문제임

```js
function Hello(name) {
this.\_name = name;
}

Hello.prototype.say = function() {
console.log('Hello, ' + this.\_name);
}

var hello1 = new Hello('승민');
var hello2 = new Hello('현섭');
var hello3 = new Hello('유근');

hello1.say(); // 'Hello, 승민'
hello2.say(); // 'Hello, 현섭'
hello3.say(); // 'Hello, 유근'
hello1._name = 'anonymous';
hello1.say(); // 'Hello, anonymous'
```

- 위에서 Hello()로 생성된 객체들은 모두 \_name이라는 변수를 가지게 됨
- 변수명 앞에 underscore(\_)를 포함했기 Private variable으로 쓰고싶은 의도로 해석되지만, 실제로는 여전히 외부에서도 쉽게 접근가능한 변수임
- 이 경우에 클로저를 사용하여 외부에서 변수에 직접 접근하는 것을 제한할 수 있음

```js
function hello(name) {
var \_name = name;
return function() {
console.log('Hello, ' + \_name);
};
}

var hello1 = hello('승민');
var hello2 = hello('현섭');
var hello3 = hello('유근');

hello1(); // 'Hello, 승민'
hello2(); // 'Hello, 현섭'
hello3(); // 'Hello, 유근'
```

- 특별히 인터페이스를 제공하는 것이 아니라면, 여기서는 외부에서 \_name에 접근할 방법이 전혀 없음 >> 은닉화 해결

## 반복문 클로저

```js
var i;
for (i = 0; i < 10; i++) {
  setTimeout(function () {
    console.log(i);
  }, 100);
}
```

- 간단하게 0-9까지의 정수를 출력하는 코드이지만 실제로 돌려보면 엉뚱하게도 10만 열 번 출력되는 걸 볼 수 있음
- 이유 (실행 순서)
  1. 먼저 setTimeout()에 인자로 넘긴 익명함수는 모두 0.1초 뒤에 호출됨
  2. 그 0.1초 동안에 이미 반복문이 모두 순회되면서 i값은 이미 10이 된 상태
  3. 그 때 익명함수가 호출되면서 이미 10이 되어버린 i를 참조하게 됨
- 이 경우에도 클로저를 사용하면 원하는 대로 동작하도록 만들 수 있음

```js
var i;
for (i = 0; i < 10; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, 100);
  })(i);
}
```

- 클로저는 만들어진 환경을 기억함
- 이 코드에서 i는 IIFE내에 j라는 형태로 주입되고, 클로저에 의해 각기 다른 환경속에 포함됨
- 반복문은 10회 반복되므로 10개의 환경이 생길 것이고, 10개의 서로 다른 환경에 10개의 서로 다른 j가 생김

- 의문 1 : IIFE 매개변수로 i를 넘기지 않고 그냥 직접 참조해도 되지 않을까?

  - 답 : 인자로 i를 넘기지 않는다면 당연히 클로저가 참조하는 IIFE의 함수 스코프에서도 i값이 없으므로 생성 당시의 외부 스코프인 글로벌을 탐색하게 되고 결국 모두 같은 i를 참조하게 됨

- 의문 2 : 여기서 콜백으로 넘기는 함수 자체를 IIFE로 만들면 되지 않을까?
  - 답 : 원하는대로 0-9까지 출력은 되지만 함수 내부가 즉시 실행되어 버리므로 setTimeout()의 0.1초 딜레이가 작동하지 않게 됨

## 클로저의 성능

- 클로저는 각자의 환경을 가지고, 이 환경을 기억하기 위해서는 당연히 메모리가 소모됨
- 클로저를 생성해놓고 참조를 제거하지 않는 것은 C++에서 동적할당으로 객체를 생성해놓고 delete를 사용하지 않는 것과 비슷함
- 클로저를 통해 내부 변수를 참조하는 동안에는 내부 변수가 차지하는 메모리를 GC가 회수하지 않으므로, 따라서 클로저 사용이 끝나면 참조를 제거하는 것이 좋음

```js
function hello(name) {
var \_name = name;
return function() {
console.log('Hello, ' + \_name);
};
}

var hello1 = hello('승민');
var hello2 = hello('현섭');
var hello3 = hello('유근');

hello1(); // 'Hello, 승민'
hello2(); // 'Hello, 현섭'
hello3(); // 'Hello, 유근'

// 여기서 메모리를 release 시키기 클로저의 참조를 제거해야 한다.
hello1 = null;
hello2 = null;
hello3 = null;
```
