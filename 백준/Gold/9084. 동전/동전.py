import sys
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n = int(input()) # 동전 종류
    coin = [0] + list(map(int, input().split())) # 1 ~ 10000원 가능
    m = int(input()) # 만들어야 할 금액

    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    # dp[i][j]: i번째 동전사용 j 금액 만드는 방법 수
    for i in range(1, n+1):
        for j in range(m+1):
            if coin[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin[i]]
    print(dp[n][m])
# good!!!!

