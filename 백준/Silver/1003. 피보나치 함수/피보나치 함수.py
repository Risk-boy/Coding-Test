import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp0[0] = 1
    dp1[0] = 0
    if n >= 1:
        dp0[1] = 0
        dp1[1] = 1
    if n >= 2:
        for i in range(2, n + 1):
            dp0[i] = dp0[i - 1] + dp0[i - 2]
            dp1[i] = dp1[i - 1] + dp1[i - 2]
    print(dp0[n], dp1[n])