import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

def solve(x):
    q = deque()
    q.append(x)
    visited[x] = True
    cost = costs[i]

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                if cost > costs[next]:
                    cost = costs[next]
    return cost

n, m, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

total = 0
for i in range(1, n + 1):
    if not visited[i]:
        total += solve(i)

if total <= k:
    print(total)
else:
    print("Oh no")