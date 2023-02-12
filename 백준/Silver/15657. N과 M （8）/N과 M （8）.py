import sys
# sys.stdin = open("input.txt")


def solve(x, ls):
    if len(ls) == m:
        print(*ls)
        return
    for k in range(x, n):
        solve(k, ls + [nums[k]])
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in range(n):
    solve(i, [nums[i]])

