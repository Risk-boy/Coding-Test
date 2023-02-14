import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    x, y = map(int, input().split())
    ls.append((x, y))

ls.sort(key=lambda x: (x[1], x[0]))

for point in ls:
    print(*point)