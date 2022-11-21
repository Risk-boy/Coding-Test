import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def dfs(s):
    visited_dfs[s] = True
    print(s, end=" ")
    for node in graph[s]:
        if not visited_dfs[node]:
            dfs(node)

def bfs(s):
    q = deque()
    q.append(s)
    visited_bfs[s] = True

    while q:
        a = q.popleft()
        print(a, end=" ")
        for node in graph[a]:
            if not visited_bfs[node]:
                visited_bfs[node] = True
                q.append(node)



# 정점의 개수, 간선의 개수, 탐색 시작 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()
    
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(v)
print()
bfs(v)

