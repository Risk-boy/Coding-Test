# import sys
# sys.stdin = open("input.txt")

n = int(input())
nums = list(map(int, input().split()))

# 숫자 범위: -1000 ~ 1000
dp = [-1001] * n
dp[0] = nums[0]

for i in range(1, n):
    # 이전 값이 -1001이 아니고 누적합이 0보다 크면
    if dp[i-1] != -1001 and (dp[i-1] + nums[i]) > 0:
        dp[i] = max(dp[i-1] + nums[i], nums[i])
 
    else:
        dp[i] = nums[i]


print(max(dp))
