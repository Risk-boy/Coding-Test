import sys
# sys.stdin = open("input.txt")
from collections import deque

def line():
    answer = []
    q = deque()
    # 진입차수가 0인 애들 큐에 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)

        for node in graph[now]:
            # 간선 제거
            indegree[node] -= 1
            # 진입 차수가 0 이 되었다면 큐에 추가
            if indegree[node] == 0:
                q.append(node)

    for i in answer:
        print(i, end=" ")


n, m = map(int, input().split())

# 진입차수
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

line()


