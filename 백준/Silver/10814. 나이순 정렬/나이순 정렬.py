import sys
# sys.stdin = open("input.txt")

n = int(input())

ls = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    ls.append([age, name])

ls.sort(key = lambda x: x[0])

for x in ls:
    print(*x)