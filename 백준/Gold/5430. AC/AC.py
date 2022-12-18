import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ac = input().rstrip()
    n = int(input())
    ls = input().rstrip()
    m = len(ls)
    ls = ls[1:m-1]
    if ls == "":
        q = deque()
    else:
        q = deque(ls.split(","))
    cnt = 0
    flag = True
    for func in ac:
        for x in func:
            if x == "R":
                cnt += 1
            elif x == "D":
                try:
                    if cnt % 2 == 0:
                        q.popleft()
                    else:
                        q.pop()
                except:
                    flag = False
    if cnt % 2 != 0:
        q.reverse()
    if flag:
        result = ",".join(q)
        print("["+result+"]")
    else:
        print("error")