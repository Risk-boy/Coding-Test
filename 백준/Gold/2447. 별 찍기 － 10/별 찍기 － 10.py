import sys
# sys.stdin = open("input.txt")


def star(i, j, n):
    if (i % 3 == 1) and (j % 3 == 1):
        print(" ", end="")
        return
    elif n == 1:
        print("*", end="")
        return
    else:
        return star(i // 3, j // 3, n // 3)


n = int(input())

for i in range(n):
    for j in range(n):
        star(i, j, n)
    print()

