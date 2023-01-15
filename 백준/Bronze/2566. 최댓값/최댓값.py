import sys
# sys.stdin = open("input.txt")

arr = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_r = -1
max_c = -1

for r in range(9):
    for c in range(9):
        if arr[r][c] > max_num:
            max_num = arr[r][c]
            max_r = r
            max_c = c

print(max_num)
print(max_r + 1, max_c + 1)