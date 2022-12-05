import sys
# sys.stdin = open("input.txt")


def solve(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    temp = solve(n // 2)
    if n % 2 == 1:
        return (temp * temp * 2) % p
    else:
        return (temp * temp) % p


T = int(input())
p = int(1e9) + 7
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(solve(n-2))