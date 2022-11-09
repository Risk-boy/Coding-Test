# import sys
# sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

interval_sum = arr[0]
end = 1
cnt = 0
for start in range(n):

    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1

    if interval_sum == m:
        cnt += 1

    interval_sum -= arr[start]


print(cnt)