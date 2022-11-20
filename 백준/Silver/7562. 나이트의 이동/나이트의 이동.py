import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(a, b):
    global er, ec
    q = deque()
    q.append((a, b, 0))
    visited[a][b] = True

    while q:
        r, c, cnt = q.popleft()
        if r == er and c == ec:
            return cnt
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))


# 테스트 케이스
T = int(input())

# 1시 방향부터
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    n = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visited = [[False] * n for _ in range(n)]
    print(bfs(sr, sc))
