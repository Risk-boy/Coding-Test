import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, check = q.popleft()
        if r == n-1 and c == m-1:
            return visited[n-1][m-1][check]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                # 벽이 아닌 경우
                if arr[nr][nc] == 0 and not visited[nr][nc][check]:
                    visited[nr][nc][check] = visited[r][c][check] + 1
                    q.append((nr, nc, check))
                # 벽인 경우
                elif arr[nr][nc] == 1 and not visited[nr][nc][check]:
                    # 벽을 아직 안부쉈다면
                    if check == 0:
                        visited[nr][nc][check + 1] = visited[r][c][check] + 1
                        q.append((nr, nc, check + 1))
                    elif check == 1:
                        continue
    return -1


n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

# 0번 idx: 벽을 아직 안부순 경우
# 1번 idx: 벽을 부순 경우
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(bfs())



