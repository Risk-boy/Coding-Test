import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신으로 가는 단계 = 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 최소 단계 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 각 숫자의 케빈 베이컨 수 구하기
distance = [0]
for i in range(1, n + 1):
    dist = 0
    for j in range(1, n + 1):
        dist += graph[i][j]
    distance.append(dist)

# 최소 베이컨 수 구하기
minIdx = 1
for i in range(2, n + 1):
    if distance[minIdx] > distance[i]:
        minIdx = i

print(minIdx)


