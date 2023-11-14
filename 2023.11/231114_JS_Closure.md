# 클로져란

## 1. 클로져란?

- 반환된 내부함수가 자신이 선언됐을 때의 환경(Lexical environment)인 스코프를 기억하여, 만일 자신이 선언됐을 때의 환경(스코프) **밖에서 호출되어도 스코프에 접근**할 수 있는 함수

<br>

```jsx
function outerFunc() {
  var x = 10;
  var innerFunc = function () {
    console.log(x);
  };
  innerFunc();
}

outerFunc(); // 10
```

1. 함수 `outerFunc` 내에서 내부함수 `innerFunc`가 선언되고 호출됨
2. 내부함수 `innerFunc`는 자신을 포함하고 있는 외부함수 `outerFunc`의 변수 `x`에 접근 가능
3. 이는 함수 `innerFunc`가 함수 `outerFunc`의 내부에 선언되었기 때문

<br>

- 함수 `innerFunc`가 함수 `outerFunc`의 내부에서 선언되었기 때문에 함수 의 상위 스코프는 함수
- 함수 `innerFunc`가 함수 `outerFunc`의 내부에 선언된 내부함수이므로 함수 `innerFunc`는 자신이 속한 렉시컬 스코프(전역, 함수 `outerFunc`, 자신의 스코프)를 참조 가능

<br>

- 내부함수 `innerFunc`를 함수 `outerFunc` 내에서 호출하는 것이 아니라 반환하는 경우

  ```jsx
  function outerFunc() {
    var x = 10;
    var innerFunc = function () {
      console.log(x);
    };
    return innerFunc();
  }

  // 함수 outerFunc를 호출하면 내부 함수 innerFunc가 반환된다.
  // 그리고 함수 outerFunc의 실행 컨텍스트는 소멸된다.

  var inner = outerFunc();
  inner(); // 10
  ```

  - 함수 `outerFunc`는 내부함수 `innerFunc`를 반환하고 **생을 마감** 함
  - 함수 `outerFunc`는 실행된 이후 콜스택(실행 컨텍스트 스택)에서 제거되었으므로 함수 `outerFunc`의 변수 `x` 또한 더이상 유효하지 않게 되어 변수 `x`에 접근할 수 있는 방법은 달리 없어 보임

  <br>

  - 그러나 위 코드의 **실행 결과는 변수 `x`의 값인 10**
  - 이미 life-cycle이 종료되어 실행 컨텍스트 스택에서 제거된 함수 `outerFunc`의 지역변수 **`x`가 다시 부활이라도 한 듯이** 동작함

<br>

- **자신을 포함하고 있는 외부함수보다 내부함수가 더 오래 유지되는 경우**, 외부 함수 밖에서 내부함수가 호출되더라도 **외부함수의 지역 변수에 접근**할 수 있는데 이러한 함수를 **클로저(Closure)** 라고 부름
