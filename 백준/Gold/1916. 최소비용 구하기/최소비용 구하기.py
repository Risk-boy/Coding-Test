import sys
import heapq
# sys.stdin = open("input.txt")

n = int(input())    # 도시 개수
m = int(input())    # 버스 개수

graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):
    # a: 출발, b: 도착, c: 비용
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    # 비용을 앞에 써준다! (비용에 따른 최소힙을 이용하기 위해서)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        else:
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for node in graph[now]:
                cost = dist + node[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[node[0]]:
                    distance[node[0]] = cost
                    heapq.heappush(q, (cost, node[0]))

dijkstra(start)

print(distance[end])

