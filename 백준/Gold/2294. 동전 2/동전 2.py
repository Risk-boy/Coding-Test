import sys
# sys.stdin = open("input.txt")
INF = int(1e9)

# n가지 종류 동전 / 합이 k원
n, k = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(int(input()))

arr = list(set(arr))
dp = [INF] * (k + 1)
for x in arr:
    if x <= k:
        dp[x] = 1

for i in range(1, k + 1):
    for j in range(len(arr)):
        if i - arr[j] > 0:
            dp[i] = min(dp[i], dp[i - arr[j]] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])