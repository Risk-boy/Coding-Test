import sys
# sys.stdin = open("input.txt")

n = int(input())
INF = float("inf")
dp = [INF] * (5001)

dp[3] = 1
dp[5] = 1

a = 0
while a * 5 <= n:
    b = (n - a * 5) // 3
    if (n - a * 5) % 3 == 0:
        dp[n] = min(a + b * dp[3],  dp[n])
    a += 1

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])
