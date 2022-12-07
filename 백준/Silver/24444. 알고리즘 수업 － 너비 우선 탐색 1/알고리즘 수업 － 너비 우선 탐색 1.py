import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    visited[s][0] = True
    visited[s][1] = 1
    cnt = 1
    while q:
        now = q.popleft()
        for v in graph[now]:
            if not visited[v][0]:
                cnt += 1
                q.append(v)
                visited[v][0] = True
                visited[v][1] = cnt


# 정점 수 / 간선 수 / 시작 정점
n, m, r = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [[False, 0] for _ in range(n + 1)]
bfs(r)

for i in range(1, n + 1):
    print(visited[i][1])

