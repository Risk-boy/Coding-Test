import sys
# sys.stdin = open("input.txt")


'''
dp[i]: i 시간 공부했을 때 얻을 수 있는 최대점수
'''
n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(t + 1)]

for i in range(n):
    for j in range(t, arr[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - arr[i][0]] + arr[i][1])

print(dp[t])