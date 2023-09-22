# DFS/BFS (2)

### 1.1. 스택(Stack)

- **선입후출(First In Last Out) 구조 또는 후입 선출(Last In First Out) 구조**

```javascript
let stack = [];

// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.push(5);
stack.push(2);
stack.push(3);
stack.push(7);
stack.pop();
stack.push(1);
stack.push(4);
stack.pop();

console.log(stack); // 최하단 원소부터 출력
console.log(stack.reverse()); // 최상단 원소부터 출력
```

```bash
[5, 2, 3, 1]
[1, 3, 2, 5]
```

<br>

### 1.2. 큐(Queue)

- **선입선출(First In First Out) 구조**

```javascript
let queue = [];

// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.push(5);
queue.push(2);
queue.push(3);
queue.push(7);
queue.shift();
queue.push(1);
queue.push(4);
queue.shift();

console.log(queue); // 먼저 들어온 순서대로 출력
queue.reverse(); // 다음 출력을 위해 역순으로 바꾸기
console.log(queue); // 나중에 들어온 원소부터 출력
```

```bash
[3, 7, 1, 4]
[4, 1, 7, 3]
```

<br>

### 1.3. 재귀 함수(Recursive Function)

- **자기 자신을 다시 호출하는 함수**

```javascript
// 재귀 함수 예제

function recursiveFunction() {
  console.log("재귀 함수를 호출합니다.");
  recursiveFunction();
}

recursiveFunction();
```

- '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력

<br>

#### 1.3.1. 재귀 함수의 종료 조건

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 반드시 명시해야 함

```javascript
// 재귀 함수 종료 예제

function recursiveFuction(i) {
  // 100번째 출력했을 때 종료되도록 종료 조건 명시
  if (i === 100) {
    return;
  }
  console.log(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.");
  recursiveFuction(i + 1);
  console.log(i, "번째 재귀 함수를 종료합니다.");
}

recursiveFuction(1);
```

- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조 이용
  - 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
- 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있음 ex) DFS

<br>

- 재귀 함수를 이용하는 대표적인 예제로 **팩토리얼(Factorial)** 문제가 있음
- 수학적으로 0!과 1!의 값은 1로 같다는 성질을 이용하여 팩토리얼 함수는 n과 1 이하가 되었을 때 함수를 종료하는 재귀 함수의 형태로 구현 가능

```javascript
// 반복적으로 구현한 n!
function factorialIterative(n) {
  let result = 1;
  // 1부터 n까지의 수를 차례대로 곱하기
  for (let i = 1; i < n + 1; i++) {
    result += 1;
  }
  return result;
}

// 재귀적으로 구현한 n!
function factorialRecursive(n) {
  // n이 1 이하인 경우 1을 반환
  if (n <= 1) {
    return 1;
  }
  // n! = n * (n - 1)!을 그대로 코드로 작성하기
  return n * factorialRecursive(n - 1);
}

// 각각의 방식으로 구현한 n! 출력(n = 5)
print("반복적으로 구현:", factorialIterative(5));
print("재귀적으로 구현:", factorialRecursive(5));
```

```bash
반복적으로 구현: 120
재귀적으로 구현: 120
```

- 실행 결과는 동일
- 재귀 함수의 코드가 더 간결함
  - 재귀 함수가 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문
