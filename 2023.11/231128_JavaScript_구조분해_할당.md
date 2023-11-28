# JavaScript 구조분해 할당

<aside>
✅ 구조분해 할당은 ES6부터 도입된 문법으로 **객체나 배열을 분해해 변수 할당을 편리하게 할 수 있는 문법**입니다.

</aside>

## 1. 구조분해 할당이란?

-   객체나 배열을 분해해 변수 할당을 편리하게 할 수 있는 문법
-   구조분해 할당을 통해 변수 선언에 반복되는 코드를 단축할 수 있음

## 2. 구조분해 할당 방법 (코드로 이해하기)

### 1. 객체 구조분해 할당

```jsx
const obj = { a: 123, b: { c: 456, d: 789 } };
```

-   일반적인 할당
    ```jsx
    const a = obj.a;
    const d = obj.b.d;
    ```
-   구조분해 할당 : 키를 맞춰 작성
    ```jsx
    const {
        a,
        b: { d },
    } = obj;
    ```

### 2. 배열 구조분해 할당

```jsx
const x = arr[0];
const y = arr[4];
```

-   일반적인 할당
    ```jsx
    const arr = [1, 2, 3, 4, 5];
    ```
-   구조분해 할당 : 인덱스를 맞춰 작성
    ```jsx
    const [x, , , , z] = arr;
    ```

## 3. 주의 사항

-   `this`가 사용되는 객체에는 구조분해 할당을 사용하지 않는 것을 권장함
    -   사용 위치에 따라 `this`가 가리키는 대상이 달라지기 때문

```jsx
const candyMachine = {
    status: {
        name: 'node',
        count: 5,
    },
    getCandy() {
        this.status.count--;
        return this.status.count;
    },
};

// 위 객체를 구조분해 할당할 경우 getCandy()와 candyMachine.getCandy()의 실행 결과가 다름
const {
    getCandy,
    status: { count },
} = candyMachine;
```
