import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph.append((cost, start, end))

graph.sort()

answer = 0
last = 0
for cost, start, end in graph:
    start = find(start)
    end = find(end)
    if start != end:
        if start < end:
            parent[end] = start
        else:
            parent[start] = end
        answer += cost
        last = cost
print(answer - last)
