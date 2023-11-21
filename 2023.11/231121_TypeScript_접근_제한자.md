## TypeScript 접근 제한자

-   클래스 기반 객체 지향 언어가 지원하는 접근 제한자(Access modifier)
-   `public`, `private`, `protected`를 지원하며 의미 또한 동일하다.
-   접근 제한자를 명시하지 않았을 때

    -   다른 클래스 기반 언어 : protected로 지정
    -   typescript : public으로 지정

```ts
class Foo {
    public x: string;
    protected y: string;
    private z: string;
    constructor(x: string, y: string, z: string) {
        // public,protected,private **모두 클래스 내부에서 참고 가능.**
        this.x = x;
        this.y = y;
        this.z = z;
    }
}
// 클래스 인스턴스를 통해 클래스 외부 참조
const foo = new Foo('x', 'y', 'z');
console.log(foo.x); // 참조 가능
console.log(foo.y); // 참조 불가능
console.log(foo.z); // 참조 불가능

// 자식 클래스 내부에 참조
class Bar extends Foo {
    constructor(x: string, y: string, z: string) {
        super(x, y, z);
        console.log(this.x); // 참조 가능
        console.log(this.y); // 참조 가능
        console.log(this.z); // 참조 불가능
    }
}
```

## 생성자 파라미터에 접근 제한자 선언

-   생성자 파라미터에도 접근 제한자를 선언할 수 있다.
-   접근 제한자가 사용된 생성자 파라미터는 암묵적으로 클래스 프로퍼티로 선언되고 생성자 내부에서 별도의 초기화가 없어도 암묵적으로 초기화가 수행된다.

```ts
class Foo {
    // public으로 x는 클래스 외부에서도 참조가 가능하다.
    constructor(public x: string) {}
}
const foo = new Foo('Hello');
console.log(foo); // Foo {x:'Hellow'}
console.log(foo.x); // Hello

class Bar {
    // private으로 클래스 내부에서만 참조 가능하다.
    constructor(private x: string) {}
}
const bar = new Bar('Hello');
console.log(bar); // Bar {x:'Hello'}
console.log(bar.x); // 참조 불가
```

-   만약 생성자 파라미터에 접근 제한자를 선언하지 않으면 생성자 내부에서만 유효한 지역변수가 되어 외부에서 참조 불가능하다.

## static 키워드

-   ES6 클래스에서 `static` 키워드는 정적(static) 메소드를 정의한다. 정적 메소드는 클래스의 인스턴스가 아닌 클래스 이름으로 호출한다.
-   클래스의 인스턴스를 생성하지 않아도 호출 할 수 있다.

```ts
class Foo {
    constructor(prop) {
        this.prop = prop;
    }

    static staticMethod() {
        // 정적메소드 내부에서 this는 클래스의 인스턴스가 아니라 자신을 가리키기 때문에 사용할 수 없다.
        return 'staticMethod';
    }
    prototypeMethod() {
        return this.prop;
    }
}

// 정적 메소드는 클래스 이름으로 호출한다.
console.log(Foo.staticMethod());
const foo = new Foo(123);
// 정적 메소드는 인스턴스로 호출할 수 없다.
console.log(foo.staticMethod()); // uncaught TyperError
```

-   Typescript에서는 `static` 키워드를 클래스 프로퍼티에도 사용할 수 있다.

```ts
class Foo {
    static instanceCounter = 0;
    constructor() {
        // 생성자가 호출될 때마다 카운터를 1씩 증가시킨다.
        Foo.instanceCounter++;
    }
}
var foo1 = new Foo();
var foo2 = new Foo();
console.log(Foo.instanceCounter); //2
console.log(foo2.instanceCounter); // error
```

## 출처

https://velog.io/@wjd489898/Typescript-%ED%81%B4%EB%9E%98%EC%8A%A4Class-private-protected-public
