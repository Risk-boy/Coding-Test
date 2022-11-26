import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# a^b % c = (a^n % c) * (a^m % c) 
def solve(a, b):
    global c

    if b == 1:
        return a % c

    temp = solve(a, b // 2)

    if b % 2 == 1:
        return (temp * temp % c) * a % c
    else:
        return temp * temp % c

a, b, c = map(int, input().split())

print(solve(a, b))