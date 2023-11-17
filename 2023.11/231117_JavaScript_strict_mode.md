# JavaScript Strict mode

<aside>
✅ 자바스크립트의 일반적인 코드와는 다른 시맨틱을 가지는 모드로, 문법과 에러를 엄격하게 처리하는 모드입니다.

</aside>

<aside>
✅ **꼬리 질문 1 : Strict mode를 적용하면 어떤 점이 달라지나요?**
기존에는 무시되던 에러를 발생시키거나, 자바스크립트 엔진 최적화 작업을 어렵게 만드는 실수를 바로잡고, ECMAScript 차기 버전에서 정의되는 문법들을 금지합니다.

**꼬리 질문 2 : use strict는 어떻게 사용하나요?**
전체 스크립트에 적용하려면 스크립트 최상단에 `use strict;`를 작성합니다. 또는 함수마다 개별로 적용할 수도 있습니다.

</aside>

## 1. Strict mode

- ES5부터 사용 가능한 모드
- Strict mode에서는 일반적인 자바스크립트 규칙에서 몇 가지를 수정함

1. 기존에는 조용히 무시되던 에러들을 throwing함
2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 바로잡음
3. ECMAScript의 차기 버전들에서 정의 될 문법을 금지함

## 2. Strict mode를 적용하는 방법 : `use strict`

- 전체 스크립트에 적용하기 위해 `"use strict";` 를 다른 구문 작성 전(최상단)에 삽입함
  ```jsx
  // 전체 스크립트 Strict mode 구문
  'use strict';
  var v = "Hi!  I'm a strict mode script!";
  ```
- 함수에 적용하기 위해 함수 본문 처음에 `"use strict";` 를 삽입함
  ```jsx
  function strict() {
    // 함수-레벨 strict mode 문법
    'use strict';
    function nested() {
      return 'And so am I!';
    }
    return "Hi!  I'm a strict mode function!  " + nested();
  }
  function notStrict() {
    return "I'm not strict.";
  }
  ```
