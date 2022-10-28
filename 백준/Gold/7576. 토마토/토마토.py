#import sys
#sys.stdin = open("input.txt")

from collections import deque

def bfs():
    global queue

    while queue:
        r, c = queue.popleft()
        # 4방향 확인
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 토마토 상자 범위 밖인 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 토마토가 아닌 경우
            if arr[nr][nc] == -1:
                continue
            # 안익은 토마토인 경우
            if arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                queue.append((nr, nc))


# m: 가로 칸의 수, n: 세로 칸의 수
m, n = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 익은 토마토 찾아서 queue에 넣어주기
# 동시에 퍼지기 때문에 queue에 먼저 넣어주어야 함
queue = deque()
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없는 칸
flag1 = True    # 처음에 익은 토마토만 있을경우 대비
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            flag1 = False
        elif arr[r][c] == 1:
            queue.append((r, c))
bfs()
# 다 익히는데 필요한 일수 구하기
cnt = -1
flag2 = False # 안 익은 토마토가 있을 경우 True로
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag2 = True
        if arr[i][j] > cnt:
            cnt = arr[i][j]

if flag1:
    print(0)
elif flag2:
    print(-1)
else:
    print(cnt-1)


