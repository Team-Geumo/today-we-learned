### 다익스트라 (Dijkstra) 알고리즘

- 다익스트라 알고리즘
  
  - **음의 가중치가 없는** 그래프의 한 정점에서 모든 정점까지의 최단거리를 각각 구하는 알고리즘
  
  - 최단 경로 문제
  
  - 우선순위 큐를 사용하면 시간복잡도를 줄일 수 있음

- 코드
  
  - 우선순위 큐 사용 X
    
    ```python
    def dijkstra1(s, V): # 시작정점 s, 마지막 정점 V
        U = [0] * (V+1)
        U[s] = 1
        for v in range(V+1):
            D[v] = adj[s][v]  # 시작 점에서 갈 수 있는 값 
    
        #while len(U) != V:
        for _ in range(V):  # V = 정점개수-1과 같으므로..남은 정점개수와 같음
            minV = INF
            w = 0
            for i in range(V+1):
                if U[i] == 0 and minV > D[i]:
                    minV = D[i]
                    w = i
            U[w] = 1  # 선택된 집합에 포함
    
            for v in range(V+1):   # 정점 v가
                if 0 < adj[w][v] < INF:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                    D[v] = min(D[v], D[w]+adj[w][v])  # 시작정점에서 v로 가는 기존 비용을 비교 후 선택
    
    INF = 987654321
    V, E = map(int, input().split())
    adj = [[INF]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        adj[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w  # 방향성 그래프
    
    D = [0]*(V+1)
    dijkstra1(0, V)
    print(D)  # 시작 정점 0에서 각 정점으로 가는 최소 비용
    ```
    
    ```python
    def dijkstra2():
        while Q:
            print(Q, D)
            now, dist = Q.pop(0)   # 정점 정보와 거리 
    
            if D[now] < dist:      # 주어진 거리보다 저장된 거리가 더 작으면 skip
                continue
    
            # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
            for v in range(len(adj_list[now])):
                n_v, n_dist = adj_list[now][v]   # 연결된 정점과 그 거리
    
                # 현재까지의 거리와 연결된 정점의 거리를 더한 값이 
                # 저장된 값보다 작다면 갱신
                if dist + n_dist < D[n_v]:
                    D[n_v] = dist + n_dist
                    Q.append((n_v, D[n_v]))   # 다음 정점과 갱신된 거리를 Queue에 등록
    
    INF = 987654321
    V, E = map(int, input().split())
    # 인접 리스트
    adj_list = [[] for _ in range(V+1)]
    
    for _ in range(E):
        s, v, d = map(int, input().split())
        adj_list[s].append((v, d))
    
    D = [INF] * (V+1)
    D[0] = 0
    for v, d in adj_list[0]:   # 시작 정점에서 인접한 정점 거리 저장
        D[v] = d
    
    Q = [*adj_list[0]]  # Queue 에 시작점으로 부터 이어진 값을 넣는다.
    
    dijkstra2()
    print(D)
    ```
  
  - 우선순위 큐 사용
    
    ```python
    from heapq import heappush, heappop
    
    def dijkstra(start):
        h = []                                  # 최소힙
        d[start] = 0
        heappush(h, (0, start))                 # 시작점 추가
        while h:
            dist_u, u = heappop(h)              # 최소 비용 간선 선택
            if d[u] < dist_u:                   # 테이블에 저장된 최소값 보다 크면 continue
                continue
            for v, w in graph[u]:               # 다음 노드로 가는 비용 계산해서
                dist_v = dist_u + w
                if dist_v < d[v]:
                    d[v] = dist_v               # 최소값 테이블에 업데이트 후
                    heappush(h, (dist_v, v))    # 힙에 추가
    
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))                 # 인접 리스트
    
    INF = 1e9
    d = [INF]*(N+1)                             # 최대값으로 초기화
    
    dijkstra(0)
    print(d)
    ```