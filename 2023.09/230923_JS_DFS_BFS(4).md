# DFS/BFS (4)

## 2. 탐색 알고리즘

### 2.2. BFS(Breadth First Search)

- **너비 우선 탐색**
- **가까운 노드부터 탐색하는 알고리즘**
- 선입선출 방식인 큐 자료구조 이용하는 것이 정석

  - 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색 진행

- BFS의 동작 방식

  - 탐색 시작 노드를 큐에 삽입하고 방문 처리
  - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 위의 과정을 더 이상 수행할 수 없을 때까지 반복

- 일반적인 경우 실제 수행 시간은 DFS보다 BFS가 좋은 편

```javascript
// BFS 메서드 정의
function bfs(graph, start, visited) {
  let queue = [start];
  // 현재 노드를 방문 처리
  visited[start] = true;
  // 큐가 빌 때까지 반복
  while (queue) {
    // 큐에서 하나의 원소를 뽑아 출력
    let v = queue.shift();
    console.log(v);
    // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for (let i of graph[v]) {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = true;
      }
    }
  }
}

// 각 노드가 연결된 정보를 객체 자료형으로 표현
const graph = {
  1: [2, 3, 8],
  2: [1, 7],
  3: [1, 4, 5],
  4: [3, 5],
  5: [3, 4],
  6: [7],
  7: [2, 6, 8],
  8: [1, 7],
};

// 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
let visited = new Array(9).fill(false);

// 정의된 BFS 함수 호출
bfs(graph, 1, visited);
```

```bash
1
2
3
8
7
4
5
6
```

<br>

### 2.3. DFS vs. BFS

|           | DFS            | BFS              |
| --------- | -------------- | ---------------- |
| 동작 원리 | 스택           | 큐               |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |

<br><br>

## 3. 음료수 얼려 먹기

### 3.1. 내 풀이

- BFS 이용

```javascript
let input = require("fs").readFileSync("example.txt").toString().split("\n");

const [N, M] = input[0].split(" ").map(Number); // 세로 크기, 가로 크기
let board = input.slice(1).map((e) => e.slice(0, M).split("").map(Number)); // 얼음 틀 형태
let count = 0; // 아이스크림 개수

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    // 구멍이 뚫려 있다면
    if (board[i][j] === 0) {
      board[i][j] = 1; // 방문표시
      count++;
      let queue = [[i, j]];

      // BFS
      while (queue.length > 0) {
        let [currentX, currentY] = queue.shift();

        for (let k = 0; k < 4; k++) {
          let nx = currentX + dx[k];
          let ny = currentY + dy[k];

          // 인접 좌표가 얼음 틀 안에 있고 구명이 뚫려 있는 부분이라면
          if (nx > -1 && nx < N && ny > -1 && ny < M && !board[nx][ny]) {
            queue.push([nx, ny]);
            board[nx][ny] = 1;
          }
        }
      }
    }
  }
}

console.log(count);
```

<br>

### 3.2. 해설

- DFS로 해결
- 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 가능
- 풀이 과정
  1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있따면 해당 지점 방문
  2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점 방문 가능
  3. 위의 과정을 모든 노드에 반복하며 방문하지 않은 지점 수 세기

```javascript
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];

rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [N, M] = lines[0].split(" ").map(Number);

  // 2차원 리스트의 맵 정보 입력받기
  let graph = [];
  for (let i = 1; i <= N; i++) {
    graph.push(Array.from(lines[i]).map(Number));
  }

  // DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
  function dfs(x, y) {
    // 주어진 범위를 벗어나는 경우에는 즉시 종료
    if (x < 0 || x >= N || y < 0 || y >= M) {
      return false;
    }

    // 현재 노드를 아직 방문하지 않았다면
    if (graph[x][y] === 0) {
      // 해당 노드 방문 처리
      graph[x][y] = 1;
      // 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
      dfs(x - 1, y);
      dfs(x, y - 1);
      dfs(x + 1, y);
      dfs(x, y + 1);
      return true;
    }
    return false;
  }

  // 모든 노드에 대하여 음료수 채우기
  let result = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      // 현재 위치에서 DFS 수행
      if (dfs(i, j) === true) {
        result++;
      }
    }
  }

  console.log(result);
});
```

<br><br>

## 4. 미로 탈출

### 4.1. 해설

- BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문에 BFS를 이용했을 떄 효과적으로 해결 가능
- (1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 됨
- 특정 노드를 방문하면 그 이전의 노드의 거리에 1을 더한 값을 리스트에 넣음

```javascript
let input = require("fs").readFileSync("example.txt").toString().split("\n");

const [N, M] = input[0].split(" ").map(Number); // N x M 직사각형
const maze = input.slice(1).map((e) => e.slice(0, M).split("").map(Number)); // 미로의 정보

// 이동할 네 방향 정의
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

// BFS 구현
function bfs(x, y) {
  let queue = [[x, y]];

  // 큐가 빌 때까지 반복
  while (queue.length > 0) {
    let [currentX, currnetY] = queue.shift();

    // 현재 위치에서 네 방향으로의 위치 확인
    for (let k = 0; k < 4; k++) {
      let nx = currentX + dx[k];
      let ny = currnetY + dy[k];

      // 미로 찾기 공간을 벗어난 경우
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

      // 벽인 경우
      if (maze[nx][ny] === 0) continue;

      // 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if (maze[nx][ny] === 1) {
        maze[nx][ny] = maze[currentX][currnetY] + 1;
        queue.push([nx, ny]);
      }
    }
  }
  // 가장 오른쪽 아래까지의 최단 거리 반환
  return maze[N - 1][M - 1];
}

console.log(bfs(0, 0));
```
