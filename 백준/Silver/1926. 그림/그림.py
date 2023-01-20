import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

def solve(x, y):
    global area
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area += 1
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    area += 1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_area = 0
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = 0
            solve(i, j)
            max_area = max(max_area, area)

print(cnt)
print(max_area)