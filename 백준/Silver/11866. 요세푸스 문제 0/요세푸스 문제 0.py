import sys
# sys.stdin = open("input.txt")

n, k = map(int, input().split())
ls = []
for i in range(1, n + 1):
    ls.append(i)
answer = []
cur = k - 1
while ls:
    answer.append(ls.pop(cur))
    n -= 1
    if n == 0:
        break
    next = cur % n
    cur = (next + k - 1) % n

print("<", end="")
n = len(answer)
for i in range(n):
    if i != (n - 1):
        print(f"{answer[i]},", end=" ")
    else:
        print(f"{answer[i]}>")