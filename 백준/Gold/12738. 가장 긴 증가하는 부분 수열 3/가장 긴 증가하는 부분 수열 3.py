import sys
from bisect import bisect_left
# sys.stdin = open("input.txt")

'''
bisect 모듈 이용해보기
'''

n = int(input())
arr = list(map(int, input().split()))
dp = []
for num in arr:
    idx = bisect_left(dp, num)

    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))