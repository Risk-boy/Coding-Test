import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def bfs(x):
    global answer
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                answer += 1
                if cur == 1:
                    q.append(next)
                    visited[next] = True
                else:
                    visited[next] = True
    return answer

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
answer = 0

print(bfs(1))
