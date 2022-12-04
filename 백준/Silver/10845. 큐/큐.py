import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

class Queue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]

    def back(self):
        return self.data[-1]

n = int(input())
q = Queue()

for _ in range(n):
    cmd = list(input().split())
    # push
    if cmd[0] == "push":
        q.enqueue(cmd[1])
    # pop
    elif cmd[0] == "pop":
        if not q.isEmpty():
            print(q.dequeue())
        else:
            print(-1)
    # size
    elif cmd[0] == "size":
        print(q.size())
    # empty
    elif cmd[0] == "empty":
        if q.isEmpty():
            print(1)
        else:
            print(0)
    # front
    elif cmd[0] == "front":
        if not q.isEmpty():
            print(q.front())
        else:
            print(-1)
    # back
    elif cmd[0] == "back":
        if not q.isEmpty():
            print(q.back())
        else:
            print(-1)
