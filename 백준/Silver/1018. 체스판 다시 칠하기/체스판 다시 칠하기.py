import sys
# sys.stdin = open("input.txt")


'''
첫번째 색을 바꾸는 경우의 수 = 64 - 첫번째 색을 안바꾸는 경우의수
'''

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
min_cnt = 64
for r in range(n - 7):
    for c in range(m - 7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if (r + i + c + j) % 2 == 0:
                    if arr[r + i][c + j] != "W":
                        cnt += 1
                else:
                    if arr[r + i][c + j] != "B":
                        cnt += 1
        min_cnt = min(min_cnt, cnt, 64 - cnt)

print(min_cnt)

