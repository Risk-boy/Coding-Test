import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

'''
가장 긴 경로가 우선
'''

def bfs(x, y):
    global answer, maxLen
    maxDist = 1
    end = arr[x][y] # 끝점
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = True

    while q:
        r, c, dist = q.popleft()
        if dist > maxDist:
            maxDist = dist
            end = arr[r][c]
        elif dist == maxDist:
            end = max(end, arr[r][c])

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and arr[nr][nc]:
                    q.append((nr, nc, dist + 1))
                    visited[nr][nc] = True
    if maxDist > maxLen:
        maxLen = maxDist
        answer = arr[x][y] + end
    elif maxDist == maxLen:
        answer = max(answer, arr[x][y] + end)

# 세로 / 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0 # 현재 최대 합
maxLen = 0 # 현재 최대 길이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            bfs(i, j)

print(answer)
