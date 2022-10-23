# import sys
# sys.stdin = open("input.txt")

# 10^6 보다 작거나 같은 정수
n = int(input())
dp = [0] * 1000001

for i in range(2, n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])