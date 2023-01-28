import sys
# sys.stdin = open("input.txt")
from collections import deque

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    if n == 1:
        print(1)
        continue
    q = deque(ls)
    check = True
    cnt = 1
    while check:
        for i in range(1, len(q)):
            if q[i] > q[0]:
                q.rotate(-1)
                m -= 1
                if m < 0:
                    m = len(q) - 1
                break
        else:
            if m == 0:
                print(cnt)
                check = False
                break
            else:
                q.popleft()
                cnt += 1
                m -= 1
    





