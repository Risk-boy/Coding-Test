import sys
# sys.stdin = open("input.txt")


def solve(x, first, second):
    global answer
    if visited[arr[x]]:
        if sorted(first) == sorted(second):
            answer += first
        return
    visited[arr[x]] = True
    solve(arr[x], first + [arr[x]], second + [arr[arr[x]]])

    return

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    solve(i, [i], [arr[i]])

answer = sorted(list(set(answer)))
print(len(answer))
for x in answer:
    print(x)