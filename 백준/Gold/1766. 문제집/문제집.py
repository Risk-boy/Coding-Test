import sys, heapq
# sys.stdin = open("input.txt")

def topology():
    heap = []
    answer = []

    # 진입차수 0인 문제 먼저 넣기(먼저 풀어야하는)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heap.append(i)
    while heap:
        now = heapq.heappop(heap)
        answer.append(now)

        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                heapq.heappush(heap, node)

    for i in answer:
        print(i, end = " ")

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology()
