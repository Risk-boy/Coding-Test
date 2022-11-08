# import sys
# sys.stdin = open("input.txt")

n = int(input())

# dp[n] : n을 제곱수로 나타낼 때 필요한 최소항의 개수
# n을 1로만 나타냈을 경우가 최대이므로 dp[n]를 i로 설정

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    j = 1
    # while j ** 2 <= i:
    while j * j <= i:
        if dp[i] > dp[i - j * j]:
            dp[i] = dp[i - j * j] + 1
        # min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])
