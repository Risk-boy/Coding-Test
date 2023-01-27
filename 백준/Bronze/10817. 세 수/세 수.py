import sys
# sys.stdin = open("input.txt")

ls = list(map(int, input().split()))

ls.sort()
print(ls[1])