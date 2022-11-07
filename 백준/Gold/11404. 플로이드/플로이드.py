import sys
# sys.stdin = open("input.txt")

n = int(input()) # 도시
m = int(input()) # 버스

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    # a에서 b로 가는데 c만큼 비용
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    else:
        if graph[a][b] > c:
            graph[a][b] = c

# 자기 자신은 비용 0 처리
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

# 플루이드 워셜 알고리즘 
# dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()