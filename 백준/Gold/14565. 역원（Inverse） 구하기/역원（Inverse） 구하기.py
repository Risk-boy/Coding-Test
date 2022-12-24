import sys
# sys.stdin = open("input.txt")

n, a = map(int, input().split())

additive_inverse = n - a

try:
    pow(a, -1, n)
    multiplicative_inverse = pow(a, -1, n)
except:
    multiplicative_inverse = -1

print(additive_inverse, multiplicative_inverse)