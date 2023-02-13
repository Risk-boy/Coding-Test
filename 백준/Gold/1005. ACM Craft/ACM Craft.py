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

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(input())
    answer = [0 for _ in range(n + 1)]
    solve()
    print(answer[target])