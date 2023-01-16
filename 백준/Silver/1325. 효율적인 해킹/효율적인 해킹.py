import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline
'''
a b 가 주어질 때 b를 해킹하면 a를 해킹 가능
'''
def bfs(x):
    global cnt
    q = deque()
    visited[x] = True
    q.append(x)

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
max_cnt = 0
answer = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    cnt = 0
    bfs(i)
    answer[i] = cnt
    if cnt > max_cnt:
        max_cnt = cnt

for i in range(1, n + 1):
    if answer[i] == max_cnt:
        print(i, end=" ")