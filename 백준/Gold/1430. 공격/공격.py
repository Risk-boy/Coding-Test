import sys, math
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve(start):
    global answer
    q = deque()
    q.append((start, d))
    visited = [False] * n
    visited[start] = True
    while q:
        cur, power = q.popleft()
        if graph[cur][0] <= r:
            answer += power
            return
        for nxt in range(n):
            if get_distance(graph[nxt][1], graph[nxt][2], graph[cur][1], graph[cur][2]) <= r:
                if not visited[nxt]:
                    q.append((nxt, power / 2))
                    visited[nxt] = True


n, r, d, x, y = map(int, input().split())
graph = []

for _ in range(n):
    _x, _y = map(int, input().split())
    graph.append([get_distance(_x, _y, x, y), _x, _y, d])

graph.sort()
answer = 0
for i in range(n):
    solve(i)

print(answer)
