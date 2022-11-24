import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def comb(nums, r):
    result = []
    if r == 0:
        return [[]]
    for i in range(len(nums)):
        ele = nums[i]
        rest = []
        for i in range(len(nums)):
            if ele == nums[i]:
                continue
            else:
                rest.append(nums[i])
        for res in comb(rest, r - 1):
            result.append([ele] + res)
    return result
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for ls in comb(arr, m):
    print(*ls)
