# reduce()란?

```
✅ reduce() 메서드는 배열의 각 요소에 대해 주어진 리듀서(reducer) 함수를 실행하고, 하나의 결과값을 반환합니다.
리듀서 함수는 누산기, 현재 값, 현재 인덱스, 원본 배열의 총 4개의 인자를 받습니다.
리듀서 함수는 각 단계에서 현재 요소와 누산된 결과를 기반으로 새로운 값을 계산하고, 이 값을 누산기에 할당합니다.
이 과정은 배열의 모든 요소에 대해 반복되며, 누산기는 이전 결과를 유지하면서 최종적으로 하나의 값을 반환합니다.
이 방식으로 reduce()는 배열을 단일 값으로 축소하는 강력한 도구로 사용됩니다.
```

<br><br>

## 0. mdn 문서

[mdn 문서 - reduce() 가장 정확하게 설명](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

<br><br>

## 1. `reduce()`란?

- **배열의 왼쪽부터 콜백 함수를 실행 후 누산함**
  ```jsx
  배열.reduce(function(acc, cur, index, arr) {
  }[,initialValue])
  ```
  - 누산기accumulator (`acc`)
  - 현재 값 (`cur`)
  - 현재 인덱스 (`idx`)
  - 원본 배열(`src`)
  - `initialValue`(optional) : callback의 최초 호출에서 **첫 번째 인수에 제공하는 값**
    - 초기값을 제공하지 않으면 **배열의 첫 번째 요소를 사용**
    - 빈 배열에서 초기값 없이 `reduce()` 호출하면 오류 발생
- 예시

  ```jsx
  const numbers = [1, 2, 3, 4];

  // 일반 for문
  let result = 0;
  for (i = 0; i < numbers.length; i++) {
    result += numbers[i];
  }
  console.log(result); // 20;

  //-----------------------------------------

  const result = numbers.reduce((number1, number2) => number1 + number2);
  /* 
    1,2 => 3  배열값 1번째, 2번째 부터 시작
    3,3 => 6
    6,4 => 10
  */
  console.log(result); // 10;

  //-------------------------------------------

  const result = numbers.reduce((number1, number2) => number1 + number2, 10);
  /* 
    10,1 => 11   initialValue값, 배열값 1번째 부터 시작
    11,2 => 13
    13,3 => 16
    16,4 => 20
  */
  console.log(result); // 20;
  ```

  ```jsx
  // 다른 산술 결과도 가능
  const numbers = [1, 2, 3, 4];

  const sumByPlus = numbers.reduce((number1, number2) => number1 + number2);
  const sumByMinus = numbers.reduce((number1, number2) => number1 - number2);
  const sumByMulti = numbers.reduce((number1, number2) => number1 * number2);

  console.log(sumByPlus); // 10
  console.log(sumByMinus); // -8
  console.log(sumByMulti); // 24
  ```

<br><br>

## 2. reduce의 `initialValue` 속성

### 2.1. `initialValue` 값이 없는 경우

```jsx
var res = [0, 1, 2, 3, 4].reduce(function (
  accumulator,
  currentValue,
  currentIndex,
  array
) {
  console.log(`accumulator : ${accumulator}`);
  console.log(`currentValue : ${currentValue}`);
  console.log(`currentIndex : ${currentIndex}`);
  console.log("                              ");
  return accumulator + currentValue;
});

console.log("res:", res); // 10
```

- `initialValue`를 제공하지 않으면, `reduce()`는 **인덱스 1부터 시작해** 콜백 함수를 실행하고 첫 번째 인덱스는 건너 뜀
  - accumulator는 배열의 첫 번째 값
  - currentValue는 배열의 두 번째 값
- 콜백은 4번 호출됨
  | callback | accumulator | currentValue | currentIndex | array | 반환 값 |
  | ---------- | ----------- | ------------ | ------------ | --------------- | ------- |
  | 1번째 호출 | 0 | 1 | 1 | [0, 1, 2, 3, 4] | 1 |
  | 2번째 호출 | 1 | 2 | 2 | [0, 1, 2, 3, 4] | 3 |
  | 3번째 호출 | 3 | 3 | 3 | [0, 1, 2, 3, 4] | 6 |
  | 4번째 호출 | 6 | 4 | 4 | [0, 1, 2, 3, 4] | 10 |

<br><br>

### 2.2. `initialValue` 값이 있는 경우

```jsx
var res = [0, 1, 2, 3, 4].reduce(function (
  accumulator,
  currentValue,
  currentIndex,
  array
) {
  console.log(`accumulator : ${accumulator}`);
  console.log(`currentValue : ${currentValue}`);
  console.log(`currentIndex : ${currentIndex}`);
  console.log("                              ");
  return accumulator + currentValue;
},
10); // 누산기 초깃값 10을 주었다.

console.log("res:", res); //20
```

- `initialValue`를 제공하면 **인덱스 0에서** 시작
  - accumulator는 `initalValue`
  - currentValue는 배열의 첫 번째 값
- 콜백은 5번 호출됨
  | callback | accumulator | currentValue | currentIndex | array | 반환 값 |
  | ---------- | ----------- | ------------ | ------------ | --------------- | ------- |
  | 1번째 호출 | 10 | 0 | 0 | [0, 1, 2, 3, 4] | 10 |
  | 2번째 호출 | 10 | 1 | 1 | [0, 1, 2, 3, 4] | 11 |
  | 3번째 호출 | 11 | 2 | 2 | [0, 1, 2, 3, 4] | 13 |
  | 4번째 호출 | 13 | 3 | 3 | [0, 1, 2, 3, 4] | 16 |
  | 5번째 호출 | 16 | 4 | 4 | [0, 1, 2, 3, 4] | 20 |
