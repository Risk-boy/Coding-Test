# import sys
# sys.stdin = open("input.txt")

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 왼쪽 전깃줄을 기준으로 정렬
arr.sort(key=lambda x: x[0])

# 오른쪽 전깃줄을 기준으로 LIS 구하기
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
