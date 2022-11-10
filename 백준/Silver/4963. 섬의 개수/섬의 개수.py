import sys
# sys.stdin = open("input.txt")
from collections import deque
from copy import deepcopy

def bfs(x, y):
    global cnt

    q = deque()
    q.append((x, y))
    if visited[x][y]:
        return
    visited[x][y] = True
    cnt += 1

    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if arr[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))


# 12시 방향부터 8방향 탐색
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
    print(cnt)
