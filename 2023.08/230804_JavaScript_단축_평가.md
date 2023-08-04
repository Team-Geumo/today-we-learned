# 단축 평가
## 논리 연산자를 사용한 단축 평가
논리합(`||`) 또는 논리곱(`&&`) 연산자 표현식의 평과 결과는 언제나 2개의 피연산자 중 어느 한쪽으로 평가되며 불리언 값이 아닐 수도 있음<br>

**단축 평가(short-circuit evaluation)** : 표현식을 평가하는 도중에 평가 결과가 확정된 경우 나머지 평가 과정을 생략하는 것<br>

<table>
    <tr align=center>
        <td><b>단축 평가 표현식</b></td>
        <td><b>평가 결과</b></td>
    </tr>
    <tr align=center>
        <td><code>true || anything</code></td>
        <td><code>true</code></td>
    </tr>
    <tr align=center>
        <td><code>false || anything</code></td>
        <td><code>anyting</code></td>
    </tr>
    <tr align=center>
        <td><code>true && anything</code></td>
        <td><code>anything</code></td>
    </tr>
    <tr align=center>
        <td><code>false && anything</code></td>
        <td><code>false</code></td>
    </tr>
</table>

단축평가를 사용하면 `if` 문을 대체할 수 있음
- 어떤 조건이 Truthy 값일 때는 논리곱(`&&`) 연산자 표현식 사용

    ```js
    var done = true;
    var message = '';

    message = done && 'Done!'; // done이 true일 때 message에 'Done!'을 할당
    
    console.log(message); // Done!
    ```
- 어떤 조건이 Falsy 값일 때는 논리합(`||`) 연산자 표현식 사용

    ```js
    var done = false;
    var message = 'Undone!';

    message = done || 'Undone!'; // done이 false일 때 message에 'Undone!'을 할당

    console.log(message); // Undone!
    ```
<br>

**단축평가를 사용한 유용한 패턴들**

1. 객체를 가리키기를 기대하는 변수가 `null` 또는 `undefined`가 아닌지 확인하고 프로퍼티를 참조할 때

    ```js
    // 단축 평가 사용 전 : TypeError 발생
    var elemA = null;
    var value = elemA.value; // TypeError

    // 단축 평가 사용 후 : 에러 발생 X
    var elemB = null;
    var value = elemB && elemB.value; //  elemB가 Truthy 값이면 elemB.value, Falsy 값이면 elemB로 평가
    ```
2. 함수 매개변수에 기본값을 설정할 때

    ```js
    // 단축 평가를 사용해 매개변수의 기본값을 설정하면 인수를 전달하지 않아도 에러 발생 X
    function getStringLength(str) {
        str = str || '';
        return str.length;
    }

    // 참고 : ES6의 매개변수 기본값 설정
    function getStringLength(str = '') {
        return str.length;
    }

    getStringLength();     // 0
    getStringLength('hi'); // 2
    ```


## 옵셔널 체이닝 연산자
ES11(ECMAScript2020)에서 도입된 옵셔널 체이닝(optional chaining) 연산자(`?.`)는 좌항의 피연산자가 `null` 또는 `undefined`인 경우 `undefined`를 반환하고, 그렇지 않으면 우항의 프로퍼티 참조를 이어감 
- 논리곱(`&&`) 연산자는 모든 Falsy 값에 대해 좌항 피연산자를 그대로 반환함

    ```js
    var str = '';
    var length = str && str.length; // str이 Falsy 값이므로 str.length를 참조하지 못함

    console.log(length); // ""
    ```
- 옵셔널 체이닝 연산자는 `null` 또는 `undefined`인 경우가 아니면 우항의 프로퍼티 참조를 이어감

    ```js
    var str = '';
    var length = str?.legnth; // str이 null 또는 undefined가 아니므로 str.length를 참조함

    console.log(length); // 0
    ```

## null 병합 연산자
ES11(ECMAScript2020)에서 도입된 null 병합(nullish coalescing) 연산자(`??`)는 좌항의 피연산자가 `null` 또는 `undefined`인 경우 우항의 피연산자를 반환하고, 그렇지 않으면 좌항의 피연산자를 반환함
- 논리합(`||`) 연산자는 모든 Falsy 값에 대해 우항의 피연산자를 반환함

    ```js
    var foo = '' || 'default string'; // ''를 참조하지 못함

    console.log(foo); // 'default string'
    ```
- null 병합 연산자는 `null` 또는 `undefined`인 경우가 아니면 좌항의 피연산자를 그대로 반환함

    ```js
    var foo = '' ?? 'default string'; // ''를 참조함

    console.log(foo); // ""
    ```
