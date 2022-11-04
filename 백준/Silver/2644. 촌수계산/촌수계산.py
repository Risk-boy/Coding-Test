# import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        s = queue.popleft()
        if s == end:
            return
        for x in arr[s]:
            if not visited[x]:
                visited[x] = visited[s] + 1
                queue.append(x)
    return


n = int(input())

start, end = map(int, input().split())

e = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(e):
    p, c = map(int, input().split())
    arr[p].append(c)
    arr[c].append(p)

visited = [0] * (n+1)
bfs(start)

if visited[end]:
    print(visited[end] - 1)
else:
    print(-1)