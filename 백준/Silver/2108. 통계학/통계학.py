import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input()) # n은 홀수
arr = []
dict = {}
for _ in range(n):
    num = int(input())
    arr.append(num)
    if num not in dict.keys():
        dict[num] = 1
    else:
        dict[num] += 1

arr.sort()

# 산술평균
mean = round(sum(arr) / n)

# 중앙값
median = arr[n // 2]

# 최빈값
maxCnt = max(dict.values())
temp = []
for key in dict.keys():
    if dict[key] == maxCnt:
        temp.append(key)

if len(temp) == 1:
    mode = temp[0]
else:
    mode = sorted(temp)[1]

# 범위
range = arr[-1] - arr[0]

print(mean)
print(median)
print(mode)
print(range)