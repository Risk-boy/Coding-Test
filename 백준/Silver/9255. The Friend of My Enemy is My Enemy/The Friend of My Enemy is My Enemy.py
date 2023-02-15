import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)

    start = int(input())
    print(f"Data Set {tc}:")
    print(*sorted(graph[start]))
    print()