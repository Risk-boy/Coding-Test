import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
        friends[x] += friends[y]
    else:
        parent[x] = y
        friends[y] += friends[x]


T = int(input())
for _ in range(T):
    n = int(input())
    dict = {0: 0}
    parent = [_ for _ in range(2 * n + 1)]
    friends = [1 for _ in range(2 * n + 1)]
    num = 1
    for _ in range(n):
        a, b = input().split()
        if a not in dict:
            dict[a] = num
            num += 1
        if b not in dict:
            dict[b] = num
            num += 1
        if find(dict[a]) != find(dict[b]):
            union(dict[a], dict[b])
            print(friends[find(dict[a])])
        else:
            print(friends[find(dict[a])])




