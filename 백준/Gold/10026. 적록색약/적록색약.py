import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs_R(x, y):
    global cnt1
    if visited1[x][y]:
        return
    q = deque()
    q.append((x, y))

    visited1[x][y] = True
    cnt1 += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited1[nr][nc] and arr[nr][nc] == "R":
                    visited1[nr][nc] = True
                    q.append((nr, nc))
def bfs_G(x, y):
    global cnt1
    q = deque()
    q.append((x, y))
    if visited1[x][y]:
        return
    visited1[x][y] = True
    cnt1 += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited1[nr][nc] and arr[nr][nc] == "G":
                    visited1[nr][nc] = True
                    q.append((nr, nc))

def bfs_B(x, y):
    global cnt1
    q = deque()
    q.append((x, y))
    if visited1[x][y]:
        return
    visited1[x][y] = True
    cnt1 += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited1[nr][nc] and arr[nr][nc] == "B":
                    visited1[nr][nc] = True
                    q.append((nr, nc))

def bfs_RG(x, y):
    global cnt2
    if visited2[x][y]:
        return
    q = deque()
    q.append((x, y))
    visited2[x][y] = True
    cnt2 += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited2[nr][nc] and (arr[nr][nc] == "R" or arr[nr][nc] == "G"):
                    visited2[nr][nc] = True
                    q.append((nr, nc))

def bfs_BB(x, y):
    global cnt2
    if visited2[x][y]:
        return
    q = deque()
    q.append((x, y))
    visited2[x][y] = True
    cnt2 += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited2[nr][nc] and arr[nr][nc] == "B":
                    visited2[nr][nc] = True
                    q.append((nr, nc))
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

# print(arr)

cnt1 = 0 # 적록색약 X
cnt2 = 0 # 적록색약 O

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

# 적록색약 아닌 사람 bfs_R, bfs_G, bfs_B
visited1 = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R":
            bfs_R(i, j)
        if arr[i][j] == "G":
            bfs_G(i, j)
        if arr[i][j] == "B":
            bfs_B(i, j)

# 적록색약인 사람은 R과 G를 동일시한다
visited2 = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R" or arr[i][j] == "G":
            bfs_RG(i, j)
        if arr[i][j] == "B":
            bfs_BB(i, j)

print(cnt1, cnt2)