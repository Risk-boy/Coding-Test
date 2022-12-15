import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


n = int(input())
m = int(input())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = [i for i in range(n+1)]
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