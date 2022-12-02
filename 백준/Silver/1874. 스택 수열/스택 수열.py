import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
stack = [0]
answer = []
start = 1
for _ in range(n):
    x = int(input())
    # x보다 같거나 작을 때 까지 push
    while stack[-1] < x:
        stack.append(start)
        answer.append("+")
        start += 1
    # x와 같다면 pop해주기
    if stack[-1] == x:
        stack.pop()
        answer.append("-")
    # 최상단 수가 x 보다 크면 no
    elif stack[-1] > x:
        answer = ["NO"]
        break

for x in answer:
    print(x)