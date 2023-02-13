import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve():
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                result.append(nxt)
    print(*result)
    
    
n = int(input())

ls = []
for _ in range(3):
    ls.append(list(map(int, input().split())))

temp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(3):
    for j in range(n):
        for k in range(j + 1, n):
            temp[ls[i][j]][ls[i][k]] += 1
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if temp[i][j] > 1:
            graph[i].append(j)
            indegree[j] += 1

solve()