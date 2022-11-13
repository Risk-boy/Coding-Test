import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    cnt += 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))

# 세로, 가로, 음식물 쓰레기 개수
n, m, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ls = []
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    ls.append((r-1, c-1))

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxCnt = 0
for trash in ls:
    cnt = 0
    if not visited[trash[0]][trash[1]]:
        bfs(trash[0], trash[1])
        if maxCnt < cnt:
            maxCnt = cnt

print(maxCnt)

