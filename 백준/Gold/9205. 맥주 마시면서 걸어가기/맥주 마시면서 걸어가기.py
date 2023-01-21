import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

'''
시작점으로부터 순차적으로 방문해가면서 마지막 지점에 도달할 수 있는지 확인
'''
def check(cur, next):
    if abs(graph[next][0] - graph[cur][0]) + abs(graph[next][1] - graph[cur][1]) <= 1000:
        return True
    else:
        return False

def solve(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        cur = q.popleft()
        if cur == n + 1:
            return "happy"
        for next in range(n + 2):
            if not visited[next] and check(cur, next):
                visited[next] = True
                q.append(next)

    return "sad"
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n + 2)]
    visited = [False] * (n + 2)
    print(solve(0))
