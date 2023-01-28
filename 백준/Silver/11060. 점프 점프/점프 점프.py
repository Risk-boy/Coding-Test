import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve(start):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        cur, cnt = q.popleft()
        if cur == n - 1:
            return cnt

        for i in range(1, arr[cur] + 1):
            next = cur + i
            if next < n:
                if not visited[next]:
                    q.append((next, cnt + 1))
                    visited[next] = True

    return -1
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n

answer = solve(0)

print(answer)