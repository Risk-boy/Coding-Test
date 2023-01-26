import sys, heapq
# sys.stdin= open("input.txt")
input = sys.stdin.readline

def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        if distance[cur] < dist:
            continue

        for next in graph[cur]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [INF] * (n + 1)
solve(1)
print(distance[n])