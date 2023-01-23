import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
for i in range(1, T + 1):
    n = int(input())
    parent = [_ for _ in range(n)]
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    print(f"Scenario {i}:")
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()

