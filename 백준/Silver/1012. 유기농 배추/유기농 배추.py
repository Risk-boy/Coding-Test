# import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(a, b):
    # 방문 했던 곳이라면 방문할 필요 없음
    if visited[a][b] == 1:
        return 0
    # 큐 초기화
    queue = deque()
    queue.append((a, b))
    # 방문 표시
    visited[a][b] = 1
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내에서
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 배추가 있고 방문 안한곳이라면
            if arr[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 큐에 추가
                queue.append((nr, nc))
    # 지렁이가 갈수있는 곳을 전부 탐색했으면
    return 1


T = int(input())

for tc in range(T):
    # 가로, 세로, 배추위치
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    # 배추 표시하기
    for i in range(k):
        c, r = map(int, input().split())
        arr[r][c] = 1
    # 4방향 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 필요한 배추흰지렁이 마리 수
    cnt = 0
    # 배추 있는 곳 기준으로 bfs
    for c in range(m):
        for r in range(n):
            if arr[r][c] == 1:
                cnt += bfs(r, c)
    print(cnt)
