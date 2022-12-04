import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x += [x[0]]
y += [y[0]]

# 외적 sum(x1y2 - x2y1)
cross = 0
for i in range(n):
    cross += (x[i]*y[i+1] - x[i+1]*y[i])

answer = round(abs(cross) / 2, 1)
print(answer)