# require과 import

## CommonJS와 ES6

- CommonJS는 2009년에 만들어진 표준으로 **자바스크립트 모듈을 만들기 위한 법칙**
- 오로지 서버사이드 모듈을 만들고 불러오기 위해 개발됨
- 2010년에는 제대로 된 모듈시스템이 없어서 클라이언트에도 쓰이곤 했음
- ECMA는 **ES6부터 모듈화를 지원하기 시작함**

## require과 import 문법

- 둘다 외부의 파일이나 라이브러리의 코드를 불러온다는 같은 목적을 가지고 있지만 전혀 다른 문법 구조를 지니고 있음
- `require` / `exports`는 NodeJS에서 사용되고 있는 CommonJS 키워드
- `import` / `export`는 ES6(ES2015)에서 새롭게 도입된 키워드

## require과 import의 주요 차이점

- `require`는 CommonJS를 사용하는 node.js문이지만 `import`는 ES6에서만 사용
- `require`는 프로그램의 어느 지점에서나 호출 할 수 있지만 `import`는 파일의 시작 부분에서만 실행할 수 있음 (그렇지만 `import` 전용 비동기 문법으로 파일 중간에 모듈 불러오기를 할 수 있음)
- 하나의 프로그램에서 두 키워드를 동시에 사용할 수 없음
- 일반적으로 `import`는 사용자가 필요한 모듈 부분만 선택해 로드 할 수 있고 `require`보다 성능이 우수하며 메모리를 절약해 선호됨

## 모듈 내보내기 / 가져오기

- CommonJS (`require` / `exports`)

  ```js
  // 모듈 전체를 export, 파일내 한번만 사용가능하다.
  const obj = {
    num: 100,
    sum: function (a, b) {
      console.log(a + b);
    },
    extract: function (a, b) {
      console.log(a - b);
    },
  };

  module.exports = obj;
  ```

  ```js
  const obj = require('./exportFile.js');

  obj.num; // 100
  obj.sum(10, 20); // 30
  obj.extract(10, 20); // -10
  ```

- ES6 (`import` / `export`)

  ```js
  // 모듈 전체를 export, 파일내 한번만 사용가능하다.
  const obj = {
    num: 100,
    sum: function (a, b) {
      console.log(a + b);
    },
    extract: function (a, b) {
      console.log(a - b);
    },
  };

  export default obj;
  ```

  ```js
  // 전체 자체를 import 할 경우 중괄호 없이 그냥 씀
  import obj from './exportFile.js';

  obj.num; // 100
  obj.sum(10, 20); // 30
  obj.extract(10, 20); // -10
  ```

## 모듈 개별 내보내기 / 가져오기

- CommonJS (`require` / `exports`)

  ```js
  // 멤버를 직접 일일히 export
  exports.name = 'Ann'; // 변수의 export
  exports.sayHello = function () {
    // 함수의 export
    console.log('Hello World!');
  };
  exports.Person = class Person {
    // 클래스의 export
    constructor(name) {
      this.name = name;
    }
  };
  ```

  ```js
  const { name, sayHello, Person } = require('./exportFile.js');

  console.log(name); // Ann
  sayHello(); // Hello World!
  const person = new Person('inpa');
  ```

- ES6 (`import` / `export`)

  ```js
  // 멤버를 따로 묶어서 export
  const name = 'Ann';
  function sayHello() {
    console.log('Hello World!');
  }
  class Person {
    constructor(name) {
      this.name = name;
    }
  }
  export { name, sayHello, Person }; // 변수, 함수, 클래스를 하나의 객체로 구성하여 export
  ```

  ```js
  import { name, sayHello, Person } from './exportFile.js';

  console.log(name); // Ann
  sayHello(); // Hello World!
  const person = new Person('inpa');

  // ----------------- OR ----------------- //

  // as 키워드를 사용해 전체를 import 한 것처럼 사용 가능
  import * as obj from './exportFile.js';

  console.log(obj.name); // Ann
  obj.sayHello(); // Hello World!
  const person = new obj.Person('inpa');
  ```

## 정리

- 두 키워드 모두 동일한 목적을 가지고 있지만 다른 문법구조를 가지고 있음
- **Babel**과 같은 자바스크립트 트랜스파일러를 통해 `import` 구문을 사용할 수 있음
- ex) React에서 라이브러리 사용하기
  - 번들링을 위해 사용하는 webpack은 node.js 환경에서 구동하므로 `require`을 사용해야 함
  - 하지만 리액트 라이브러리를 사용할 때는 babel에서 `imoprt` 구문을 `require` 구문으로 변환해 주기 때문에 `import` 구문을 사용할 수 있음
