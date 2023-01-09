import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(3):
    if n >= arr[i]:
        answer += arr[i]
    else:
        answer += n

print(answer)