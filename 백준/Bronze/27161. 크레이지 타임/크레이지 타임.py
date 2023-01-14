import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
check = True
start = 1
for i in range(n):
    x, time = input().split()
    time = int(time)
    if x == "HOURGLASS":
        print(start, "NO")
        if time == start:
            if check:
                start += 1
                if start > 12:
                    start = 1
            else:
                start -= 1
                if start == 0:
                    start = 12
        else:
            check = not check
            if not check:
                start -= 1
                if start == 0:
                    start = 12
            else:
                start += 1
                if start > 12:
                    start = 1
    else:
        if time == start:
            print(start, "YES")
        else:
            print(start, "NO")
        if check:
            start += 1
            if start > 12:
                start = 1
        else:
            start -= 1
            if start == 0:
                start = 12

