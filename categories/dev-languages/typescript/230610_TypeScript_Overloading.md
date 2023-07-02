# TypeScript Overloading

## Overloading이란?

- 동일한 이름에 매개 변수만 다른 여러 버전의 함수를 만드는 것
- 파라미터의 형태가 다양한 여러 케이스에 대응하는 같은 이름을 가진 함수를 만드는 것
- 함수의 다형성(다양한 형태)을 지원하는 것
- function 키워드로만 함수 오버로딩을 할 수 있으며 arrow function으로는 오버로딩을 할 수 없음

## Overloading 하는 이유

- 파라미터만 달라지고, 비슷한 로직이 반복되는 경우에 사용할 수 있음
- 코드의 중복을 줄이고 재사용성을 높일 수 있음

```ts
const addZero = (num: number) => (num > 9 ? "" : "0") + num;

function formatDate(date: Date, format = "yyyyMMdd"): string {
  const yyyy = date.getFullYear().toString();
  const MM = addZero(date.getMonth() + 1);
  const dd = addZero(date.getDate());
  return format.replace("yyyy", yyyy).replace("MM", MM).replace("dd", dd);
}

function formatDateString(dateStr: string, format = "yyyyMMdd"): string {
  const date = new Date(dateStr);
  const yyyy = date.getFullYear().toString();
  const MM = addZero(date.getMonth() + 1);
  const dd = addZero(date.getDate());
  return format.replace("yyyy", yyyy).replace("MM", MM).replace("dd", dd);
}

function formatDateTime(datetime: number, format = "yyyyMMdd"): string {
  const date = new Date(datetime);
  const yyyy = date.getFullYear().toString();
  const MM = addZero(date.getMonth() + 1);
  const dd = addZero(date.getDate());
  return format.replace("yyyy", yyyy).replace("MM", MM).replace("dd", dd);
}
```

## 주의할 점

- 함수의 이름은 같아야 함
- 매개변수가 추가되는 것은 괜찮지만 순서는 반드시 지켜야 함

```ts
// 문제 없는 함수 오버로딩 선언
class User {
  constructor(private id: string) {}
  setId(id: string): string;
  setId(id: number): string;
}

// Error
class User {
  constructor(private id: string) {}
  // 선언 시에 에러는 나지 않지만 오버로딩 함수 정의 시에 에러
  setId(id: string): void;
  setId(id: string): number; // 반환 타입 다름
  setId(radix: number, id: number): void; // 인수 순서 다름
}
```

## Overloading 구현

### 1. 매개변수의 개수가 같을 때

```ts
class User {
  constructor(private id: string) {}

  setId(id: string): void;
  setId(id: number): void;

  // 유니온 타입으로 선언 & 타입 가드
  setId(id: string | number): void {
    this.id = typeof id === "number" ? id.toString() : id; // 타입 가드
  }
}
```

### 2. 매개변수의 개수가 다를 때

```ts
class User {
  constructor(private id: string) {}

  setId(id: string): void;
  setId(id: number, radix: number): void;

  // 유니온 타입으로 선언 & 옵셔널 & 타입 가드
  setId(id: string | number, radix?: number): void {
    // radix는 number or undefined
    this.id = typeof id === "number" ? id.toString(radix) : id;
  }
}
```

## Generic Type과의 차이점

- 타입을 추론할 수 있는 시점과 용도의 범위
  ![타입추론](../../_image/overloading.png)
- 함수 파라미터에 들어갈 타입을 알고 있고, 파라미터 타입만 달라지고 함수의 로직이 반복된다면 함수 오버로딩 사용
- 어떤 타입이 올지 모르겠고, 타입을 다양한 용도에서 사용하고 싶다면 제네릭 사용
