import sys
# sys.stdin = open("input.txt")
from collections import deque

'''
bfs를 돌면서 같은 색을 방문한 개수가 해당 공간을 포함하는
최소한의 직사각형 면적이랑 같은지 확인
'''

def bfs(r, c, x):
    q = deque()
    rowMin = r
    rowMax = r
    colMin = c
    colMax = c
    cnt = 1
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == x and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
                    if rowMin > nr:
                        rowMin = nr
                    if rowMax < nr:
                        rowMax = nr
                    if colMin > nc:
                        colMin = nc
                    if colMax < nc:
                        colMax = nc

    if (rowMax - rowMin + 1) * (colMax - colMin + 1) == cnt:
        return True
    else:
        return False

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input()))

visited = [[False] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
check = True
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            if not bfs(r, c, arr[r][c]):
                check = False
                break
    if not check:
        break


if check:
    print("dd")
else:
    print("BaboBabo")
