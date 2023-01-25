import sys
# sys.stdin = open("input.txt")
from collections import deque

'''
뱀을 타는 경우도 고려해야함
'''
def solve(x):
    q = deque()
    q.append((x, 0))

    while q:
        cur, cnt = q.popleft()

        for i in range(1, 7):
            check = False
            next = cur + i
            if next > 100:
                continue
            # 사다리 타는 경우
            for j in range(n):
                if next == ladders[j][0]:
                    if graph[ladders[j][1]] == 0:
                        q.append((ladders[j][1], cnt + 1))
                        graph[ladders[j][1]] = cnt + 1
                    else:
                        graph[ladders[j][1]] = min(graph[ladders[j][1]], cnt + 1)
                    check = True
            # 뱀인 경우
            for k in range(m):
                if next == snakes[k][0]:
                    if graph[snakes[k][1]] == 0:
                        q.append((snakes[k][1], cnt + 1))
                        graph[snakes[k][1]] = cnt + 1
                    else:
                        graph[snakes[k][1]] = min(graph[snakes[k][1]], cnt + 1)
                    check = True
            # 사다리, 뱀 아닌 경우
            if not check:
                if graph[next] == 0:
                    q.append((next, cnt + 1))
                    graph[next] = cnt + 1
                else:
                    graph[next] = min(graph[next], cnt + 1)
    return

n, m = map(int, input().split())

ladders = [list(map(int, input().split())) for _ in range(n)]
snakes = [list(map(int, input().split())) for _ in range(m)]

graph = [0 for _ in range(101)]

solve(1)
print(graph[100])