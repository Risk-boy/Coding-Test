import sys
# sys.stdin = open("input.txt")
from collections import deque
import math


def bfs(a, b):
    global flag
    q = deque()
    q.append((a, 0))
    visited[a] = True

    while q:
        n, cnt = q.popleft()
        if n == b:
            flag = True
            return cnt
        n = str(n)
        # 천의 자리 ~ 일의 자리 순차적으로 변경
        for i in range(4):
            for j in range(10):
                new = n[:i] + str(j) + n[i+1:]
                new = int(new)
                if new in prime and not visited[new]:
                    visited[new] = True
                    q.append((new, cnt+1))

# 에라토스테네스 체
arr = [True] * 10001
arr[0], arr[1] = False, False
for i in range(2, 101):
    if arr[i]:
        j = 2
        while i * j <= 10000:
            arr[i * j] = False
            j += 1
# 4자리수 소수들
prime = []
for i in range(1000, 10001):
    if arr[i]:
        prime.append(i)

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue

    visited = [False] * (10000)
    flag = False
    answer = bfs(a, b)
    if flag:
        print(answer)
    else:
        print("impossible")


