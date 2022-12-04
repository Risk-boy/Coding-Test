import sys
# sys.stdin = open("input.txt")

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 외적
D = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

# 일직선
if D == 0:
    print(0)
# 반시계
elif D > 0:
    print(1)
# 시계
else:
    print(-1)


