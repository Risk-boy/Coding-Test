import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
'''
리프노드들끼리만 연결
'''

def dfs(x, plus):
    global max_d, distance
    for node in graph[x]:
        if not visited[node[0]]:
            distance += node[1]
            visited[node[0]] = True
            dfs(node[0], node[1])
    if max_d < distance:
        max_d = distance
    visited[x] = False
    distance -= plus
    return

n = int(input())
if n == 1:
    print(0)
    exit()
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))


visited = [False] * (n + 1)
max_d = 0
distance = 0
for i in range(p + 1, n + 1):
    visited[i] = True
    dfs(i, 0)

print(max_d)
