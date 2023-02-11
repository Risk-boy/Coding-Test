import sys
# sys.stdin = open("input.txt")
from collections import deque


n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = deque([i for i in range(1, n + 1)])

q.rotate()      # 오른쪽으로 한칸
q.rotate(-1)    # 왼쪽으로 한칸

answer = 0
cnt = 0
idx = 0
while cnt != len(arr):
    for i in range(len(q)):
        if q[i] == arr[cnt]:
            idx = i
            break
    if idx <= len(q) // 2:
        while q[0] != arr[cnt]:
            q.rotate(-1)
            answer += 1
    else:
        while q[0] != arr[cnt]:
            q.rotate()
            answer += 1
    q.popleft()
    cnt += 1

print(answer)