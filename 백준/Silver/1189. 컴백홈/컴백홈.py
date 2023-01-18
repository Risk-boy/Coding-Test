import sys
# sys.stdin = open("input.txt")

def solve(x, y, distance):
    global r, c, k, cnt
    if distance > k:
        return
    if distance == k:
        if x == 0 and y == c - 1:
            cnt += 1
            return
        else:
            return

    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and graph[nx][ny] != "T":
                visited[nx][ny] = True
                solve(nx, ny, distance + 1)
                visited[nx][ny] = False
    return

r, c, k = map(int, input().split())

graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited[r - 1][0] = True
cnt = 0

solve(r - 1, 0, 1)

print(cnt)