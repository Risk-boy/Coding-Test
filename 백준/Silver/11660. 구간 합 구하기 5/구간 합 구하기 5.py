import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

if n >= 2:
    for r in range(n + 1):
        for c in range(1, n + 1):
            arr[r][c] += arr[r][c-1]
    for c in range(n + 1):
        for r in range(1, n + 1):
            arr[r][c] += arr[r-1][c]

    for _ in range(m):
        a, b, c, d = map(int, input().split())
        answer = arr[c][d] - arr[c][b-1] - arr[a-1][d] + arr[a-1][b-1]

        print(answer)

if n == 1:
    for _ in range(m):
        print(arr[0])




