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

n = int(input())
parent = [_ for _ in range(n + 1)]

for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

check = parent[1]

for i in range(1, n + 1):
    if check != find(i):
        print(1, i)
        break



