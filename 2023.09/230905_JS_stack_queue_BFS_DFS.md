# [JavaScript] Stack, Queue, BFS, DFS

## 1. Stack (스택)

- First In Last In
- 먼저 들어간 것이 나중에 나온다
- 자바스크립트에서 `Array` 자료형으로 간단하게 스택 구현 가능

```javascript
// 스택으로 사용할 리스트를 선언
let stack = [];

// push를 이용해 스택에 원소를 채워 넣기
stack.push(1);
stack.push(2);
stack.push(3);

// 스택의 맨 꼭대기에 있는 원소를 조회할 땐 length - 1 인덱스 사용
console.log(stack[stack.length - 1]); // 3
// 또는 slice(-1) 사용
console.log(stack.slice(-1)); // 3

// 스택에서 값을 제거할 때에는 pop()을 사용
stack.pop(); // 스택의 끝에 있는 3를 단순히 제거
let value = stack.pop(); // 스택의 끝의 2를 바로 할당 가능
console.log(value); // 2
```

<br><br>

## 2. Queue (큐)

- First In First In
- 스택과 반대로 먼저 들어간 것이 먼저 나옴
- ex) 사람들이 쭉 늘어서 있는 대기열

```javascript
// 큐로 사용할 리스트 선언
let queue = [];

// push 이용해 큐에 원소를 채워넣기
queue.push(1);
queue.push(2);
queue.push(3);

// 큐의 맨 앞에 있는 원소를 조회할 땐 0 인덱스를 사용
console.log(queue[0]); // 1

// 큐에서 값을 제거할 때에는 shift() 사용
queue.shift(); // 큐의 앞에 있는 1을 단순히 제거
let value = queue.shift(); // 큐의 앞의 2를 바로 할당 가능
console.log(value); // 2
```

<br><br>

## 3. BFS (너비 우선 탐색)

- Breadth First Search
- 현재 위치를 기준으로, 방문이 가능한 모든 위치 탐색
- 그 다음 단계에서는 **이전 단계에서 구한 위치**들을 기준으로 다시 방문이 가능한 모든 위치 탐색
- **완전 탐색**과 다른 점은 **갈 수 있는 위치**만 탐색한다는 점

  - 결론적으로 못 가거나, 갈 수 없는 위치는 굳이 탐색할 필요가 없어지니 완전 탐색보다는 효율적

<br>

### 3.1. BFS 이용한 예시 코드

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

let input = [];
let N;
let matrix = [];

rl.on("line", (line) => {
  input.push(line.trim());
  if (input.lenght === Number(input[0]) + 1) {
    rl.close();
  }
});

rl.on("close", () => {
  N = Number(input[0]);
  for (let i = 1; i <= N; i++) {
    matrix.push(input[i].split(" ").map(Number));
  }

  let visited = Array.from({ length: N }, () => Array(N).fill(false));

  let count = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (matrix[i][j] === 1 && !visited[i][j]) {
        count++;
        // BFS
        q = [];
        q.push([i, j]);
        visited[i][j] = true;

        while (q.length > 0) {
          let [currentR, currentC] = q.shift();

          for (let k = 0; k < 4; k++) {
            let nextR = currentR + dx[k];
            let nextC = currentC + dy[k];

            if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < N) {
              if (matrix[nextR][nextC] === 1 && !visited[nextR][nextC]) {
                q.push([nextR, nextC]);
                visited[nextR][nextC] = true;
              }
            }
          }
        }
      }
    }
  }
  console.log(count);
});
```

<br><br>

## 4. DFS (깊이 우선 탐색)

- Depth First Search
- 현재 위치를 기준으로, 방문을 시작한 위치와 방향을 탐색이 불가능할 때까지 탐색한 이후에 돌아옴
- **완전 탐색**과 다른 점은 **갈 수 있는 위치**만 탐색한다는 점

  - 결론적으로 못 가거나, 갈 수 없는 위치는 굳이 탐색할 필요가 없어지니 완전 탐색보다는 효율적

### 4.1. JavaScript에서 BFS와 DFS

- 자바스크립트에서 `BFS`와 `DFS`의 차이는 탐색 후보에서 뒤에서 후보를 가져오는지, 앞에서 후보를 가져오는 차이

  - `BFS` -> `queue.shift()`
  - `DFS` -> `queue.pop()`

<br>

### 4.2. DFS 이용한 예시 코드

```javascript
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];
let input = [];
let matrix = [];
const score = {};

rl.on("line", (line) => {
  input.push(line.trim());
});

rl.on("close", () => {
  const [N, K] = input[0].split(" ").map(Number);
  for (let i = 1; i <= N; i++) {
    matrix.push(input[i].split(" ").map(Number));
  }

  const visited = Array.from({ length: N }, () => Array(N).fill(false));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        // q: 탐색 후보 관리
        // 첫번쨰 탐색 후보 추가
        let q = [];
        q.push([i, j]);
        // size : 현재 탐색하는 단지의 크기
        // target : 현재 탐색하는 건물의 유형
        let size = 1;
        const target = matrix[i][j];

        //탐색 후보가 없을 때 까지 탐색
        while (q.length) {
          const [currentR, currentC] = q.pop();
          visited[currentR][currentC] = true;
          for (let k = 0; k < 4; k++) {
            const nextR = currentR + dx[k];
            const nextC = currentC + dy[k];
            // 마을 안의 좌표인지 확인
            if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < N) {
              // 방문한 적이 있으면, 현재 탐색 중인 건물의 유형과 동일한지 확인
              if (!visited[nextR][nextC] && matrix[nextR][nextC] === target) {
                // 모든 조건을 만족하면 방문을 true로 변경하고
                // 탐색 후보에 추가한 후 단지의 크기를 1 추가
                visited[nextR][nextC] = true;
                q.push([nextR, nextC]);
                size++;
              }
            }
          }
        }
        // 단지의 크기 K이상이라면, 건물의 유형에 단지의 개수를 추가
        if (size >= K) {
          score[target] = (score[target] || 0) + 1;
        }
      }
    }
  }
  const sortedScores = Object.entries(score).sort(
    (a, b) => b[1] - a[1] || b[0] - a[0]
  );
  console.log(sortedScores.length ? sortedScores[0][0] : -1);
});
```
