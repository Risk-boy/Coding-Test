import sys
# sys.stdin = open("input.txt")
from collections import deque

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

visited = [[False] * n for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            q.append((arr[i][j], i, j, 0))
            visited[i][j] = True

q = deque(sorted(q))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    power, r, c, cnt = q.popleft()
    if cnt == s:
        continue
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc]:
                if not arr[nr][nc]:
                    arr[nr][nc] = power
                    q.append((power, nr, nc, cnt + 1))
                    visited[nr][nc] = True

print(arr[x - 1][y - 1])



