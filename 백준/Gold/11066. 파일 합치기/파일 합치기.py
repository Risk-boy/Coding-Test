# import sys
import math
# sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    # dp[i][j]: i부터 j번째 까지 파일을 합치는데 드는 비용
    dp = [[math.inf] * n for _ in range(n)]

    # arr[i]+arr[i+1]+...+arr[j]를 구하기 위해 누적합 리스트 만들기
    csum = [0] * n
    csum[0] = arr[0]
    for i in range(1, n):
        csum[i] = csum[i-1] + arr[i]
    # 인덱스 범위가 벗어나서 csum[-1]을 호출할 때 0을 불러와주기위함
    csum.append(0)
    
    for i in range(n-1):
        dp[i][i] = 0
        dp[i][i+1] = arr[i] + arr[i+1]
    dp[n-1][n-1] = 0

    # dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+arr[i]+...+arr[j])
    for step in range(1, n):
        for i in range(n - step):
            j = i + step
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+csum[j]-csum[i-1])

    print(dp[0][n-1])




