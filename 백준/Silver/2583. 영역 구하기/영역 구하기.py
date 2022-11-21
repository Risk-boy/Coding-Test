import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(r, c):
    global size
    if r <= -1 or r >= m or c <= -1 or c >= n:
        return False
    if arr[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        size += 1
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        return True
    return False


m, n, k = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] =  1

visited = [[False for _ in range(n)] for _ in range(m)]
answer = []
cnt = 0
for r in range(m):
    for c in range(n):
        if arr[r][c] == 0 and not visited[r][c]:
            cnt += 1
            size = 0
            dfs(r, c)
            answer.append(size)
print(cnt)
answer.sort()
print(*answer)