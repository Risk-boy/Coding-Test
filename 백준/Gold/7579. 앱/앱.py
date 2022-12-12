import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())

memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
C = sum(cost)
# dp[i][j]: i번째까지 사용해서 j크기의 cost를 채울 때 최대 memory
dp = [[0] * (C + 1) for _ in range(n+1)]
answer = C + 1
for i in range(1, n+1):
    for j in range(0, C+1):
        if cost[i] > j: # 비활성화 불가
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])
        if dp[i][j] >= m:
            answer = min(answer, j)

print(answer)



