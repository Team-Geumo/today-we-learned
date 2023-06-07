## 상수와 변수

### ✅ undefined 와 null

undefined : 선언되었지만 아무런 값도 대입되지 않은 경우

null : 일부로 비어있음을 표현하기 위해 null 을 넣은 경우

```
let variable;
console.log(variable); // undefined
variable = null;
console.log(variable); // null
```

### ✅ 메모리

- 메모리 사용 과정

  - 할당 : 변수 생성 시 메모리 할당

  - 사용 : 할당된 메모리에 값을 넣어 사용

  - 해제 : 사용을 마치면 해제하여 메모리 비우기

- 메모리가 다 차면 프로그램이 터진다 = 꼭 해제해야 한다

- 따라서 JS 엔진의 Garbage Collector 는 사용하지 않는 메모리를 해제한다!

다음과 같이 변수를 선언 & 초기화한 후 변경했다면

변수의 고유 식별자를 생성하고 메모리에 주소를 할당 & 할당한 주소에 값이 들어간다.

`let a = 10;`

새로운 변수 b에 기존 변수 a를 대입한다면

b 는 기존 변수 a의 메모리 주소를 참조하게 된다.

`let b = a;`

여기서 기존 변수 a의 값을 변화시키면, a는 새로운 메모리 주소를 할당받고 그 곳에 변화된 값이 들어간다.

자바스크립트에서 원시타입은 변경이 불가능하기 때문에, 값이 변한다 = 새로운 메모리 주소

`let a = a + 1;`

즉, 이 과정을 다 거치면 a 와 b 는 다른 주소를 가르키고 있는 것이다 !

그렇다면 원래 a 가 할당받았던 메모리는 어떻게 된걸까?

정답은 `Garbage Collector`

브라우저는 Mark and Sweep Algorithm 방식으로 메모리를 해제한다.

닿을 수 없는 주소 = 필요 없는 주소로 판단하여 해당 메모리를 해제하는 것이다.

위의 예시라면, 기존의 a 주소는 아무것도 연결되어 있지 않다. 따라서 해제 !

### ✅const 배열은 왜 변할까

자바스크립트 엔진은 메모리 모델이 구현되어 있는 가상 머신으로 이루어져 있다.

메모리 모델 > Heap(참조 타입) / Call Stack(원시 타입)

```
const a = 1;
const b = 2;
const arr = [];
```

위 코드가 실행되면, Call Stack 에 a, b, arr 이 차례대로 쌓인다.

배열을 선언하면 Heap에 배열 영역이 생성된다.

여기서 Call Stack 에 들어있는 배열 변수는 Heap 의 배열 메모리 주소를 참조한다.

```
arr.push(1); // arr : [1]
arr.push(2); // arr : [1, 2]
```

Heap 영역의 메모리는 동적으로 크기가 변할 수 있으므로,

배열에 값을 추가하면 Heap영역에 그대로 할당된다. Call Stack에서는 그대로 Heap의 arr 메모리를 가르키고
있기 때문에, 배열이 상수로 선언되어도 값 push가 가능하다!

## 표현식과 연산자

### ✅ 이상한 && ||

인턴 면접을 본 적이 있는데, 이거로 많은 퀴즈(?)를 출제하셔서 상당히 당황한 기억이 있다.
그래서 이번 기회에 정복하기 !

**&& (AND)**

모든 피연산자가 true가 되었을 때 true를 반환한다.

일반적으로, 왼쪽에서 오른쪽으로 스캔하고 연산자는 처음으로 만나는 거짓 같은 피연산자의 값을 반환한다.

혹은 모두 참 같은 값이라면 마지막 피연산자의 값을 반환한다.

거짓 같은 값 `falsy`

false, undefined, null, 0, -0, NaN, ''(empty string)

참 같은 값 `truthy`

거짓 같은 값이 아닌 값들

**|| (OR)**
피연산자 중 하나 이상이 참인 경우에 true를 반환한다.
왼쪽에서 오른쪽으로 스캔하며 처음으로 만나는 참 같은 값을 반환한다.
둘 다 거짓 같은 값이라면 마지막 피연산자의 값을 반환한다.
x || y 에서, x가 truthy 라면 x를 반환하고, x가 falsy이고 y가 truthy라면 y를 반환한다.

```
true && true; // true
true && false; // false
false && true; // false
false && 3 === 4; // false
"Cat" && "Dog"; // "Dog"
false && "Cat"; // false
"Cat" && false; // false
"" && false; // ""
false && ""; // false

true || true; // true
false || true; // true
true || false; // true
false || 3 === 4; // false
"Cat" || "Dog"; // "Cat"
false || "Cat"; // "Cat"
"Cat" || false; // "Cat"
"" || false; // false
false || ""; // ""
```

잘 이해하면 리액트에서 조건부 렌더링에 써먹을 수 있닥..

### ✅ && || 활용

이렇게 OR 연산자와 AND 연산자가 표현식을 평가하는 도중에 평가 결과가 확정된 경우 나머지 평가 과정을

생략하는 것을 `단축 평가`라고 한다!

**null 과 undefined 확인하기**

```
const obj = null;

const item1 = obj.item;
console.log(item1); // TypeError: Cannot read properties of null

const item2 = obj && obj.item;
console.log(item2); // null
```

위의 경우에, obj.item 까지 가기 전 falsy 값인 obj 를 만나버렸으므로 바로 null 을 반환한다 = 타입에러를

피할 수 있다.

```
const a; //undefined
const func = (state) => {
  const thisState = state || 1; // a=undefined 이므로 1
  return thisState*2;
}
console.log(func(a)); // 2
```

이런 경우처럼 함수에 잘못 전달했을 때도 대비할 수 있다.

원래같았다면 NaN 지옥에 빠졌을 것이다

이 외에도, 매개변수가 분모로 들어갈 때 0이 들어가는 경우도 방지할 수 있을 것 같다!

## 배열과 객체

### ✅ typeof 배열 ?

자바스크립트에서 배열은 객체와 같은 타입을 가진다.
따라서 객체처럼 사용할 수 있다.

```
const arr = [1, 2, 3];
console.log(typeof arr); // object

arr['id'] = 'cszzi'; // 객체처럼 요소 추가
console.log(arr); // [ 1, 2, 3, id: 'cszzi' ]

arr[6] = 7;
console.log(arr); // [ 1, 2, 3, <3 empty items>, 7, id: 'cszzi' ]

console.log(Object.keys(arr)); // [ '0', '1', '2', '6', 'id' ]
console.log(arr.length); // 7 (id:cszzi 는 length 계산에 들어가지 않음)
```

이 코드를 보면, 동떨어진 인덱스인 6은 length에 반영이 되었지만 id:cszzi 는 length에 반영되지 않았다.

인덱스로 유효한 속성을 JavaScript 배열에 설정할 때, 그 인덱스가 현재 배열의 경계 바깥에 있는 경우, JavaScript 엔진은 배열의 length 속성을 그에 맞춰 업데이트하기 때문이다!
'id' 는 배열의 인덱스로 유효한 속성이 아니다.

```
const arr = [1, 2, 3, 4, 5, 6];

arr.length = 4;
console.log(arr); // [1, 2, 3, 4];

arr.length = 6;
console.log(arr); // [ 1, 2, 3, 4, <2 empty items> ]
console.log(arr[5]); // undefined
```

length 값을 조정하여 배열의 크기를 늘이거나 줄일 수 있다. 다만 늘인다면 empty items 로 칸만 늘어나는 거라, 직접 참조하면 undefined 가 찍힌다.

## 스코프와 클로저 (+호이스팅)

### ✅ 스코프

사전적으로는 범위로, 변수가 어느 범위까지 참조되는 지 = 유효범위를 의미한다.

스코프를 통해 동일한 식별자를 가진 변수간의 충돌을 방지할 수 있다.

스코프 없으면... 같은 파일 내의 모오오든 변수이름을 다 열심히 생각해서 다르게 해야한다.

**함수 레벨 스코프**

- 함수 내부 전체에서만 유효한 식별
- var 키워드로 선언된 변수, 함수 선언식으로 만들어진 함수
  **블록 레벨 스코프**
- if / else, while / for 내부 범위
- ES6의 let, const 키워드로 선언된 변수
  **렉시컬 스코프 (클로저 이해할때 쉬움)**
- 함수를 어디서 호출하는지가 아니라, 어디에 선언하였는지에 따라 결정
- 함수를 선언한 시점에 상위 스코프가 결정
- 중첩된 함수에서 내부 함수가 상위 스코프의 환경에 접근 가능

```
// 렉시컬 스코프 예시
let x = 1;

function foo() {
  let x = 10;
  bar(); // foo 안에서 bar 호출
}

function bar() { // 전역에 선언
  console.log(x);
}

foo(); // 1
bar(); // 1
```

여기서, bar를 호출할 때 위에 let x=10; 문장이 있음에도 불구하고 전역 x 값을 참조한다.

bar 함수는 전역에 선언되었기 때문에, bar 함수의 렉시컬 스코프는 선언될 때 상위 스코프인 전역이라서 그렇다

### ✅ 클로저

함수는 선언된 환경의 스코프를 기억한다.

자바스크립트에서 함수는 클로저를 형성하는데, 클로저는 함수 + 렉시컬 스코프 이다.

따라서 함수가 스코프 밖에서 실행될 때에도 상위 스코프에 접근할 수 있다.

```
function add(x){
  let y = 3;
  return function (z){
    console.log(x + y + z);
  }
};
const add1 = add(1); // closure : x=1, y=3
const add2 = add(2); // closure : x=2, y=3
add1(10); // z=10 : 14
add2(10); // z=10 : 15
```

add(1), add(2) 에서 console.log(x+y+z) 를 수행하는 함수를 리턴한다.

그러면서 각각의 closure 를 갖게 되고 매개변수 z 를 받아 다른 값을 출력하게 된다.

### ✅ 클로저 활용 - 정보 은닉

클로저를 통해, 내부 변수와 함수를 숨길 수 있다.

이렇게 클로저를 활용하는 것을 모듈 패턴이라고 한다..!

```
function Counter() {
  let privateCounter = 0;
  function changeBy(val) {
    privateCounter += val;
  }
  return {
    increment: function() {
      changeBy(1);
    },
    decrement: function() {
      changeBy(-1);
    },
    value: function() {
      return privateCounter;
    },
  }
}
const counter = Counter();
counter.increment(); // +1
counter.increment(); // +1
counter.decrement(); // -1
console.log(counter.value()); // 1
```

counter.increment, counter.decrement, counter.value 같은 환경을 공유하는 클로저이고,

그 안에는 변수privateCounter와 함수changeBy가 존재한다.

따라서 내부의 privateCounter에 직접 접근하지 않고, 클로저 함수를 통해서 값을 수정하고 조회할 수 있다.

### ✅ 클로저 - 버그 발생

```
function counting() {
  let i = 0;
  for (i = 0; i < 5; i += 1){
    setTimeout(function (){
      console.log(i);
    }, i * 100);
  }
}
counting();
// 5 5 5 5 5
```

클로저의 개념을 생각하면, setTimeout 에서 실행되는 익명 콜백 함수는 for문 내부의 i를 참조한다.

그렇지만 이 콜백함수가 선언과 동시에 반환되는 환경에서, 이미 i는 5이다.

이 부분이 헷갈려서 하나씩 생각을 해보았다

```
[i=0] 0ms 뒤에 function 탄생하기로 약속
[i=1] 100ms 뒤에 function 탄생하기로 약속
...
[i=4] 400ms 뒤에 function 탄생하기로 약속
[i=5] for문 끝
function 탄생
function 탄생
function 탄생
function 탄생
function 탄생
```

JS 엔진에서 setTimeout의 경우 지정된 시간 후에 함수를 바로 실행하는 것이 아니라, CallStack 에 추가한다.

그것도 자세히 말하자면 Message Queue 에 저장되어 있다가 지정된 시간이 지나고 CallStack 이 비어있을 때 추가한다.

따라서 CallStack 에 추가되었을(선언되었을) 시점에는 이미 CallStack이 비어있는 상태라서 for문의 문장이 다 끝난 것이다.

즉 그때는 i=5 라는것!!

아무튼 이런 이유로 인해 의도대로 0 1 2 3 4 출력이 안된다.
그렇다면 어떻게 해결해야 할까!

### ✅ 클로저 버그방지1 - let

```
function counting() {
  for (let i = 0; i < 5; i += 1){
    setTimeout(function () {
      console.log(i);
    }, i * 100);
  }
}
counting(); //0 1 2 3 4
```

let 키워드로 선언된 i 는 블록 스코프를 가진다.

즉, for문 안에서 선언되었기 때문에 i의 영향력은 for문 한바퀴(?)라는 것이다.

따라서 매 루프마다 클로저를 생성한다.

### ✅ 클로저 버그방지2 - IIFE

IIFE란?
즉시 실행 함수 표현 IIFE, Immediately Invoked Function Expression

정의되자마자 즉시 실행되는 자바스크립트 함수

```
function counting() {
  let i = 0;
  for (i = 0; i < 5; i += 1){
    (function (number) {
      setTimeout(function () {
        console.log(number);
      }, number * 100);
    })(i);
  }
}
```

매 루프마다 setTimeout 을 실행하는 함수를 정의하고, i를 매개변수로 호출한다.

코드를 풀어서 쓰면 아래랑 같다! (이해가 잘 안되었어서 풀어서 써봄)

```
function counting() {
  let i = 0;
  for (i = 0; i < 5; i += 1){
    const func = function(number){ // 정의
      setTimeout(function(){
        console.log(number);
      }, number*100);
    };
    func(i); // 실행
  }
}
```

이렇게 되면 매 루프마다 함수를 선언하기 때문에 그때그때 클로저가 형성된다.

클로저의 렉시컬 환경은 선언되는 시점에서의 환경이기 때문에, 그때의 i를 참조할 수 있다.

### ✅ 호이스팅

호이스팅은 '끌어올림'을 뜻한다.

JS엔진은 컴파일 - 인터프리팅 순서로 코드를 처리하게 되는데, 컴파일 단계에서 선언과 초기화를 분리하여
인식한다.

var a = 2; 는 var a; 와 a = 2; 로 인식하는 것이다.

선언 단계에서는 선언의 위치와 상관 없이 해당 스코프의 컴파일 단계에서 처리하며, 선언된 변수는 메모리에 먼저 저장된다.

이렇게 선언 단계가 스코프의 꼭대기로 끌어올려지는 것을 호이스팅이라고 한다.

```
function func1() {
	a=2;
	var a;
	console.log(a); // 선언부가 호이스팅되므로 2를 출력
}
function func2(){
	console.log(a); // 선언하기 전에 참조 = undifined
	var a=2;
}

function func3(){
  a=2;
  let a;
  console.log(a);
}
function func4(){
  console.log(a);
  let a=2;
}
```

```
func1(); // 2
func2(); // undefined
func3(); // ReferenceError : Cannot access 'a' before initialization
func4(); // ReferenceError : Cannot access 'a' before initialization
```

var 키워드로 선언하여 발생한 호이스팅으로 인한 문제는 let 과 const 키워드로 방지할 수 있다.

아예 에러처리가 됨으로써 코드가 예측할 수 있게 되고, 잠재적 버그가 사라지는 것이다.

그렇다면 let, const 는 호이스팅이 안되나 ?

아니다. 얘네도 호이스팅이 된다고 할수 있다.

ReferenceError가 뜨는 이유는 TDZ(Temporal Dead Zone)의 영향때문인데..

### ✅ TDZ

자바스크립트에서의 변수는 다음과 같은 과정을 거친다.

1. 선언 : 변수 객체 등록
2. 초기화 : 선언 단계의 변수를 위한 메모리 생성, undefined 로 초기화
3. 할당 : 사용자가 초기화된 메모리에 값을 넣는 것
   var 키워드로 변수를 선언하면 선언단계와 초기화단계가 동시에 이루어진다.

따라서, 호이스팅 영향을 받아 선언하기 전에 참조하더라도 undefined 가 출력되는 것이다.

(선언부가 끌어올려지기 때문에)

let, const 키워드로 변수를 선언하면 전혀 다르다.

선언단계와 초기화단계가 나누어져 진행된다. 초기화단계 전에는 읽거나 쓸 수 없다.

위의 호이스팅 예시처럼, 초기화 전에 접근하게 되면 ReferenceError 를 발생시킨다.

변수 스코프의 맨 위(선언단계)에서 변수의 초기화 완료 시점까지의 변수를 시간상 사각지대 (Temporal Dead Zone, TDZ) 에 들어간 변수라고 한다.

{
// TDZ가 스코프 맨 위에서부터 시작
// = 호이스팅으로 인한 선언 단계

    const func = () => console.log(number); // OK

    // TDZ 안에서 number에 접근하면 ReferenceError

    let number = 3;
    // 이 코드가 실행되었을 때 number의 TDZ 종료
    func(); // TDZ 끝나고 호출 - 3

}
위 코드의 경우, number 변수 선언 코드가 number에 접근하는 func 함수보다 아래에 위치하지만 정상 동작한다.
함수가 호출되었을 시점은 number 가 초기화된 후이기 때문이다.
이렇게 .. 사각지대가 코드의 작성 위치가 아니라 코드의 실행 시간에 의해 형성되기 때문에 '시간상 사각지대' 라고 한다 !
