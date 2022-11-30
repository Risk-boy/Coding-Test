import sys
# sys.stdin = open("input.txt")

n = int(input())
p = [0] + list(map(int, input().split()))

dp = []
for i in range(n + 1):
    dp.append(p[i])

for i in range(2, n + 1):
    for j in range(1, i + 1):
        for k in range(j, i + 1 - j):
            if j + k == i:
                dp[i] = max(dp[i], dp[j] + dp[k])

# print(dp)
print(dp[n])

