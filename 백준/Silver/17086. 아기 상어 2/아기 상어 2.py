import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve(s, e):
    global answer
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((s, e, 0))
    visited[s][e] = True

    while q:
        r, c, cnt = q.popleft()
        if graph[r][c] == 1:
            answer = max(answer, cnt)
            return

        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
answer = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            solve(i, j)

print(answer)
