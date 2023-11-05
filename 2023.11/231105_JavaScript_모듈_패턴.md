# JavaScript 모듈 패턴

프로그래밍에는 코드를 좀 더 우아하고 아름답게 혹은 간결하고 깔끔하게 만들어주는 많은 패턴들이 존재한다. 이러한 디자인 패턴들은 프로그램의 아키텍쳐를 어떻게하면 더욱 아름답게 만들 수 있을까하는 고민과 함께 오랜 시간 전부터 존재해왔다. 오늘은 자바스크립트에서 자주 사용되는 패턴 중 하나인 모듈 패턴에 대해 소개하려고 한다. 모듈 패턴은 아주 간단하지만 매우 강력한 패턴 중 하나라 알아두면 좋을 것 같다.

## 클로져란 무엇인가?

클로져는 이미 실행이 종료된 함수의 변수나 함수를 참조할 수 있는 링크를 가진 내부 함수를 뜻한다. 클로져를 설명할 때 아주 단골처럼 등장하는 예시를 하나 가져왔다.

```js
function outer(x) {
  function inner(y) {
    return x + y;
  }
  return inner;
}
const inner = outer(5);
inner(3); // 5 + 3 == 8
```

inner 라는 함수는 x 를 입력 값으로 받는 외부 함수인 outer 함수에 의해 둘러 쌓여있다. 내부 함수 역시 y 를 입력 값으로 받는다. 그리고 두 개를 더한 값을 반환한다.

여기서 inner 함수를 살펴보면 못 보던 클로져라고 하는 스코프가 하나 보인다. 이 클로져 스코프는 outer 함수를 가리키고 있다. outer 함수는 이미 사용이 종료된 함수기에 외부에서는 접근이 불가능하다.

## 모듈 패턴

그래서 우리는 오직 내부 함수에서만 접근이 가능한 클로져의 특성을 이용해서 모듈 패턴을 구현할 것이다.

```js
function jane() {
  const name = 'jane';
  const mid = 'A';
  const final = 'B+';
  return {
    midtermScore: () => mid,
    finaltermScore: () => final,
  };
}
jane().midtermScore(); // A
jane().finaltermScore(); // B+
```

이 예제에서 학생 jane 의 중간고사와 기말고사 점수는 그 어떠한 이유를 막론하고 변경되면 안된다. jane 은 함수를 값으로 담고 있는 프로퍼티들을 담은 객체를 반환하고 있다. jane 의 스코프 밖에서 바라볼 때 jane 의 그 어떠한 프로퍼티에도 접근을 할 수 없는게 정상이다.

클로져는 잘못된 방법으로 남용하게 될 경우 메모리 누수를 유발하기 쉽다고 알려져 있다. 아주 틀린 말은 아니다. 그러나 클로져는 그럼에도 불구하고 값의 은닉화에 있어 아주 적합한 녀석이다. 위의 예제에서 만약 jane 의 시험 점수를 바꾸고 싶다면, jane 이 반환하는 객체에 점수를 바꿀 수 있는 메소드를 추가하면 된다.

```js
return {
  getMid: () => mid,
  getFinal: () => final,
  setMid: (score) => (mid = score),
  setFinal: (score) => (final = score),
};
```

jane 의 시험 점수는 오로지 이 메소드들을 통해서만 가능하다.

## IIFE 와 같이 사용하는 방법

주로 모듈 패턴은 IIFE 와 같이 사용된다. IIFE 역시 외부에서는 접근이 불가능한 독립적인 스코프를 갖고 있다.

```js
var stories = 'Medium Story';
var medium = (function () {
  var stories = ['🍔', '🍟', '🍕'];
  return { getStories: stories };
})();
```

IIFE 의 좋은 점은, 스코프가 겹치지 않기 때문에 같은 이름의 변수가 존재한다고 해도 외부 스코프와 충돌할 문제가 전혀 없다는 것이다. 게다가 클로져를 이용하면 private 한 변수나 함수를 만드는 것도 가능하다.

```js
console.log(stories); // Medium Story
console.log(medium.getStories()); // ['🍔', '🍟', '🍕']
console.log(medium.stories); // undefined
```

여기서 stories 는 함수 내에서만 존재하는 값이므로 외부에서 직접 접근이 불가능하다. stories 에 접근하는 유일한 방법은 getStories 를 이용하는 것 뿐이다.

Export 키워드를 이용한 방법
ES6 의 등장 이후부터 모듈 패턴을 구현하는 방법이 굉장히 간단해졌다. 하나 이상의 방법이 존재하지만, 기본적인 컨셉은 모두 “코드를 다른 파일에 담아 보관한다” 라고 볼 수 있다.

```js
const stories = ['🍔', '🍟', '🍕'];
const getStories = () => stories;
export { getStories };
```

라는 코드가 어떤 파일에 있으면, 다른 파일에서 이 파일을 로드한다.

```js
import { getStories } from '..';
const stories = 'Medium Story';
console.log(stories); // Medium Story
console.log(getStories(); // ['🍔', '🍟', '🍕']
```

## 자바스크립트 클래스를 이용한 방법

ES2020 에는 `#` 키워드를 이용해서 private 를 구현해낼 수 있는 방식이 추가되었다.

```js
const stories = 'Medium Story';
class Medium {
  #stories = ['🍔', '🍟', '🍕'];
  get Stories() {
    return this.#stories;
  }
}
const medium = new Medium();
console.log(stories); // Medium Story
console.log(medium.Stories); // ['🍔', '🍟', '🍕']
console.log(medium.#stories);
// Uncaught SyntaxError: Private field '#stories' must be declared in an enclosing class
```

대신, 갓 나온 아주 따끈따끈한 기능이므로 타 브라우저의 브라우저 호환을 반드시 확인하고 사용할 것을 권장한다.

## 보너스: 타입스크립트를 이용한 방법

타입스크립트를 이용하면 클래스를 이용해서 매우 쉽게 풀어낼 수 있다.

```js
const stories = 'Medium Story';
class Medium {
    private stories = ['🍔', '🍟', '🍕'];
    get Stories() {
    return this.stories;
    }
}
const medium = new Medium();
console.log(stories); // Medium Story
console.log(medium.Stories); // ['🍔', '🍟', '🍕']
console.log(medium.stories); // ['🍔', '🍟', '🍕']
// Property 'stories' is private and only accessible within class 'Medium'
```

근데 여기서 뭔가 이상한 점이 있다. medium.stories 가 분명 private 으로 되어 있는데 값이 출력됐다. 사실 이는 정상적인 동작인데, private 은 자바스크립트에는 없는 키워드고, 타입스크립트에만 존재하는 키워드다. 그래서 타입스크립트가 private 을 자바스크립트로 트랜스파일 할 때는 사실상 아무것도 특별한 무언가를 하지 않는다.

타입스크립트는 대신 코딩할 때 에러를 보여주면서 잘못된 방식이라는 것을 알려줄 뿐이다. 그래서 사실 이 에러를 수정하지 않으면 안되게끔 만든다. 그래서 private 이 붙은 타입스크립트 클래스는 일반 자바스크립트 클래스와 빌드 결과가 똑같다고 볼 수 있다. 사실 이것 마저도 아래처럼 주석을 달면 에러가 사라진다.

```js
// @ts-ignore
console.log(medium.stories);
// 에러는 사라진다
```

따라서 타입스크립트는 휴먼에러를 좀 더 편하게 잡기 위함이라고 보면 되고 타입스크립트의 private 은 사실상의 자바스크립트 모듈 패턴의 코드를 생성하지는 않는다. 다만 코딩하는 그 시점에서 모듈 패턴을 사용하려는 의도에서 약간의 실수가 발생할 경우 그것을 에러를 보여주면서 바로 잡아줄 수는 있다.

## 정리

모듈 패턴은 자바스크립트에서 정말 유용하고 강력한 패턴이다. 모듈 패턴은 변수와 함수를 외부로부터 감추고 보호한다. 그리고 이 패턴의 근간에는 클로져가 있다.

## 출처

https://medium.com/%EC%98%A4%EB%8A%98%EC%9D%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-%EB%AA%A8%EB%93%88-%ED%8C%A8%ED%84%B4-d5ba2c94eeb5
