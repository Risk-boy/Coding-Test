import sys
# sys.stdin = open("input.txt")

def dfs(r, c):
    global cnt
    visited[r][c] = 1
    if arr[r][c] == "U":
        nr, nc = r - 1, c
    elif arr[r][c] == "D":
        nr, nc = r + 1, c
    elif arr[r][c] == "L":
        nr, nc = r, c - 1
    elif arr[r][c] == "R":
        nr, nc = r, c + 1

    if not visited[nr][nc]:
        dfs(nr, nc)

    if visited[nr][nc] == 1:
        cnt += 1
    visited[r][c] = 2

n, m = map(int, input().split())

arr = list(list(input()) for _ in range(n))

cnt = 0
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)


print(cnt)




