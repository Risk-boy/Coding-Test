import sys
# sys.stdin = open("input.txt")
import math

m, n = map(int, input().split())

arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(m, n + 1):
    # 1 체크
    if i == 1:
        continue
    if arr[i]:
        print(i)