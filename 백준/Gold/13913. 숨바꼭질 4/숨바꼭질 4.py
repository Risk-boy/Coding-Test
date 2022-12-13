import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(n, k):
    q = deque()
    q.append((n, 0))

    visited[n] = True
    while q:
        now, dist = q.popleft()

        if now == k:
            return dist

        for new in [now-1, now+1, now*2]:
            if 0 <= new < 100001:
                if not visited[new]:
                    visited[new] = True
                    q.append((new, dist+1))
                    path[new] = now


n, k = map(int, input().split())
visited = [False] * 100001
path = [0] * 100001
route = [k]
answer = bfs(n, k)
print(answer)
temp = k
for _ in range(answer):
    route.append(path[temp])
    temp = path[temp]

print(*route[::-1])








