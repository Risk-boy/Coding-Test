import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    ls = list(input().split())
    if ls[0] == "push_front":
        q.appendleft(ls[1])
    elif ls[0] == "push_back":
        q.append(ls[1])
    elif ls[0] == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif ls[0] == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif ls[0] == "size":
        print(len(q))
    elif ls[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif ls[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif ls[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
