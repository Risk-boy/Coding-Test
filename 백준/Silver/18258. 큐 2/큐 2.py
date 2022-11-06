import sys
# sys.stdin = open('input.txt')

from collections import deque

q = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)


