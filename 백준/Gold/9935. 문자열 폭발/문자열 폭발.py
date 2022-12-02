import sys
# sys.stdin = open("input.txt")

string = list(input())
bomb = list(input())
n = len(bomb)
stack = []

for a in string:
    stack.append(a)
    if a == bomb[-1] and stack[-n:] == bomb:
        del stack[-n:]

if not stack:
    print("FRULA")
else:
    print("".join(stack))