import sys
import heapq
# sys.stdin = open("input.txt")

v, e = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    # 시작: a, 도착: b, 비용: c
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

INF = int(1e9)

distance = [INF] * (v + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        else:
            for node in graph[now]:
                cost = dist + node[1]
                if cost < distance[node[0]]:
                    distance[node[0]] = cost
                    heapq.heappush(q, (cost, node[0]))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])