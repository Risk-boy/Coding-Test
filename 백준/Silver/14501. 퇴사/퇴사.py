import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = [[0, 0] for _ in range(n)]
dp = [0] * (n + 6) # t 최대 값은 5
for i in range(n):
    t, p = map(int, input().split())
    arr[i][0] = t
    arr[i][1] = p

for i in range(1, n + 1):
    for j in range(i):
        t = arr[j][0]
        p = arr[j][1]
        if j + t <= i:
            dp[i] = max(dp[i], dp[j] + p)

print(max(dp[:n+1]))


