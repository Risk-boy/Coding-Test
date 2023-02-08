import sys
# sys.stdin = open("input.txt")
from collections import deque


def solve(s, e):
    q = deque()
    q.append((s, e))
    visited[s][e] = True
    score[s][e] = graph[s][e]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    score[nr][nc] = score[r][c] + graph[nr][nc]
                    q.append((nr, nc))
                    visited[nr][nc] = True
                else:
                    if score[nr][nc] > score[r][c] + graph[nr][nc]:
                        score[nr][nc] = score[r][c] + graph[nr][nc]
                        q.append((nr, nc))



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    score = [[9 * n * n] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    solve(0, 0)
    print(f"Problem {cnt}: {score[n-1][n-1]}")
    
    cnt += 1

