import sys
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = arr[0][0]
    dp2[0] = arr[1][0]
    if n >= 2:
        dp1[1] = arr[0][1] + arr[1][0]
        dp2[1] = arr[0][0] + arr[1][1]
    for i in range(2, n):
        dp1[i] = arr[0][i] + max(dp2[i-2], dp2[i-1])
        dp2[i] = arr[1][i] + max(dp1[i-2], dp1[i-1])
    if n == 1:
        print(max(dp1[0], dp2[0]))
    else:
        print(max(dp1[n-1], dp2[n-1]))





