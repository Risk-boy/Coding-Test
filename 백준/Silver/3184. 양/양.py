import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve(x, y):
    global answer_sheep, answer_wolf
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    sheep = wolf = 0
    if arr[x][y] == "o":
        sheep += 1
    elif arr[x][y] == "v":
        wolf += 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc]:
                    if arr[nr][nc] == "#":
                        continue
                    if arr[nr][nc] == "v":
                        wolf += 1
                    elif arr[nr][nc] == "o":
                        sheep += 1
                    q.append((nr, nc))
                    visited[nr][nc] = True
    if wolf >= sheep:
        answer_wolf += wolf
    else:
        answer_sheep += sheep

    return

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer_sheep = 0
answer_wolf = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != "#" and not visited[i][j]:
            solve(i, j)

print(answer_sheep, answer_wolf)