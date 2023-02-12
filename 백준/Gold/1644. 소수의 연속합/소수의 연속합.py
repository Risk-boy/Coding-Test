import sys, math
# sys.stdin = open("input.txt")

n = int(input())
arr = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1
primes = []
for i in range(2, n + 1):
    if arr[i]:
        primes.append(i)

cnt = 0
interval_sum = 0
end = 0
for start in range(len(primes)):
    while interval_sum < n and end < len(primes):
        interval_sum += primes[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= primes[start]

print(cnt)

