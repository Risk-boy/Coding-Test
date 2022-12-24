import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
nums = list(set(arr))
nums.sort(reverse=True)
cnt = len(nums) - 1
dict = {}
for i in range(len(nums)):
    if nums[i] not in dict:
        dict.setdefault(nums[i], cnt)
        cnt -= 1

for i in range(n):
    print(dict[arr[i]], end=" ")