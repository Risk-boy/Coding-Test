import sys
# sys.stdin = open("input.txt")

'''
첫 집에 먼저 칠해주고 생각
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 1000000
for i in range(3):
    dp = [[1000000] * 3 for _ in range(n)]
    dp[0][i] = arr[0][i] # 먼저 고정으로 칠해주기
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]

    for k in range(3):
        if k != i:
            answer = min(answer, dp[n - 1][k])

print(answer)




