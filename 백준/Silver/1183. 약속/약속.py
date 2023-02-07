import sys
# sys.stdin = open("input.txt")

n = int(input())

ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append(b - a)

ls.sort()
m = len(ls)
if m % 2 == 1:
    print(1)
else:
    print(ls[m // 2] - ls[m // 2 - 1] + 1)
