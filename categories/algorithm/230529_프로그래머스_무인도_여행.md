# 프로그래머스 무인도 여행
```
def solution(maps):
    answer = []
    visited=[[0] * len(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if visited[i][j] == 0 and maps[i][j] != "X":
                answer.append(bfs(visited,i,j,maps))
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer

def bfs(visited,i,j,maps):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    q = [[i,j]]
    visited[i][j] = 1
    cnt = 0
    while q:
        r,c = q.pop(0)
        cnt += int(maps[r][c])
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= len(maps) or nc < 0 or nc >= len(maps[0]) or visited[nr][nc] == 1 or maps[nr][nc] == "X":
                continue
            q.append([nr,nc])
            visited[nr][nc] = 1
    return cnt
```