import sys
# sys.stdin = open("input.txt")

n = int(input())
check = True
num = 666
cnt = 0
while check:
    if '666' in str(num):
        cnt += 1
        if n == cnt:
            check = False
            print(num)
    num += 1