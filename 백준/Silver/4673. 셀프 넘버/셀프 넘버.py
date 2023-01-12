import sys
# sys.stdin = open("input.txt")

def solve(n):
    if n > 10000:
        return
    next = n
    x = n % 10
    next += x
    n = n // 10
    while n:
        x = n % 10
        next += x
        n = n // 10
    if next <= 10000:
        visited[next] = True
        solve(next)
    return

visited = [False] * 10001

for i in range(1, 10001):
    if not visited[i]:
        solve(i)

for i in range(1, 10001):
    if not visited[i]:
        print(i)
