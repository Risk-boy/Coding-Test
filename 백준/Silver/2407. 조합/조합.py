import sys
# sys.stdin = open("input.txt")
from math import factorial

n, m = map(int, input().split())

print(factorial(n) // (factorial(n-m) * factorial(m)))
