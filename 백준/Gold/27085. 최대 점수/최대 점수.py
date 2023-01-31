import sys
# sys.stdin = open("input.txt")

INF = int(2e14)
n, s = map(int, input().split())
arr = list(map(int, input().split()))
q = [[], []]

for direction in [1, -1]:
    total = min_value = 0
    i = s + direction - 1
    if direction > 0:
        k = 0
    else:
        k = 1

    while 0 <= i < n:
        total += arr[i]
        min_value = min(min_value, total)
        if total > 0:
            q[k].append((-min_value, total))
            total = min_value = 0
        i += direction
    q[k].append((INF, -1))

answer = 0

while answer >= min(q[0][0][0], q[1][0][0]): # 던전을 계속 진행 가능 한경우
    if q[0][0][0] > q[1][0][0]: # 오른쪽으로 진행
        answer += q[1][0][1]
        q[1].pop(0)
    else:   # 왼쪽으로 진행
        answer += q[0][0][1]
        q[0].pop(0)

print(answer)

