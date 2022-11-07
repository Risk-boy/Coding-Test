import sys
import heapq
# sys.stdin = open("input.txt")

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0
    while q:
        dist, now, path = heapq.heappop(q)
        if now == end:
            print(distance[end])
            print(len(path))
            print(*path)
            return
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0], path + [node[0]]))


n = int(input())    # 도시
m = int(input())    # 버스

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # a에서 b로가는데 c비용
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())
INF = int(1e9)
distance = [INF] * (n + 1)

dijkstra(start, end)



