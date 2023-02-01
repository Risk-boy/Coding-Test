import sys
# sys.stdin = open("input.txt")

n = int(input())
n -= 1
arr = list(map(int, input().split()))
target = arr[-1]
dp = [[[0, False] for _ in range(21)] for _ in range(n)]
dp[0][arr[0]][0] = 1
dp[0][arr[0]][1] = True

for i in range(1, n):
    for j in range(21):
        if dp[i - 1][j][1]:
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]][0] += (dp[i - 1][j][0])
                dp[i][j + arr[i]][1] = True
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]][0] += (dp[i - 1][j][0])
                dp[i][j - arr[i]][1] = True

print(dp[n - 1][target][0])