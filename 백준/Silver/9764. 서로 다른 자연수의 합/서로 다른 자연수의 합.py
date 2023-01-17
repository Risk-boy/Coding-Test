import sys
# sys.stdin = open("input.txt")

'''
dp[i][j]: i를 만들 때 가장 큰 숫자가 j인 경우
prefix_sum을 이용해 시간초과 해결
'''
p = 100999
dp = [[0] * 2001 for _ in range(2001)]
prefix_sum = [[0] * 2001 for _ in range(2001)]

dp[0][0] = 1
for i in range(1, 2001):
    prefix_sum[0][i] = prefix_sum[0][i - 1] + dp[0][i - 1]

for i in range(1, 2001):
    for j in range(1, i + 1):
        dp[i][j] += prefix_sum[i - j][j] % p
    for j in range(1, 2001):
        prefix_sum[i][j] = (prefix_sum[i][j - 1] + dp[i][j - 1]) % p
        
T = int(input())
for _ in range(T):
    n = int(input())

    print(prefix_sum[n][n] + 1)