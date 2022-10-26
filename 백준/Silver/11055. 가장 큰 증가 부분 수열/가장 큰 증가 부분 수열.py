# import sys
# sys.stdin = open("input.txt")

n = int(input())

arr = list(map(int, input().split()))

# i 번째를 포함하는 가장 큰 LIS 합
dp = []
for num in arr:
    dp.append(num)
for i in range(1, n):
    for j in range(i):
        # LIS 조건을 만족하고
        if arr[j] < arr[i]:
            # 이전까지 합 + 자기자신 보다 작으면
            if dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

print(max(dp))
