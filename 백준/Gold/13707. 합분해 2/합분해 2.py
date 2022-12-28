import sys
# sys.stdin = open("input.txt")


'''
dp[i][j]: j개의 수를 이용해 i가 되는 경우의 수
'''
n, k = map(int, input().split())
p = int(1e9)

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(k + 1): # 0을 만드는 경우의 수 = 1
    dp[0][i] = 1

for j in range(1, k + 1):
    for i in range(1, n + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % p

print(dp[n][k])