import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()

        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)




n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]

cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    bfs(i)
    cnt += 1

print(cnt)
