import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = arr[i]
            q.append(i)

    while q:
        now = q.popleft()
        for node in graph[now]:
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)
            dp[node] = max(dp[node], dp[now] + arr[node])



n = int(input())

indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
# 각 건물을 짓는데 필요한 최소한의 시간
dp = [0 for _ in range(n + 1)]
# 각각의 건물을 짓는데 필요한 시간
arr = [0 for _ in range(n + 1)]


for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    arr[i] = temp[0]
    for j in range(1, len(temp) - 1):
        graph[temp[j]].append(i)
        indegree[i] += 1

solve()
for i in range(1, n + 1):
    print(dp[i])

