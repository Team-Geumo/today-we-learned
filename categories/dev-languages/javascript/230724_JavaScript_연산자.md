# 07장 연산자
**피연산자(operand)** 는 값, **연산자(operator)** 는 피연산자를 연산하여 새로운 값을 만드는 역할을 함
## 7.1 산술 연산자(arithmetic operator)
피연산자를 대상으로 수학적 계산을 수행해 새로운 숫자 값을 만드는 연산자<br>
- 피연산자의 개수에 따라 **이항 산술 연산자**와 **단항 산술 연산자**로 구분
- 산술 연산이 불가능한 경우 `NaN`을 반환

### 7.1.1 이항(binary) 산술 연산자
2개의 피연산자를 산술 연산하여 숫자 값을 만드는 연산자<br>
- 피연산자의 값을 변경하는 **부수 효과(side effect)** 가 없음
- 즉, 어떤 산술 연산을 해도 피연산자의 값이 바뀌지 않고 언제나 새로운 값을 만듦

|이항 산술 연산자|의미|부수 효과|
|:---:|:---:|:---:|
|`+`|덧셈|X|
|`-`|뺄셈|X|
|`*`|곱셈|X|
|`/`|나눗셈|X|
|`%`|나머지|X|

### 7.1.2 단항(unary) 산술 연산자
1개의 피연산자를 산술 연산하여 숫자 값을 만드는 연산자

|이항 산술 연산자|의미|부수 효과|
|:---:|:---:|:---:|
|`++`|증가|O|
|`--`|감소|O|
|`+`|효과 없음|X|
|`-`|양수를 음수로, 음수를 양수로 반전|X|
<br>

**증가/감소 연산자**

피연산자의 값을 변경하는 암묵적 할당이 이루어짐
- **전위 증가/감소 연산자** : 먼저 피연산자의 값을 증가/감소시킨 후, 다른 연산을 수행함 (선증가/선감소 후할당)
- **후위 증가/감소 연산자** : 먼저 다른 연산을 수행한 후, 피연산자의 값을 증가/감소시킴 (선할당 후증가/후감소)

    ```js
    var x = 5, result;

    // 전위 증가/감소 연산자
    result = ++x;
    console.log(result, x); // 6 6

    result = --x;
    console.log(result, x); // 5 5

    // 후위 증가/감소 연산자
    result = x++;
    console.log(result, x); // 5 6

    result = x--;
    console.log(result, x); // 6 5
    ```

### 7.1.3 문자열 연결 연산자
`+` 연산자는 피연산자 중 하나 이상이 문자열인 경우 문자열 연산자로 동작함
```js
// Number은 String으로 타입 변환
'1' + 2;
1 + '2';

// true는 1, false는 0로 타입 변환
1 + true;
1 + false;

// null은 0으로 타입 변환
1 + null;

// undefined는 숫자로 타입 변환되지 않음
+undefined;
1 + undefined;
```
- 위 코드처럼 개발자의 의도와 상관 없이 **암묵적인 타입 변환(implict coercion)** 이 일어남 : [**09장 타입 변환과 단축 평가**]() 참고

## 7.2 할당 연산자(assignment operator)
우항에 있는 피연산자의 평가 결과를 좌항에 있는 변수에 할당하는 연산자<br>
|할당 연산자|예|동일 표현|부수 효과|
|:---:|:---:|:---:|:---:|
|`=`|`x = 5`|`x = 5`|O|
|`+=`|`x += 5`|`x = x + 5`|O|
|`-=`|`x -= 5`|`x = x - 5`|O|
|`*=`|`x *= 5`|`x = x * 5`|O|
|`/=`|`x /= 5`|`x = x / 5`|O|
|`%=`|`x %= 5`|`x = x % 5`|O|

**할당문과 연쇄 할당**
```js
var x;

console.log(x = 10); // 10
```
할당문은 할당된 값으로 표현되는 표현식이므로 할당문을 다른 변수에 할당할 수 있음<br>

```js
var a, b, c;

// 연쇄 할당 : 오른쪽에서 왼쪽으로 진행
a = b = c = 0;

console.log(a, b, c);
```

## 7.3 비교 연산자(comparison operator)
좌항과 우항의 피연산자를 비교해 그 결과를 불리언 값으로 반환하는 연산자<br>
주로 `if` 문이나 `for` 문과 같은 제어문의 조건식에 사용됨

### 7.3.1 동등/일치 비교 연산자
동등 비교 연산자는 느슨한 비교, 일치 비교 연산자는 엄격한 비교를 함<br>
|비교 연산자|의미|사례|설명|부수 효과|
|:---:|:---:|:---:|:---:|:---:|
|`==`|동등 비교|`x == y`|x와  y의 값이 같음|X|
|`=`|일치 비교|`x === y`|x와  y의 값과 타입이 같음|X|
|`=`|부동등 비교|`x != y`|x와  y의 값이 다름|X|
|`=`|불일치 비교|`x !== y`|x와  y의 값과 타입이 다름|X|
<br>

**동등 비교 연산자(loose equality operator)**

피연산자를 비교할 때 먼저 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 비교함<br>
결과를 예측하기 어렵고 실수하기 쉬우므로 일치 비교 연산자를 권장함<br>
```js
5 == '5'; // true
```
- **주의 사항** : 안티 패턴이 발생함 (지양하므로 이해하지 않아도 됨)

    ```js
    '0' == ''; // false
    0 == '';   // true
    0 == '0';  // true
    false == 'false';   // false
    false == '0';       // true
    false == null;      // false
    false == undefined; // false
    ```
<br>

**일치 비교 연산자(strict equality operator)**

피연산자의 **타입과 값이 모두 같을 경우에만** true를 반환함<br>
암묵적 타입 변환을 하지 않기 때문에 예측하기 쉬움<br>
```js
5 === 5;   // true
5 === '5'; // false
```

- 동등 비교 연산자, 일치 비교 연산자 모두 **양의 0**과 **음의 0**을 같다고 판단함

    ```js
    0 == -0  // true
    0 === -0 // true
    ```

- **주의 사항** : `NaN`은 자신과 일치하지 않는 유일한 값으로, 숫자가 `NaN`인지 조사하려면 `Number.isNaN`을 사용해야 함

    ```js
    NaN === NaN; // false

    Number.isNaN(NaN); // true
    Number.isNaN(10);  // false
    Number.isNaN(1 + undefined); // true
    ```

<br>

**Object.is()**

예측 가능한 정확한 비교 결과를 반환하는 메서드<br>
```js
-0 === 0;         // true
Object.is(-0, +0) // false

NaN === NaN;         // false
Object.is(NaN, NaN); // true
```

### 7.3.2 대소 관계 비교 연산자
피연산자의 크기를 비교하여 불리언 값을 반환하는 연산자<br>
|대소 관계 비교 연산자|예제|설명|부수 효과|
|:---:|:---:|:---:|:---:|
|`>`|`x > y`|x가 y보다 크다|X|
|`<`|`x < y`|x가 y보다 작다|X|
|`>=`|`x >= y`|x가 y보다 크걷나 같다|X|
|`>=`|`x <= y`|x가 y보다 작거나 같다|X|

## 7.4 삼항 조건 연산자(ternary operator)
조건식의 평가에 따라 반환할 값을 결정하는 연산자<br>
`조건식 ? 조건식이 true일 때 반환할 값 : 조건이 false일 때 반환할 값`<br>
```js
var result = score >= 60 ? 'pass' : 'fail';
```
- 조건식 평가 결과가 불리언 값이 아니면 암묵적 타입 변환이 일어남

    ```js
    var x = 2;

    var result = x % 2 'odd' : 'even'; // even
    ```
- `if ... else`문도 유사하게 처리할 수 있지만 **값으로 사용할 수 없다**는 차이가 있음

    ```js
    var x = 10;

    var result = if (x % 2) { result = 'odd'; } else { result = 'even'; };
    // SyntaxError : if ... else문은 표현식이 아닌 문
    ```

## 7.5 논리 연산자(logical operator)
피연산자를 논리연산 하는 연산자<br>

<table>
  <tr>
    <th>논리 연산자</th>
    <th>의미</th>
    <th>부수 효과</th>
</tr>
  <tr align="center">
<td><code>||</code></td>
<td>논리합(OR)</td>
<td>X</td>
</tr>
  <tr align="center">
<td><code>&&</code></td>
<td>논리곱(AND)</td>
<td>X</td>
</tr>
  <tr align="center">
<td><code>!</code></td>
<td>부정(NOT)</td>
<td>X</td>
</tr>
</table>

**논리합과 논리곱**

불리언 값이 아닌 값을 반환할 수 있으며 **두 개의 피연산자 중 어느 한 쪽으로 평가됨** : [**9.4절 단축 평가**]() 참고
```js
'Cat' || 'Dog'; // Cat
'Cat' && 'Dog'; // Dog
```
<br>

**논리 부정 연산자**

항상 불리언 값을 반환하며 피연산자가 불리언 값이 아니면 **암묵적 타입 변환**이 일어남
```js
!0;       // true
!'Hello'; // false
```
<br>

**드 모르간의 법칙**
```js
!(x || y) === (!x && !y)
!(x && y) === (!x || !y)
```

## 7.6 쉼표 연산자
왼쪽부터 차례대로 피연산자를 평가하고 마지막 피연산자의 결과를 반환하는 연산자
```js
var x, y, z;

x = 1, y = 2, z = 3; // 3
```

## 7.7 그룹 연산자
자신의 피연산자인 표현식을 가장 먼저 평가하는 연산자로, 연산자 중 **우선순위가 가장 높음**
```js
10 * 2 + 3;  // 23
10 * (2 + 3) // 50
```

## 7.8 typeof 연산자
피연산자의 데이터 타입을 **문자열로 반환하는** 연산자<br>
`string`, `number`, `boolean`, `undefined`, `symbol`, `object`, `function` 중 하나를 반환함 (`null`을 반환하는 경우는 없음)
```js
typeof ''             // string
typeof 1              // number
typeof NaN            // number
typeof true           // boolean
typeof undefined      // undefined
typeof Symbol()       // symbol
typeof null           // object
typeof []             // object
typeof {}             // object
typeof new Date()     // object
typeof /test/gi       // object
typeof function () {} // function
```
- `null` 타입은 `typeof` 연산자로 확인할 수 없으므로 일치 연산자를 사용해야 함

  ```js
  var foo = null;
  
  typeof foo === null; // false
  foo == null;         // true
  ```
- 선언하지 않은 식별자를 `typeof` 연산자로 연산하면 `ReferenceError`가 발생하지 않고 `undefined`를 반환함

  ```js
  typeof undeclared; // undefined
  ```

## 7.9 지수 연산자
좌항의 피연산자를 밑(base)로, 우항의 피연산자를 지수(exponent)로 거듭 제곱하여 숫자 값을 반환하는 연산자
```js
// ES7에서 지수 연산자가 도입되기 전에는 Math.pow()를 사용했음
Math.pow(2, 2);  // 4
Math.pow(2, -2); // 0.25

2 ** 2;  // 4
2 ** -2; // 0.25
```
- 음수를 거듭제곱의 밑으로 사용하려면 괄호로 묶어야 함

  ```js
  -5 ** 2;   // SyntaxError

  (-5) ** 2; // 25
  ```
- 다른 산술 연산자와 마찬가지로 할당 연산자와 함께 사용할 수 있음

  ```js
  var num = 5;
  num **= 2; // 25
  ```

## 7.10 그 외의 연산자
|연산자|개요|참고|
|---|---|---|
|`?.`|옵셔널 체이닝 연산자|[**9.4.2절 옵셔널 체이닝 연산자**]()|
|`??`|`null` 병합 연산자|[**9.4.3절 null 병합 연산자**]()|
|`delete`|프로퍼티 삭제|[**10.8절 프로퍼티 삭제**]()|
|`new`|생성자 함수를 호출할 때 사용하여 인스턴스를 생성|[**17.2.6절 new 연산자**]()|
|`instanceof`|좌변의 객체가 우변의 생성자 함수와 연결된 인스턴스인지 판별|[**instanceof 연산자**]()|
|`in`|프로퍼티 존재 확인|[**in 연산자**]()|

## 7.11 연산자의 부수 효과
대부분의 연산자는 다른 코드에 영향을 주지 않음<br>
**부수 효과가 있는 연산자** : 할당 연산자(`=`), 증가/감소 연산자(`++`/`--`), `delete` 연산자
```js
var x;
var o = { a: 1 };

// 할당 연산자는 변수 값이 변화는 부수 효과가 있음
x = 1;
console.log(x); // 1

// 증가/감소 연산자는 피연산자의 값을 변경하는 부수 효과가 있음
x++;
console.log(x); // 2

// delete 연산자는 객체의 프로퍼티를 삭제하는 부수 효과가 있음
delete o.a;
console.log(o); // {}
```
## 7.12 연산자 우선 순위
여러 개의 연산자로 이뤄진 문이 실행될 때 연산자가 실행되는 순서
<table>
<tr><th>우선순위</th><th align="center">연산자</th></tr>
<tr><td align="center">1</td><td><code>()</code></td></tr>
<tr><td align="center">2</td><td><code>new</code>(매개변수 존재), <code>.</code>, <code>[]</code>(프로퍼티 접근), <code>()</code>(함수 호출), <code>?.</code>(옵셔널 체이닝)</td></tr>
<tr><td align="center">3</td><td><code>new</code>(매개변수 미존재)</td></tr>
<tr><td align="center">4</td><td><code>x++</code>, <code>x--</code></td></tr>
<tr><td align="center">5</td><td><code>!x</code>, <code>+x</code>, <code>-x</code>, <code>++x</code>, <code>--x</code>, <code>typeof</code>, <code>delete</code></td></tr>
<tr><td align="center">6</td><td><code>**</code></td></tr>
<tr><td align="center">7</td><td><code>*</code>, <code>/</code>, <code>%</code></td></tr>
<tr><td align="center">8</td><td><code>+</code>, <code>-</code></td></tr>
<tr><td align="center">9</td><td><code><</code>, <code><=</code>, <code>></code>, <code>>=</code>, <code>in</code>, <code>instanceof</code></td></tr>
<tr><td align="center">10</td><td><code>==</code>, <code>!=</code>, <code>===</code>, <code>!==</code></td></tr>
<tr><td align="center">11</td><td><code>??</code>(null 병합)</td></tr>
<tr><td align="center">12</td><td><code>&&</code></td></tr>
<tr><td align="center">13</td><td><code>||</code></td></tr>
<tr><td align="center">14</td><td><code>? ... : ...</code></td></tr>
<tr><td align="center">15</td><td><code>=</code>, <code>+=</code>, <code>-=</code>, ... (할당)</td></tr>
<tr><td align="center">16</td><td><code>,</code></td></tr>
</table>

## 7.13 연산자 결합 순서
연산자의 어느 쪽(좌항 또는 우항)부터 평가를 수행할 것인지를 나타내는 순서
<table>
<tr><th>결합 순서</th><th>연산자</th></tr>
<tr><td align="center">좌항 → 우항</td><td><code>+</code>, <code>-</code>, <code>/</code>, <code>%</code>, <code><</code>, <code><=</code>, <code>></code>, <code>>=</code>, <code>&&</code>, <code>||</code>, <code>.</code>, <code>[]</code>, <code>()</code>, <code>??</code>, <code>?</code>, <code>in</code>, <code>instanceof</code></td></tr>
<tr><td align="center">우항 → 좌항</td><td><code>=</code>, <code>+=</code>, <code>-=</code>, ... (할당) <code>++</code>, <code>--</code>, <code>!x</code>, <code>+x</code>, <code>-x</code>, <code>++x</code>, <code>--x</code>, <code>typeof</code>, <code>delete</code>, <code>? ... : ...</code>, <code>**</code></td></tr>
</table>