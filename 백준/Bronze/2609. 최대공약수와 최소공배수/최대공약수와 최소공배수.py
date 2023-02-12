import sys
# sys.stdin = open("input.txt")

x, y = map(int, input().split())

if y > x:
    x, y = y, x

a = x
b = y

r = a % b
if r == 0:
    gcd = b
    lcm = (a // b) * gcd
    print(gcd)
    print(lcm)
else:
    a = b
    b = r
    while r != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcm = (x // gcd) * (y // gcd) * gcd
    print(gcd)
    print(lcm)