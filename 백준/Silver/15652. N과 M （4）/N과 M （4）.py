import sys
# sys.stdin = open("input.txt")

def comb_rep(nums, r):
    result = []
    if r == 0:
        return [[]]
    for i in range(len(nums)):
        ele = nums[i]
        rest = nums[i:]
        for res in comb_rep(rest, r-1):
            result.append([ele] + res)

    return result


n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

for ls in comb_rep(nums, m):
    print(*ls)