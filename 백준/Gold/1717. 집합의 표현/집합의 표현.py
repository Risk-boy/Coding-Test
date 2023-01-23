import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [_ for _ in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")