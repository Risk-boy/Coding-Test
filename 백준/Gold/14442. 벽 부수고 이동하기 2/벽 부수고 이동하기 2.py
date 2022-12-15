import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs():
    global k
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, check = q.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][check]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                # 벽을 부술 수 없는 경우
                if arr[nr][nc] == 0 and check == k:
                    if not visited[nr][nc][check]:
                        visited[nr][nc][check] = visited[r][c][check] + 1
                        q.append((nr, nc, check))
                # 벽을 부술 수 있는 경우
                elif check < k:
                    # 벽이 아닌 경우
                    if arr[nr][nc] == 0 and not visited[nr][nc][check]:
                        visited[nr][nc][check] = visited[r][c][check] + 1
                        q.append((nr, nc, check))
                    # 벽인 경우
                    elif arr[nr][nc] == 1 and not visited[nr][nc][check+1]:
                        visited[nr][nc][check+1] = visited[r][c][check] + 1
                        q.append((nr, nc, check+1))
    return -1


n, m, k = map(int, input().split())

arr = list(list(map(int, input())) for _ in range(n))
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
print(bfs())
