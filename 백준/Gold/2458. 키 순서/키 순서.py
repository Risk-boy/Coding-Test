import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)


graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 두 친구 사이의 거리를 1로 설정
    graph[a][b] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 키가 몇 번째 인지 알 수 있는 학생 수
cnt = 0
for i in range(1, n + 1):
    flag = True
    for j in range(1, n + 1):
        if i != j:
            # 서로 거리가 1e9라면 키를 비교 못함
            if graph[i][j] == graph[j][i]:
                flag = False
    if flag:
        cnt += 1

print(cnt)
