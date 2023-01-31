import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def solve(x):
    global cnt
    visited[x] = True
    q = deque()
    for next in ls[x]: # 직접 친구
        visited[next] = True
        q.append(next)
        cnt += 1

    while q:
        cur = q.popleft()
        for next in ls[cur]: # 친구의 친구
            if not visited[next]:
                visited[next] = True
                cnt += 1


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
ls = [[] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        if graph[i][j] == "Y":
            ls[i].append(j)
            ls[j].append(i)


max_cnt = 0
for i in range(n):
    cnt = 0
    visited = [False] * n
    solve(i)
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)