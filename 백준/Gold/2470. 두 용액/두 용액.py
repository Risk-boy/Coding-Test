import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

arr.sort()
start = 0
end = n - 1
minSum = 2 * int(1e9)
a, b = -1, -1
while start < end:
    result = arr[start] + arr[end]
    if result == 0:
        a = start
        b = end 
        break

    # 차이가 작으면 되므로 절대값으로
    if minSum > abs(result):
        minSum = abs(result)
        a = start
        b = end
    if result < 0:
        start += 1
    if result > 0:
        end -= 1

print(arr[a], arr[b])
