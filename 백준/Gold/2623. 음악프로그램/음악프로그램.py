import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def solve():
    q = deque()
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    if len(result) == n:
        for num in result:
            print(num)
    else:
        print(0)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(2, temp[0] + 1):
        graph[temp[i - 1]].append(temp[i])
        indegree[temp[i]] += 1

solve()
