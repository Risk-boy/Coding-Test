import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())


def nCr(n, r):

    if n < r:
        return

    if n == r or r == 0:
        dp[n][r] = 1
        return dp[n][r]
    dp[n][r] = nCr(n-1, r-1) + nCr(n-1, r)
    
    return dp[n][r]


dp = [[0] * (k + 1) for _ in range(n + 1)]


nCr(n, k)

print(dp[n][k])
