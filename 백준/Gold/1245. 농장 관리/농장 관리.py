import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(x, y):
    global check
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        r, c = q.popleft()

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == arr[r][c]:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                elif arr[nr][nc] > arr[r][c]:
                    check = False


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(n):
    for j in range(m):
        check = True
        if not visited[i][j]:
            bfs(i, j)
            if check:
                answer += 1

print(answer)