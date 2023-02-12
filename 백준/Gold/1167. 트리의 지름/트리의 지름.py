import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline 

def dfs(x, dist):
    for node, d in graph[x]:
        if not visited[node]:
            distance[node] = dist + d
            visited[node] = True
            dfs(node, dist + d)




v = int(input())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    i = 1
    while i < len(temp) - 1:
        graph[temp[0]].append((temp[i], temp[i + 1]))
        i += 2


distance = [0] * (v + 1)
visited = [False] * (v + 1)
visited[1] = True
dfs(1, 0)
a = distance.index(max(distance))
distance = [0] * (v + 1)
visited = [False] * (v + 1)
visited[a] = True
dfs(a, 0)

print(max(distance))

