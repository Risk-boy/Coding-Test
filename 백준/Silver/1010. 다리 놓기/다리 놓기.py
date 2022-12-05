import sys
# sys.stdin = open("input.txt")
import math

T = int(input())
for _ in range(T):
    n, m  = map(int, input().split())
    # mCn
    answer = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(answer)