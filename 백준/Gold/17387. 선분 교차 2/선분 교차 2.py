import sys
# sys.stdin = open("input.txt")

'''
세점이 일직선 위에 있는 경우도 생각해야함
각각의 선분을 기준으로 다른 선분의 양 끝점을 바라보았을 때
외적 곱의 부호가 0 or -1 이거나 0 and 0 이여야 하는데
0 and 0 일 경우에는 좌표의 상대적 크기 비교
'''

def cross(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a1 = (x1, y1)
a2 = (x2, y2)
a3 = (x3, y3)
a4 = (x4, y4)

c1 = cross(x1, y1, x2, y2, x3, y3) * cross(x1, y1, x2, y2, x4, y4)
c2 = cross(x3, y3, x4, y4, x1, y1) * cross(x3, y3, x4, y4, x2, y2)

if c1 < 0 and c2 < 0:
    print(1)
elif (c1 == 0 and c2 < 0) or (c1 < 0 and c2 == 0):
    print(1)
elif c1 == 0 and c2 == 0:
    if max(a1, a2) < a3 and max(a1, a2) < a4:
        print(0)
    elif max(a3, a4) < a1 and max(a3, a4) < a2:
        print(0)
    else:
        print(1)
else:
    print(0)