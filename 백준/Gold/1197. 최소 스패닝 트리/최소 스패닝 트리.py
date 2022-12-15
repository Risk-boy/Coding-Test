import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


v, e = map(int, input().split())
graph = []
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    # 비용을 맨 앞으로
    graph.append([c, a, b])

graph.sort()

answer = 0
for cost, start, end in graph:
    start = find_parent(parent, start)
    end = find_parent(parent, end)
    if start != end:
        if start > end:
            parent[start] = end
        else:
            parent[end] = start
        answer += cost
print(answer)
