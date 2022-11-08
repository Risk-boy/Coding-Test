# import sys
# sys.stdin = open("input.txt")


n, k = map(int, input().split())

# dp[k][n]: 정수 k개를 더해 합이 n이 되는 경우의 수
# dp[k][n] = dp[k-1][0] + dp[k-1][1] +...+ dp[k-1][n-1] + dp[k-1][n]

dp = [[0] * (n + 1) for _ in range(k + 1)]

dp[0][0] = 1

for r in range(1, k + 1):
    for c in range(n + 1):
        for i in range(c + 1):
            dp[r][c] += dp[r-1][i]

print(dp[k][n] % 1000000000)