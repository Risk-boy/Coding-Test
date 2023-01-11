import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
dp[n]: n일까지 받을 수 있는 최대 금액
'''
n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    k = i + arr[i][0] - 1
    if k <= n: # 최대 일수를 넘기면 안됨
        dp[k] = max(dp[k], dp[i - 1] + arr[i][1])
    if k > i: # 일수가 맞아 떨어지지 않는 부분 체크
        dp[i] = max(dp[i - 1], dp[i])

print(max(dp))