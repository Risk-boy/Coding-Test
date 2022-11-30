import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1
for i in range(n):
    for j in range(arr[i], k + 1):
        dp[j] = dp[j] + dp[j-arr[i]]


print(dp[k])

