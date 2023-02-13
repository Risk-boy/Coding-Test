import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve(s, e):
    heap = []
    heapq.heappush(heap, (0, s, e))
    visited[s][e] = True

    while heap:
        cnt, r, c = heapq.heappop(heap)
        if r == n - 1 and c == m - 1:
            return cnt

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc]:
                    if graph[nr][nc] == 1:  # 벽이면
                        heapq.heappush(heap, (cnt + 1, nr, nc))
                    else:
                        heapq.heappush(heap, (cnt, nr, nc))
                    visited[nr][nc] = True



m, n = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[False] * m for _ in range(n)]
walls = [[10000] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(solve(0, 0))
