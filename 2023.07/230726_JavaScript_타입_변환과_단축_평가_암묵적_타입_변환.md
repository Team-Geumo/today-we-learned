# 09장 타입 변환과 단축 평가
## 9.1 타입 변환이란?
기존 원시 값을 사용해 **다른 타입의 새로운 원시 값을 생성하는 것**

**명시적 타입 변환(타입 캐스팅)** : 개발자가 의도적으로 값의 타입을 변환하는 것<br>
**암묵적 타입 변환(타입 강제 변환)** : 개발자의 의도와 상관 없이 자바스크립트 엔진에 의해 암묵적으로 타입이 자동 변환되는 것<br>
```js
var x = 10;

var strA = x.toString(); // 명시적 타입 변환
var strB = x + '';       // 암묵적 타입 변환

console.log(typeof strA, strA); // string 10
console.log(typeof strB, strB); // string 10
console.log(typeof x, x)        // number 10 : x 변수의 값은 변하지 않음
```

## 9.2 암묵적 타입 변환
### 9.2.1 문자열 타입으로 변환
`+` 연산자가 문자열 연결 연산자로 동작할 때 피연산자는 문자열 타입으로 암묵적 타입 변환됨
```js
// 숫자 타입
0 + ''         // "0"
-0 + ''        // "0"
1 + ''         // "1"
-1 + ''        // "-1"
NaN + ''       // "NaN"
Infinity + ''  // "Infinity"
-Infinity + '' // "-Infinity"

// 불리언 타입
true + ''  // "true"
false + '' // "false"

// null 타입
null + '' // "null"

// undefined 타입
undefined + '' // "undefined"

// 심벌 타입
(Symbol()) + '' // TypeError: Cannot convert a Symbol value to a string

// 객체 타입
({}) + ''           // "[object Object]"
Math + ''           // "[object Math]"
[] + ''             // ""
[10, 20] + ''       // "10,20"
(function(){}) + '' // "function(){}"
Array + ''          // "function Array() { [native code] }"
```

### 9.2.2 숫자 타입으로 변환
산술 연산자, 비교 연산자의 피연산자는 숫자 타입으로 암묵적 타입 변환됨<br>
- 피연산자를 숫자 타입으로 변환할 수 없는 경우는 표현식의 평가 결과가 `NaN`이 됨
- `''`, `[]`, `null`, `false`는 `0`으로, `true`는 `1`로 변환됨
```js
// 문자열 타입
+''    // 0
+'0'   // 0
+'1'   // 1
+'one' // NaN

// 불리언 타입
+true  // 1
+false // 0

// null 타입
+null // 0

// undefined 타입
+undefined // NaN

// 심벌 타입
+Symbol() // TypeError: Cannot convert a Symbol value to a number

// 객체 타입
+{}             // NaN
+[]             // 0
+[10, 20]       // NaN
+(function(){}) // NaN
```

### 9.2.3 불리언 타입으로 변환
조건식의 평가 결과는 불리언 타입으로 암묵적 타입 변환됨<br>
불리언 타입이 아닌 값은 **Truthy 값(참으로 평가되는 값)** 또는 **Falsy 값(거짓으로 평가되는 값)** 으로 구분됨<br>

**Falsy 값** : Falsy 값 외의 모든 값은 참으로 평가되는 Truthy 값임
- `false`
- `undefined`
- `null`
- `0`, `-0`
- `NaN`
- `''`