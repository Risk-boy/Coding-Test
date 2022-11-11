import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(a, b, c):
    global cnt
    if visited[a][b]:
        return
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    cnt += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                # 방문 안했고 안전구역이라면
                if not visited[nr][nc] and arr[nr][nc] > k:
                    visited[nr][nc] = True
                    q.append((nr, nc))

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 제일 높은 곳 미만으로 비를 하나하나 뿌려보기
maxH = 0
for i in range(n):
    for j in range(n):
        if maxH < arr[i][j]:
            maxH = arr[i][j]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

maxCnt = 1
for k in range(1, maxH):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k:
                bfs(i, j, k)
    if maxCnt < cnt:
        maxCnt = cnt

print(maxCnt)
