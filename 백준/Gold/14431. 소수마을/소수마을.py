import sys, math, heapq
# sys.stdin = open("input.txt")

'''
에라토스테네스 체로 소수 리스트 만들기
각 마을 간 거리 체크 -> 거리가 소수이면 인접리스트에 추가
다익스트라 알고리즘을 통해 최단거리 구하기
'''

def get_distance(x1, y1, x2, y2):
    return int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 소수 마을 위치 / A 마을 위치
x1, y1, x2, y2 = map(int, input().split())

n = int(input())
graph = [[] for _ in range(n + 2)]
town = [] # 마을 좌표 정보

# 에라토스테네스 체 구현
# 좌표의 정보가 절대값이 3000이하인 정수이므로 최대거리 = sqrt(2 * 6000**2) = 8485...
prime = [True for _ in range(8500)]
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(8500)) + 1):
    if prime[i]:
        j = 2
        while i * j < 8500:
            prime[i * j] = False
            j += 1

# 두 마을 사이의 거리 정보 저장
town.append((x1, y1))
town.append((x2, y2))

for _ in range(n):
    x, y = map(int, input().split())
    town.append((x, y))

for i in range(n + 2):
    for j in range(i + 1, n + 2):
        dist = get_distance(town[i][0], town[i][1], town[j][0], town[j][1])
        if prime[dist]: # 두 마을 사이의 거리가 소수이면 추가
            graph[i].append((j, dist))
            graph[j].append((i, dist))

# 다익스트라
distance = [int(1e9) for _ in range(n + 2)]
dijkstra(0)

if distance[1] != int(1e9):
    print(distance[1])
else:
    print(-1)