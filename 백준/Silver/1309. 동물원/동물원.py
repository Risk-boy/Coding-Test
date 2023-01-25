import sys
# sys.stdin = open("input.txt")

'''
왼쪽 / 오른쪽 각각의 칸에 대해서 사자 있는 경우 없는 경우
'''

n = int(input())
p = 9901
# 왼쪽 / 오른쪽 / 둘다 없음
dp = [[0, 0, 0] for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, n):
    dp[i][0] += (dp[i - 1][1] + dp[i - 1][2]) % p
    dp[i][1] += (dp[i - 1][0] + dp[i - 1][2]) % p
    dp[i][2] += sum(dp[i - 1]) % p

print(sum(dp[n - 1]) % 9901)