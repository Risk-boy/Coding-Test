import sys
# sys.stdin = open("input.txt")

'''
중앙에서 다른곳: 2
인접한곳: 3
반대편: 4
같은곳 다시: 1
dp[i][j][k]: i번째 움직였을 때 j: 왼쪽 발 위치 k: 오른쪽 발 위치
ㅇㅇ...
'''
def power(cur, nxt):
    if cur == 0:
        return 2
    elif cur == nxt:
        return 1
    elif (cur - nxt) % 2 == 1:
        return 3
    else:
        return 4
arr = list(map(int, input().split()))
n = len(arr)
dp = [[[400000 for _ in range(5)] for _ in range(5)] for _ in range(n)]
dp[0][0][0] = 0
for i in range(1, n):
    next = arr[i - 1]
    for left in range(5):
        for right in range(5):
            dp[i][next][right] = min(dp[i][next][right], dp[i-1][left][right] + power(left, next))
            dp[i][left][next] = min(dp[i][left][next], dp[i-1][left][right] + power(right, next))

answer = 400000
for i in range(5):
    for j in range(5):
        answer = min(answer, dp[n - 1][i][j])

print(answer)