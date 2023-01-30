import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

'''
각 섬마다 번호 부여하기
각 섬에서 출발해서 인접한 섬까지 최단거리 갱신
'''

def land_check():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not land[i][j]:
                cnt += 1
                land[i][j] = cnt
                q = deque()
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]

                        if 0 <= nr < n and 0 <= nc < n:
                            if arr[nr][nc] == 1 and land[nr][nc] == 0:
                                land[nr][nc] = cnt
                                q.append((nr, nc))
    return cnt

def solve(land_num):
    global max_length
    q = deque()
    for i in range(n):
        for j in range(n):
            if land[i][j] == land_num:
                q.append((i, j))

    visited = [[0 for _ in range(n)] for _ in range(n)]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if not land[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                if land[nr][nc] and land[nr][nc] != land_num and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    if max_length > visited[r][c]:
                        max_length = visited[r][c]



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
land = [[0 for _ in range(n)] for _ in range(n)]  # 섬 번호 부여할 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 섬 번호 부여하기
land_cnt = land_check()

# 섬마다 돌면서 최단거리 갱신
max_length = 200
for x in range(1, land_cnt + 1):
    solve(x)

print(max_length)

