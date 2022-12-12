import sys
# sys.stdin = open("input.txt")

n = int(input())

s = 0
for i in range(1, n + 1):
    s += 1 / i

print(n * s)
