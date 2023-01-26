import sys
# sys.stdin = open("input.txt")

def get_distance(x1, y1, x2, y2):
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
n = int(input())
parent = [i for i in range(n + 1)]
ls = [[]]
for _ in range(n):
    x, y = map(float, input().split())
    ls.append([x, y])
graph = []
for i in range(n):
    if i == 0:
        continue
    for j in range(i + 1, n + 1):
        graph.append([get_distance(ls[i][0], ls[i][1], ls[j][0], ls[j][1]), i, j])

graph.sort()
answer = 0
for cost, start, end in graph:
    start = find(start)
    end = find(end)
    if start != end:
        if start < end:
            parent[end] = start
        else:
            parent[start] = end
        answer += cost

print(answer)

