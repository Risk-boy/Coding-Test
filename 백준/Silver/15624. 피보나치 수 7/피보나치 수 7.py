import sys
# sys.stdin = open("input.txt")

n = int(input())
p = int(1e9) + 7
dp = [0] * (n + 1)
if n >= 1:
    dp[1] = 1
if n >= 2:
    for i in range(n - 1):
        dp[i + 2] = (dp[i] + dp[i + 1]) % p

print(dp[n])