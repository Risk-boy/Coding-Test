# import sys
# sys.stdin = open("input.txt")

n = int(input())

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5

for i in range(9, 101):
    dp[i] = dp[i-5] + dp[i-1]
for _ in range(n):
    num = int(input())
    print(dp[num])


