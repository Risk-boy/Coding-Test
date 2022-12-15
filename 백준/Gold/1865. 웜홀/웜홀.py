import sys
# sys.stdin = open("input.txt")
INF = int(1e9)


def solve(start):

    dist[start] = 0

    for i in range(n+1):
        for j in range(len(graph)):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]

            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n:
                    return True
    return False

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    graph = []
    dist = [INF] * (n+2)

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    for i in range(1, n+1):
        graph.append((n+1, i, 0))
    negative_cycle = solve(n+1)

    if negative_cycle:
            print("YES")
    else:
        print("NO")
