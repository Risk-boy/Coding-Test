import sys
# sys.stdin = open("input.txt")

'''
각각의 선분을 기준으로 다른 선분의 양끝점을 바라 보았을 때
외적 값의 부호가 달라야함
'''

def cross(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

c1 = cross(x1, y1, x2, y2, x3, y3) * cross(x1, y1, x2, y2, x4, y4)
c2 = cross(x3, y3, x4, y4, x1, y1) * cross(x3, y3, x4, y4, x2, y2)

if c1 < 0 and c2 < 0:
    print(1)
else:
    print(0)

