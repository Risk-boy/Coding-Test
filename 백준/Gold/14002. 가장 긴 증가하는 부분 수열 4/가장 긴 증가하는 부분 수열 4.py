# import sys
# sys.stdin = open("input.txt")


def go(p):
    if p == -1:
        return
    go(v[p])
    print(arr[p],end=' ')


n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
v = [-1] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            v[i] = j

# print(arr)
# print(f"dp: {dp}")
# print(f"v: {v}")
ans = max(dp)
print(ans)
p = [i for i, x in enumerate(dp) if x == ans][0]
go(p)
