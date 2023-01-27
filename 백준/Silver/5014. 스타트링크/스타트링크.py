import sys
# sys.stdin = open("input.txt")
from collections import deque


'''
총 f층, g층에 가야함, 현재 s층
'''

def solve(x):
    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q:
        cur, cnt = q.popleft()
        if cur == g:
            return cnt

        for go in [u, -d]:
            next = cur + go
            if 1 <= next <= f:
                if not visited[next]:
                    q.append((next, cnt + 1))
                    visited[next] = True

    return -1
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)
answer = solve(s)

if answer != -1:
    print(answer)
else:
    print("use the stairs")
