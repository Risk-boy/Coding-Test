import sys
# sys.stdin = open("input.txt")


n = int(input())
arr = [0] + list(map(int, input().split()))
answer = [0 for _ in range(n + 1)]
stack = []

for i in range(1, n+1):
    while stack:
        if stack[-1][1] > arr[i]:
            answer[i] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append((i, arr[i]))

print(*answer[1:])

