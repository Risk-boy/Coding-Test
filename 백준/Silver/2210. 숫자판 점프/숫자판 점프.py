import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(int(1e6))

def solve(r, c, num, cnt):
    if cnt == 6:
        if num not in visited:
            visited.append(num)
        return
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:
            solve(nr, nc, num + str(arr[nr][nc]), cnt + 1)
    return

arr = [list(map(int, input().split())) for _ in range(5)]

visited = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(5):
    for j in range(5):
        solve(i, j, str(arr[i][j]), 1)


print(len(visited))