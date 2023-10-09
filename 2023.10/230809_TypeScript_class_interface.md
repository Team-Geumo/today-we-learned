## 1. Class

- TS를 객체지향 코드를 배워보기
- TS를 통해 코드를 재사용 (반복되는 코드 제거)하는 방법 알아보기
  - 파라미터만 작성하면 constructor을 알아서 작성해줌
  - public, private, protected 속성은 TS에서만 적용되고 JS에서는 적용되지 않음
    - TS에서는 보호 차원에서 에러를 띄워줌
    - JS에서는 속성을 무시하고 코드가 작동함 (모두 public 인 것처럼)
  ```tsx
  // 추상 클래스 : 다른 클래스가 상속받을 수 있는 클래스
  abstract class User {
    constructor(
      private firstName: string,
      private lastName: string,
      protected nickName: string,
    ) {}
    getFullName() {
      // 여기에도 public, private, protected 속성 추가 가능
      return `${this.firstName} ${this.lastName}`;
    }
    // 추상 메서드 : 추상 클래스를 상속 받는 모든 클래스가 구현해야 하는 메서드
    // 직접 구현하지 않고 call signature만 작성해야 함
    abstract getNickName(): void;
  }
  // 추상 클래스는 직접 인스턴스를 만들 수 없음 (only 다른 클래스에 상속만 가능)
  // const hy = new User("hy", "kim", "호롱") // Error

  class Player extends User {
    getNickName() {
      console.log(this.nickName); // TS에서 protected 설정해줬기 때문에 접근 가능
    }
  }

  const hy = new Player('hy', 'kim', '호롱');

  // hy.firstName // compile ERROR : TS에서 private 설정해줘서 접근 불가능
  // hy.nickName // compile ERROR : TS에서 protected 설정해줘서 접근 불가능
  hy.getFullName();
  ```
- 위 코드를 JS로 컴파일 하면?
  ```jsx
  'use strict';
  class User {
    constructor(firstName, lastName, nickName) {
      this.firstName = firstName;
      this.lastName = lastName;
      this.nickName = nickName;
    }
    getFullName() {
      return `${this.firstName} ${this.lastName}`;
    }
  }
  class Player extends User {
    getNickName() {
      console.log(this.nickName);
    }
  }
  const hy = new Player('hy', 'kim', '호롱');
  hy.getFullName();
  ```
- 객체 속성 정리하기
  - abstract class (추상 클래스)
    - 다른 클래스가 상속받을 수 있는 클래스
    - 오로지 상속만 가능하고, 직접 사용해 인스턴스를 만들 수는 없음
  - abstract method (추상 메서드)
    - 추상 클래스를 상속 받는 모든 클래스가 구현해야 하는 메서드
    - 구현되어있지 않은(=== 코드가 없는) 메서드
    - call signature만 존재할 수 있음
  - public
    - 클래스 내부, 상속받은 클래스, 클래스 외부에서 모두 사용 가능
  - private
    - 클래스 내부에서만 사용 가능, 상속받은 클래스나 클래스 외부에서 사용 불가능
  - protected
    - 클래스 내부와 상속받은 클래스에서 사용 가능, 클래스 외부에서만 사용 불가능
- ex) Dict : 단어의 뜻을 찾고 단어를 추가할 수 있는 class로 만들기
  ```tsx
  type Words = {
    [key: string]: string; // 제한된 양의 property 혹은 key를 가지는 타입을 정의
  };

  //  1. Error : initializer가 없음
  //  class Dict {
  //    priveate words:Words
  //  }

  //  2. 원하는 형태가 아님
  //  class Dict {
  //    constructor(
  //      priveate words:Words
  //    ) {}
  //  }

  class Dict {
    private words: Words; // call signature 따로
    constructor() {
      this.words = {}; // initialize 따로
    }
    add(word: Word) {
      // class를 타입처럼 사용할 수 있음 (중요?)
      if (this.words[word.term] === undefined) {
        this.words[word.term] = word.def;
      }
    }
    def(term: string) {
      return this.words[term];
    }
    static hello() {
      // static은 JS에서도 유효한 속성임
      return 'hello';
    }
  }

  class Word {
    constructor(
      public readonly term: string, // 밖에서 읽을 수 있지만 수정은 안 됨
      public readonly def: string,
    ) {}
  }

  const kimchi = new Words('kimchi', '한국 전통 음식');

  const dict = new Dict();

  dict.add(kimchi);
  dict.def('kimchi');
  ```
- class 형태 비교하기 (in JS) : **`무슨 차이지?`**
  ```tsx
  // 1. constructor 안에 call signature 작성
  class Dict {
  	constructor(
  		priveate words:Words
  	) {}
  }

  // in JS
  "use strict"
  class Dict {
  	constructor(words) {
  		this.words = words;
  	}
  }

  // 2. constructor 밖에 call signature 작성
  class Dict {
  	constructor(
  		priveate words:Words
  	) {}
  }

  // in JS
  "use strict"
  class Dict {
  	constructor() {
  		this.words = words;
  	}
  }
  ```

## 2. Interfaces

- type vs interface
  - type : 여러가지 type 설명 및 특정 값 지정 등 여러가지 용도를 가짐
  - interface : 오직 **object의 형태를 설명하는 용도로만** 사용됨 (형식도 다름)
  ```tsx
  // type Team = string 처럼 타입만 지정할 수도 있지만
  type Team = 'red' | 'blue' | 'yellow'; // 처럼 특정 값을 지정할 수 있음
  type Health = 1 | 5 | 10;

  type Player = {
    nickName: string;
    team: Team;
    health: Health;
  };

  interface Player {
    nickName: string;
    team: Team;
    health: Health;
  }

  const hy: Player = {
    nickName,
  };
  ```
- interface는 class처럼 취급할 수 있음
  - readonly, extends 등 사용 가능
  ```tsx
  interface User {
    name: string;
  }

  interface Player extends User {}

  const hy: Player = {
    name: 'hy',
  };
  ```
  - 같은 작업을 type으로 한다면 : extends 대신 & 연산자 사용
  ```tsx
  type User = {
    name: string;
  };

  type Player = User & {
    // & : and
  };

  const hy: Player = {
    name: 'hy',
  };
  ```
- interface는 object 속성을 자동으로 합쳐줌
  ```tsx
  interface User {
    name: string;
  }
  interface User {
    nickName: string;
  }

  const hy: User = {
    name: 'hy',
    nickName: '허렁',
  };
  ```
  - 같은 작업을 type으로 한다면 : Error 발생
  ```tsx
  type User = {
    name: string;
  };
  type User = {
    // Error : type User은 이미 존재함
    nickName: string;
  };
  ```
- interface는 컴파일 하면 JS로 바뀌지 않고 사라짐 (어디서 알 수 있었지..?)

## 3. abstract class를 interface로 대체하기

- 필요성 : abscract class는 JS로 컴파일 시에 그 속성(추상화)이 남아있지 않고 일반적인 class가 됨
  - 따라서, JS로 컴파일 했을 때 사라지는 interface로 대체할 필요가 있음
  - ex) abstract class 작성
    - JS로 컴파일 시 일반 class로 바뀌어서 작성됨
  ```tsx
  abstract class User {
    constructor(protected firstName: string, protected lastName: string) {}
    abstract sayHi(name: string): string;
    abstract fullName(): string;
  }

  class Player extends User {
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    }
    sayHi(name: string) {
      return `Hi, my name is ${this.fullName()}`;
    }
  }
  ```
  - 같은 기능을 interface로 작성
    - constructor 작성하지 않음
    - `implements` : class의 extends와 동일한 역할이지만 JS에 없음 (interface나 type을 상속하는 역할)
    - interface를 상속하면 private나 protected 속성을 사용할 수 없음 : 어케 해결..?
    - class의 속성을 정해주면서 JS에서는 보이지 않음
    - interface도 type처럼 사용할 수 있음
    - interface는 new xxx 형태로 사용하지 않고 컨텐츠만 적어주면 됨 (복습 필요,, 뭔말)
  ```tsx
  interface User {
    firstName: string;
    lastName: string;
    sayHi(name: string): string;
    fullName(): string;
  }
  interface Human {
    health: number;
  }
  class Player implements User, Human {
    constructor(
      public firstName: string, // private 사용할 수 없음
      public lastNAme: string,
      public health: number,
    );
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    }
    sayHi(name: string) {
      return `Hi, my name is ${this.fullName()}`;
    }
  }

  function makeUser(user: User) {
    return 'hi';
  }

  makeUser({
    firstName: 'hy',
    lastName: 'kim',
    fullName: () => 'xx',
    sayHi: (name) => 'string',
  });
  // User은 interface기 때문에 new User과 같이 사용하지 않아도 됨 (컨텐츠만 적어주면 됨)
  ```
- 그렇다면, type도 abstract class를 대체할 수 있는지? (할 수 있다는 뉘앙스였는디,,)

## 4. Polymorphism

- ex) 로컬 스토리지 API와 같은 API를 가지는 클래스 만들기
  ```tsx
  // Storage는 이미 정의된 object
  // 다음 코드를 통해 Storage를 따라해봄
  interface SStorage<T> {
    [key: string]: T;
  }

  class LocalStorage<T> {
    // generic type을
    private storage: SStorage<T> = {}; // interface로 전달
    set(key: string, value: T) {
      this.storage[key] = value;
    }
    remove(key: string) {
      delete this.storage[key];
    }
    get(key: string): T {
      return this.storage[key];
    }
    clear() {
      this.storage = {};
    }
  }

  const stringStorage = new LocalStorage<string>(); // generic type이 string

  stringStorage.get('ket');

  const booleanStorage = new LocalStorage<boolean>();

  booleanStorage.get('xx');
  booleanStorage.set('hello', true);
  ```
