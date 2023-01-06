import sys
# sys.stdin = open("input.txt")

'''
dp[i]: 체력 i일때 최대 기쁨
'''

n = int(input())
hp = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [0 for _ in range(100)]

for i in range(n):
    for j in range(99, hp[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - hp[i]] + joy[i])

print(dp[99])