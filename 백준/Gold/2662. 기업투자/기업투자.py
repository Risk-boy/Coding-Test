import sys
# sys.stdin = open("input.txt")
from copy import deepcopy

# n: 금액 / m: 기업수
n, m = map(int, input().split())
arr = [0]

for _ in range(n):
    arr.append(list(map(int, input().split()))[1:])

dp = [0] * (n+1)
# 얼마씩 투자했는지 저장
path = [[] for _ in range(n+1)]

for i in range(m):
    for j in range(n, -1, -1):
        temp = 0
        for k in range(1, j+1):
            if dp[j] < dp[j-k] + arr[k][i]:
                dp[j] = dp[j-k] + arr[k][i]
                path[j] = deepcopy(path[j-k])
                temp = k
        path[j].append(temp)

print(dp[-1])
print(*path[-1])



