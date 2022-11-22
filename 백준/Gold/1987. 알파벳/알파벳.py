import sys
# sys.stdin = open("input.txt")

def dfs(a, b, cnt):
    global answer

    if answer < cnt:
        answer = cnt

    for i in range(4):
        na = a + dr[i]
        nb = b + dc[i]
        if 0 <= na < r and 0 <= nb < c:
            if not visited[arr[na][nb]]:
                visited[arr[na][nb]] = True
                dfs(na, nb, cnt + 1)
                visited[arr[na][nb]] = False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r, c = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(input()))

for i in range(r):
    for j in range(c):
        arr[i][j] = ord(arr[i][j]) - ord("A")

visited = [False] * 26

answer = 0
visited[arr[0][0]] = True
dfs(0, 0, 1)
print(answer)
