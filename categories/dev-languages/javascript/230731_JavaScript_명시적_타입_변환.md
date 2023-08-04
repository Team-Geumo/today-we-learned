# 명시적 타입 변환
## 명시적 타입 변환 방법
1. 표준 빌트인 생성자 함수(`String`, `Number`, `Boolean`)을 `new` 연산자 없이 호출하는 방법
2. 빌트인 메서드를 사용하는 방법
3. 암묵적 타입 변환을 이용하는 방법

## 문자열 타입으로 변환
1. `String` 생성자 함수를 `new` 연산자 없이 호출하는 방법
2. `Object.prototype.toString()`을 사용하는 방법
3. 문자열 연결 연산자를 이용하는 방법

```js
// 1. String 생성자 함수를 new 연산자 없이 호출하는 방법
String(1);        // "1"
String(NaN);      // "NaN"
String(Infinity); // "Infinity"
String(true);     // "true"

// 2. Object.prototype.toString()을 사용하는 방법
(1).toString();        // "1"
(NaN).toString();      // "NaN"
(Infinity).toString(); // "Infinity"
(true).toString();     // "true"

// 3. 문자열 연결 연산자를 이용하는 방법
1 + '';        // "1"
NaN + '';      // "NaN"
Infinity + ''; // "Infinity"
true + '';     // "true"
```
## 숫자 타입으로 변환
1. `Number` 생성자 함수를 `new` 연산자 없이 호출하는 방법
2. `parseInt`, `parseFloat` 함수를 사용하는 방법 (문자열만 숫자 타입으로 변환 가능)
3. `+` 단항 산술 연산자를 이용하는 방법
4. `*` 산술 연산자를 이용하는 방법
```js
// 1. Number 생성자 함수를 new 연산자 없이 호출하는 방법
Number('0');     // 0
Number('-1');    // -1
Number('10.53'); // 10.53
Number(true);    // 1

// 2. parseInt, parseFloat 함수를 사용하는 방법 (문자열만 숫자 타입으로 변환 가능)
parseInt('0');       // 0
parseInt('-1');      // -1
parseFloat('10.53'); // 10.53

// 3. + 단항 산술 연산자를 이용하는 방법
+'0';     // 0
+'-1';    // -1
+'10.53'; // 10.53
+true;    // 1

// 4. * 산술 연산자를 이용하는 방법
'0' * 1;     // 0
'-1' * 1;    // -1
'10.53' * 1; // 10.53
true * 1;    // 1
```

## 불리언 타입으로 변환
1. `Boolean` 생성자 함수를 `new` 연산자 없이 호출하는 방법
2. `!` 부정 논리 연산자를 두 번 사용하는 방법
```js
// 1. Boolean 생성자 함수를 new 연산자 없이 호출하는 방법
// 문자열 타입 변환
Boolean('x');     // true
Boolean('');      // false
Boolean('false'); // true
// 숫자 타입 변환
Boolean(0);        // false
Boolean(1);        // true
Boolean(NaN);      // false
Boolean(Infinity); // true
// null, undefined 타입 변환
Boolean(null);      // false
Boolean(undefined); // false
// 객체 타입 변환
Boolean({}); // true
Boolean([]); // true
// 2. ! 부정 논리 연산자를 두 번 사용하는 방법
// 문자열 타입 변환
!!'x';     // true
!!'';      // false
!!'false'; // true
// 숫자 타입 변환
!!0;        // false
!!1;        // true
!!NaN;      // false
!!Infinity; // true
// null, undefined 타입 변환
!!null;      // false
!!undefined; // false
// 객체 타입 변환
!!{}; // true
!![]; // true
```