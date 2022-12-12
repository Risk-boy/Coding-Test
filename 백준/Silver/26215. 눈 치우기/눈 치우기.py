import sys
# sys.stdin = open("input.txt")

n = int(input())
snow = list(map(int, input().split()))

snow.sort(reverse=True)

if snow[0] >= 1441:
    print(-1)
    sys.exit()
if n == 1:
    print(snow[0])
    sys.exit()

cnt = 0
while snow[0] != 0:
    if snow[1] == 0:
        snow[0] -= 1
        cnt += 1
    else:
        snow[0] -= 1
        snow[1] -= 1
        cnt += 1
        snow.sort(reverse=True)

if cnt >= 1441:
    print(-1)
else:    
    print(cnt)

