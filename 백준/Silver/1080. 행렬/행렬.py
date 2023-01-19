import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
'''
한칸씩 이동하면서 숫자가 다르면 변경
남은 컬럼이 2개인데 숫자를 변경해야하면 불가능
'''
def change(x, y):
    for i in range(3):
        for j in range(3):
            A[x + i][y + j] = (A[x + i][y + j] + 1) % 2

n, m = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip())) for _ in range(n)]
B = [list(map(int, input().rstrip())) for _ in range(n)]
if n <= 2 or m <= 2:
    for r in range(n):
        for c in range(m):
            if A[r][c] != B[r][c]:
                print(-1)
                exit()
    print(0)
    exit()

cnt = 0
for r in range(n):
    for c in range(m):
        if A[r][c] != B[r][c]:
            if r <= n - 3 and c <= m - 3:
                change(r, c)
                cnt += 1
            else:
                print(-1)
                exit()

print(cnt)
