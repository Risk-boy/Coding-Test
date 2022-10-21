# import sys
# sys.stdin = open("input.txt")

n = int(input())
# 계단 정보
arr = [0]
# dp 초기화, n <= 300
dp = [0] * (n+1)
for i in range(n):
    arr.append(int(input()))

# n 이 작은 수일 경우 runtime error 발생
dp[1] = arr[1]
if n >= 2:
    dp[2] = arr[1] + arr[2]
if n >= 3:
    dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
    
for i in range(4, n+1):
    # 세번째 전 계단까지의 최대 + 바로 전계단 + 자기자신
    # vs
    # 두번째 전 계단까지의 최대 + 자기자신
    dp[i] = max(dp[i-3] + arr[i-1], dp[i-2]) + arr[i]

print(dp[n])