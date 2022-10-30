# import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)

    visited = [False] * (v+1)
    visited[start] = True
    while queue:
        virus = queue.popleft()

        for com in graph[virus]:
            if not visited[com]:
                visited[com] = True
                cnt += 1
                queue.append(com)

    return cnt

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
# print(graph)
print(bfs(1))

