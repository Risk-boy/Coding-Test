# import sys
# sys.stdin = open("input.txt")

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    # 자기 색깔이 아닌 곳 중 최소값 + 자기 자신
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))