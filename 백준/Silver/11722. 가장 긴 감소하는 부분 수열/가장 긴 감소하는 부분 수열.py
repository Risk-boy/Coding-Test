# import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

# i 번째까지 가장 긴 감소하는 부분 수열 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))