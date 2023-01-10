import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
1번에서 출발
(1, v1, v2, n)
(1, v2, v1, n)
'''
def d(start, end):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

answer = min(d(1, v1) + d(v1, v2) + d(v2, n), d(1, v2) + d(v2, v1) + d(v1, n))

if answer < INF:
    print(answer)
else:
    print(-1)