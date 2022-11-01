# import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [0] * 100001

    visited[s] = 1

    while queue:
        r = queue.popleft()

        for nr in [r-1, r+1, r*2]:
            if nr == k:
                return visited[r] + 1
            else:
                if nr < 0 or nr > 100000:
                    continue
                if not visited[nr]:
                    visited[nr] = visited[r] + 1
                    queue.append(nr)


# 수빈, 동생 위치
n, k = map(int, input().split())

if n == k:
    print(0)
else:
    print(bfs(n) - 1)