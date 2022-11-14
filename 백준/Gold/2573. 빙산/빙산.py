import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif arr[nr][nc] == 0:
                    arr[r][c] -= 1
                    if arr[r][c] < 0:
                        arr[r][c] = 0


n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

year = 0

while True:

    # 분리된 섬 개수 찾기
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    # 분리된 섬이 2개 이상이라면
    if cnt >= 2:
        print(year)
        break
    # 나뉘어질 섬이 없다면
    if cnt == 0:
        print(0)
        break

    year += 1
