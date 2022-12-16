import sys
# sys.stdin = open("input.txt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = sum(arr[:k])
prefix_sum = sum(arr[:k])

for i in range(k, n):
    prefix_sum = prefix_sum + arr[i] - arr[i-k]
    if answer < prefix_sum:
        answer = prefix_sum

print(answer)
