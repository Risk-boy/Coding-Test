import sys, math
# sys.stdin = open("input.txt")


def solve(n):
    maxCnt = 0
    maxBase = 2
    for x in range(2, n): # base
        cnt = 0
        sum = 0
        for i in range(int(math.log(n, x)) + 1):
            sum += x ** i
            cnt += 1
            if sum == n:
                if maxCnt < cnt:
                    maxCnt = cnt
                    maxBase = x
                break
            elif sum > n:
                break
    return maxBase

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    answer = solve(n)
    print(f"Case #{tc}: {answer}")