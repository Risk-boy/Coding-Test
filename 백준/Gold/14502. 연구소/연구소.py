import sys
# sys.stdin = open("input.txt")
from collections import deque
from itertools import combinations
import copy

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if temp[nr][nc] == 0:
                    temp[nr][nc] = 2
                    q.append((nr, nc))


# 세로 / 가로
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 바이러스 위치 찾기
virus = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            virus.append((r, c))

# 벽을 세울 수 있는 공간 찾기
ls = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            ls.append((r, c))

# 세개의 벽을 세울 공간의 조합 만들기
comb_ls = list(combinations(ls, 3))


# 감염되지 않은 구역의 최대값
maxP = 0

# 상 하 좌 우
dr = [-1, 1, 0 , 0]
dc = [0, 0, -1, 1]

# 각각의 조합에 대해서 bfs 수행하기
for walls in comb_ls:
    temp = copy.deepcopy(arr)
    cnt = 0
    for wall in walls:
        temp[wall[0]][wall[1]] = 1
    # 바이러스가 있는 공간에 대해 bfs 수행
    for v in virus:
        bfs(v[0], v[1])
    # 감염되지 않은 구역 찾기
    for r in range(n):
        for c in range(m):
            if temp[r][c] == 0:
                cnt += 1
    if maxP < cnt:
        maxP = cnt

print(maxP)
