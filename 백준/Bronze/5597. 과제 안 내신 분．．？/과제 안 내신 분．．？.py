nums = []
for i in range(1, 31):
    nums.append(i)

for _ in range(28):
    idx = nums.index(int(input()))
    nums.pop(idx)

nums.sort()
for i in range(2):
    print(nums[i])