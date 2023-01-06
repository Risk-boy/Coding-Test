import sys
# sys.stdin = open("input.txt")
import math
'''
dp[i]: i명 늘리는데 필요한 최소 비용
'''

c, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# arr[i][0]: 비용 / arr[i][1]: 고객수

dp = [100000 for _ in range(1101)]
dp[0] = 0
for i in range(n):
    for j in range(1, 1101):
        k = j - arr[i][1]
        if k < 0:
            k = 0
        dp[j] = min(dp[j], dp[k] + arr[i][0])


print(min(dp[c:]))