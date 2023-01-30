import sys
# sys.stdin = open("input.txt")

'''
자기보다 큰 수 있으면 바로 채우기
자기 자리에 작은 수가 있으면 큰 수 나올 때 까지 뒤로 가기
'''
n = int(input())
arr = list(map(int, input().split()))

nums = [11 for _ in range(n)]

for i in range(n):
    idx = arr[i]
    num = i + 1
    cnt = -1
    for j in range(n):
        if nums[j] > num:
            cnt += 1
            if cnt == idx:
                nums[j] = num
                break

print(*nums)
