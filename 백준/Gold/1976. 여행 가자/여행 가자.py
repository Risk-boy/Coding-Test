import sys
# sys.stdin = open("input.txt")

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ls = list(map(int, input().split()))
parent = [_ for _ in range(n + 1)]

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union(i + 1, j + 1)

for i in range(m - 1):
    if find(ls[i]) != find(ls[i + 1]):
        print("NO")
        break
else:
    print("YES")