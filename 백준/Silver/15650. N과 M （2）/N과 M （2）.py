import sys
# sys.stdin = open("input.txt")

def comb(nums, r):
    result = []
    if r == 0:
         return [[]]
    for i in range(len(nums)):
        ele = nums[i]
        rest = nums[i + 1:]
        for res in comb(rest, r - 1):
            result.append([ele] + res)
    return result

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
for ls in comb(nums, m):
    print(*ls)