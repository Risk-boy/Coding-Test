import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
'''
0 ~ 256 까지의 높이 각각에 대해 걸리는 시간 구하기
'''

n, m, cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_time =  500 * 500 * 256 * 2
max_height = 0
for h in range(257):
    spare = cnt
    time = 0
    for i in range(n):
        for j in range(m):
            diff = arr[i][j] - h
            if diff > 0:
                spare += diff
                time += 2 * diff
            else:
                spare -= abs(diff)
                time += abs(diff)

    if spare < 0:
        continue

    if min_time >= time:
        min_time = time
        height = h
        max_height = max(max_height, height)

print(min_time, max_height)