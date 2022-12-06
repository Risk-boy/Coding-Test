import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * m for _ in range(n)]

dp[0][0] = arr[0][0]

for r in range(n):
    for c in range(m):
        if r > 0 and c > 0:
            dp[r][c] = arr[r][c] + max(dp[r-1][c-1], dp[r][c-1], dp[r-1][c])
        elif r > 0:
            dp[r][c] = arr[r][c] + dp[r-1][c]
        elif c > 0:
            dp[r][c] = arr[r][c] + dp[r][c-1]

print(dp[n-1][m-1])
