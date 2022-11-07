import sys
# sys.stdin = open("input.txt")
import heapq

# n: 학생 수 / m: 도로 수 / x: 파티 열리는 곳
n, m, x = map(int, sys.stdin.readline().split())
# 1 <= x <= n
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # a에서 b로 c시간
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 비용, 노드 순서로
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리한 곳이라면
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

# 갔다가 다시 와야됨
# dijkstra(start) + dijkstra(x)

INF = int(1e9)

# x에서 출발하는 배열은 따로 만들기
distance_x = [INF] * (n + 1)
# 각각의 학생이 x로 가는데 걸리는 최소시간 저장
time = [0] * (n + 1)
for start in range(1, n + 1):
    # 매번 초기화
    distance = [INF] * (n + 1)
    # 출발 장소가 파티장소라면
    if start == x:
        distance_x = distance
    dijkstra(start)
    # 최소시간 갱신
    time[start] = distance[x]

# 돌아오는 시간 더해주기
for i in range(1, n + 1):
    time[i] += distance_x[i]

print(max(time))


