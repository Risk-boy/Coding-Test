import sys, math
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    n = int(math.sqrt(distance))
    check = n ** 2
    answer = 0
    if distance < 4:
        answer = distance
        print(answer)
    else:
        if distance == check:
            answer = 2 * n - 1
        elif check < distance <= n + check:
            answer = 2 * n
        else:
            answer = 2 * n + 1
        print(answer)