import sys
# sys.stdin = open("input.txt")

check = True
T = 1
while check:
    n = int(input())
    if n == 0:
        check = False
    names = {}
    for i in range(1, n + 1):
        name = input()
        names[i] = [name, 0]
    for _ in range(2 * n - 1):
        num, x = input().split()
        num = int(num)
        if names[num][1] == 0:
            names[num][1] += 1
        else:
            names[num][1] = 0
    for value in list(names.values()):
        if value[1] == 1:
            print(T, value[0])
    T += 1