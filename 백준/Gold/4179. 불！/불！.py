import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(r, c):
    global answer
    qq = deque()
    qq.append((r, c, 1))
    visited[r][c] = True

    while qq:
        nq = len(q)
        nqq = len(qq)
        for _ in range(nq):
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if arr[nr][nc] != "#" and arr[nr][nc] != "F":
                        arr[nr][nc] = "F"
                        q.append((nr, nc))

        for _ in range(nqq):
            r, c, cnt = qq.popleft()
            if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                answer = cnt
                return
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if arr[nr][nc] == "." and not visited[nr][nc]:
                        qq.append((nr, nc, cnt + 1))
                        visited[nr][nc] = True



n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
a = b = 0
answer = "IMPOSSIBLE"
for i in range(n):
    for j in range(m):
        if arr[i][j] == "F":
            q.append((i, j))
        elif arr[i][j] == "#":
            visited[i][j] = True
        elif arr[i][j] == "J":
            a = i
            b = j
bfs(a, b)
print(answer)