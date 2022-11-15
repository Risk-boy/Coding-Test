import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(a, b):
    global cnt, flag
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:

        # 물을 일단 한칸씩 흘려보내기
        lenW = len(waterQ)
        for _ in range(lenW):
            x, y = waterQ.popleft()
            waterV[x][y] = True
            for i in range(4):
                nx = x + dr[i]
                ny = y + dc[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not waterV[nx][ny]:
                        if arr[nx][ny] != "X" and arr[nx][ny] != "D":
                            waterV[nx][ny] = True
                            waterQ.append((nx, ny))

        # 비버도 한칸씩 이동
        lenB = len(q)
        cnt += 1
        for _ in range(lenB):
            r, c = q.popleft()
            if arr[r][c] == "D":
                flag = True
                return
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    # 물이 아직 침범 안한곳
                    if not visited[nr][nc] and not waterV[nr][nc]:
                        if arr[nr][nc] != "X":
                            visited[nr][nc] = True
                            q.append((nr, nc))


n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

waterQ = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            startR, startC = i, j
        elif arr[i][j] == "*":
            waterQ.append((i, j))

waterV = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

flag = False
cnt = 0
bfs(startR, startC)

if not flag:
    print("KAKTUS")
else:
    print(cnt-1)