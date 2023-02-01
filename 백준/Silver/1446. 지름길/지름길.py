import sys
# sys.stdin = open("input.txt")

n, d = map(int, input().split())
graph = []
for _ in range(n):
    s, e, l = map(int, input().split())
    graph.append((s, e, l))

graph.sort()
INF = 10000
distance = [i for i in range(d + 1)]

for start, end, dist in graph:
    if end > d:
        continue
    if distance[end] > distance[start] + dist:
        distance[end] = distance[start] + dist
        for i in range(end + 1, d + 1):
            distance[i] = min(distance[i], distance[end] + i - end)

print(distance[d])