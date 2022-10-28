from collections import deque

# import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    # queue 초기화
    queue = deque()
    queue.append((r, c))
    # queue가 빌 때 까지
    while queue:
        r, c = queue.popleft()
        # 4방향 돌면서
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 미로 범위를 벗어나는 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 벽을 만나는 경우
            if maze[nr][nc] == 0:
                continue
            # 처음 와본 곳이라면
            if maze[nr][nc] == 1:
                # 추가해주고
                queue.append((nr, nc))
                # 거리 1 더해주기
                maze[nr][nc] = maze[r][c] + 1

    return maze[n-1][m-1]

print(bfs(0,0))