import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

def solve():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = 1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            answer[nxt] = max(answer[nxt], answer[cur] + 1)

            if indegree[nxt] == 0:
                q.append(nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
answer = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

solve()
print(*answer[1:])