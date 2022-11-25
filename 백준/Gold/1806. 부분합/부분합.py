# 문제 꼼꼼하게 읽자!!!!!
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

minLen = 100000
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += arr[end]
        end += 1
    if interval_sum >= s:
        Len = end - start
        if minLen > Len:
            minLen = Len
    interval_sum -= arr[start]
    
if minLen == 100000:
    print(0)
else:
    print(minLen)