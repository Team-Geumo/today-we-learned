# 백트래킹
## Promising
- 트리 구조를 기반으로 DFS로 깊이 탐색을 진행하면서 각 루트에 대해 조건에 부합하는지 체크
## Pruning
- 해당 트리에서 조건에 맞지않는 노드는 더 이상 DFS로 깊이 탐색을 진행하지 않고 가지치기를 함

## 백트래킹 구현
- 해를 구하는 도중 해가 아니어서 막히면 막히기 전으로 다시 돌아가서 해를 찾는 기법
- 예를 들어, 갈랫길에서 한쪽으로 갔다가 이 길이 아닌 것 같으면 왔던 길로 되돌아와 다른 선택지로 감
- 가상의 트리에서 해를 구하기 위해 부모 노드에서 자식 노드까지 뻗어나감. 만약 해당 노드가 조건에 맞지 않는다면 다시 부모노드로 돌아감
- 해가 아닌 선택지는 없애면서 탐색하기 때문에 시간복잡도를 줄일 수 있음

## N과 M
https://www.acmicpc.net/problem/15649
### 풀이
1. 중복 방지를 위해 방문 여부를 알려주는 visited라는 리스트를 만들어서 숫자의 범위인 n만큼 False라는 값을 채워줌
2. 결과를 담아서 출력해 줄 answer라는 빈 배열을 선언
3. depth, n, m을 입력받는데 이때, depth는 answer 배열에 들어온 숫자의 개수가 됨. depth가 m과 같아진다면 문제에서 요구하는 수열을 찾은 것이므로 출력하고 함수가 종료됨
4. depth와 m이 같지 않다면 아직 탐색해야 할 숫자가 남았다는 의미이므로 visited에 False값이 저장되어 아직 방문하지 않은 숫자를 방문
5. 방문한 숫자는 방문했다는 의미로 visited에 True를 저장해주고 depth를 1증가시킨 상태에서 재귀함수를 실행
6. 함수를 다시 실행하면 금방 방문한 숫자를 answer배열에 저장하고 해당 함수에서 나오게 되면 방문했다는 표시를 다시 False로 바꿔주고 해당 숫자를 pop해주어야 원래 자리로 돌아가서 다음 탐색을 실행
### 코드
```python
def n_and_m(depth, n, m):

  if depth == m:
    print(' '.join(map(str, answer)))

  for i in range(1, n+1):
    
    if not visited[i]:
      visited[i] = True
      answer.append(i)
      n_and_m(depth+1, n, m)
      visited[i] = False
      answer.pop()

n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

n_and_m(0, n, m)
```