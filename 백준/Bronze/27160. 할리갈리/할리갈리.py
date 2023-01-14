import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
fruits = {}
for _ in range(n):
    fruit, num = input().split()
    if fruit not in fruits:
        fruits[fruit] = int(num)
    else:
        fruits[fruit] += int(num)

check = False
for fruit in fruits.keys():
    if fruits[fruit] == 5:
        check = True
        break

if check:
    print("YES")
else:
    print("NO")