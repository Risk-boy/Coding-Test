import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def dfs(x, cnt):
    global check
    if cnt == 4:
        check = True
        return

    for nxt in graph[x]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, cnt + 1)
            visited[nxt] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = False
for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, 0)
    if check:
        print(1)
        exit()

print(0)
