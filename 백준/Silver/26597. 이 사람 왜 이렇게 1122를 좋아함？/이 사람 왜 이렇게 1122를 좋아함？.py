import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

maxNum = int(1e18)
minNum = -int(1e18)

check = False
ls = []
for i in range(1, n + 1):
    num, q = input().split()
    num = int(num)
    if q == "^":
        if minNum < num + 1:
            minNum = num + 1
    elif q == "v":
        if maxNum > num - 1:
            maxNum = num - 1
    if minNum > maxNum:
        check = True
        break
    if minNum == maxNum:
        ls.append(i)

if check:
    print("Paradox!")
    print(i)
else:
    if minNum == maxNum:
        print("I got it!")
        print(ls[0])
    else:
        print("Hmm...")
