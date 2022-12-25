import sys, math
# sys.stdin = open("input.txt")

n = int(input())
p = int(1e9) + 7
print(math.factorial(n) % p)