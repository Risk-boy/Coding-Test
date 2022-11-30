import sys
# sys.stdin = open("input.txt")

n = int(input())

dp = [0] * (1001)

p = 10007

dp[1] = 1
dp[2] = 3
dp[3] = 5
for i in range(4, n + 1):
    dp[i] = (dp[i-1] % p) + (2 * dp[i-2]) % p

print(dp[n] % p)
