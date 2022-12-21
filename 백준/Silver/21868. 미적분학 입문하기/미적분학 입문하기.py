import sys
# sys.stdin = open("input.txt")

numerator, denominator = map(int, input().split())
a, b = map(int, input().split())
x0 = int(input())

print(a * x0 + b)
if a == 0:
    print(0, 0)
else:
    print(numerator, abs(a) * denominator)