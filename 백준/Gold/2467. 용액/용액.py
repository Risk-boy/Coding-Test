import sys
# sys.stdin = open("input.txt")

'''
two pointers 사용
합의 절대값이 가장 작은 두 수 찾기
합이 음수이면 start를 증가시키기
합이 양수이면 end를 감소시키기
'''
n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1
min_value = 2000000000

while start < end:
    temp = arr[start] + arr[end]
    if min_value > abs(temp):
        min_value = abs(temp)
        left = arr[start]
        right = arr[end]
        if temp == 0:
            break

    if temp < 0:
        start += 1
    else:
        end -= 1

print(left, right)