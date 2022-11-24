import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)

    visited = [False] * (n + 1)
    visited[x] = True

    while q:
        v = q.popleft()
        if v in lier:
            return True
        for man in graph[v]:
            if not visited[man]:
                q.append(man)
                visited[man] = True
    return False
n, m = map(int, input().split())

lier = list(map(int, input().split()))
if len(lier) >= 2:
    lier = lier[1:]

    arr = []
    for _ in range(m):
        temp = list(map(int, input().split()))
        temp = temp[1:]
        arr.append(temp)
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        if len(arr[i]) >= 2:
            for j in range(len(arr[i])):
                for k in range(len(arr[i])):
                    if arr[i][j] != arr[i][k]:
                        graph[arr[i][j]].append(arr[i][k])
    cnt = 0
    for i in range(m):
        for num in arr[i]:
            if num in lier:
                cnt += 1
                break
            else:
                if bfs(num):
                    cnt += 1
                    break
    print(m - cnt)

else:
    print(m)



