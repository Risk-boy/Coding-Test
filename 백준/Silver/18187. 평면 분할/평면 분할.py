import sys
# sys.stdin = open("input.txt")

n = int(input())

dp = [0] * (n+1)
dp[1] = 2
line = [1, 0, 0]

for i in range(2, n+1):
    line.sort(reverse=True)
    dp[i] = dp[i-1] + sum(line[:2]) + 1
    line[2] += 1

print(dp[n])