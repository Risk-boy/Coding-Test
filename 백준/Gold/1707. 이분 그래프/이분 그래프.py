import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline 
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = (visited[cur] + 1) % 2
            elif visited[next] == visited[cur]:
                return False
    return True
T = int(input())
for _ in range(T):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [-1] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == -1:
            check = bfs(i)
            if not check:
                break
    if check:
        print("YES")
    else:
        print("NO")

