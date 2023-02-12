import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

'''
임의의 한점으로부터 가장 먼 거리의 점을 찾고
그 점으로 부터 가장 먼 곳에 있는 점과의 거리
어떤분의 블로그를 참고했당
'''

def dfs(x, dist):
    for node in graph[x]:
        if distance[node[0]] == -1:
            distance[node[0]] = dist + node[1]
            dfs(node[0], dist + node[1])

n = int(input())
if n == 1:
    print(0)
    exit()
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

a = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[a] = 0
dfs(a, 0)

print(max(distance))

