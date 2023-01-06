import sys
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    dict = {}
    check = True
    i = 1
    while check:
        x = (a ** i) % 10
        if x == 0:
            x = 10
        if x not in dict.values():
            dict[i] = x
        else:
            check = False
        i += 1
    c = len(dict.keys())

    print(dict[list(dict.keys())[(b % c) - 1]])

