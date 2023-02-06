import sys
# sys.stdin = open("input.txt")
from itertools import permutations

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
ls = list(permutations(arr, m))
for nums in ls:
    print(*nums)
