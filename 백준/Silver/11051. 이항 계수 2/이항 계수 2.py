import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(n, r):
    if dp[n][r] > 0:
        return dp[n][r]
    
    if n == r or r == 0:
        dp[n][r] = 1
        return 1

    dp[n][r] = (solve(n-1, r-1) + solve(n-1, r)) % 10007

    return dp[n][r]

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
solve(n, k)
print(dp[n][k])