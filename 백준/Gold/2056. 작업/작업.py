import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def solve():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = time[i]

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            answer[nxt] = max(answer[nxt], answer[cur] + time[nxt])

            if indegree[nxt] == 0:
                q.append(nxt)

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
answer = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for j in range(2, len(temp)):
        graph[temp[j]].append(i)
        indegree[i] += 1

solve()

print(max(answer))