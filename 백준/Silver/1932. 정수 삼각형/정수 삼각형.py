# import sys
# sys.stdin = open("input.txt")

n = int(input())

dp = [[] for _ in range(n)]

for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(len(ls)):
        dp[i].append(ls[j])

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][0] += dp[i-1][0]
        elif j == i:
            dp[i][-1] += dp[i-1][-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

answer = 0

print(max(dp[-1]))