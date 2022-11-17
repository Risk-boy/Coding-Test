import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(a, b):
    q = deque()
    q.append((a, b, 0))
    maxCnt = 0
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True

    while q:
        r, c, cnt = q.popleft()
        if cnt > maxCnt:
            maxCnt = cnt

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == "L" and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))

    return maxCnt

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dist = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            dist.append(bfs(i, j))


print(max(dist))

