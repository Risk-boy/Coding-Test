# import sys
# sys.stdin = open("input.txt")

n = int(input())

arr = list(map(int, input().split()))
arr_reverse = []
for i in range(n-1, -1, -1):
    arr_reverse.append(arr[i])

dp01 = [1] * n  # LIS
dp02 = [1] * n  # 주어진 수열을 뒤집어서 LIS

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp01[i] = max(dp01[i], dp01[j] + 1)
        if arr_reverse[i] > arr_reverse[j]:
            dp02[i] = max(dp02[i], dp02[j] + 1)

# dp02 다시 뒤집기
for i in range(n // 2):
    dp02[i], dp02[n-1-i] = dp02[n-1-i], dp02[i]

# dp01과 dp02 각각의 원소를 더해 가장 긴 길이 구하기
answer = 0
for i in range(n):
    if answer < dp01[i] + dp02[i]:
        answer = dp01[i] + dp02[i]
print(answer - 1)
