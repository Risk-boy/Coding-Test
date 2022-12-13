import sys
# sys.stdin = open("input.txt")
from collections import deque


def solve(n, k):
    q = deque()
    q.append((n, 0))
    visited[n] = True
    distance[n] = 0

    while q:
        now, dist = q.popleft()
        if now == k:
            return

        for i in range(3):

            if i == 0: # -1 이동
                new = now - 1
                if 0 <= new <= 200000:
                    if not visited[new]:
                        visited[new] = True
                        if new % 2 == 0 and new-1 >= 0:
                            minD = min(dist+1, distance[new-1]+1, distance[new//2])
                            distance[new] = minD
                            q.append((new, minD))
                        elif new-1 >= 0:
                            minD = min(dist+1, distance[new-1]+1)
                            distance[new] = minD
                            q.append((new, minD))
                        else:
                            distance[new] = dist + 1
                            q.append((new, dist + 1))

            elif i == 1: # +1 이동
                new = now + 1
                if 0 <= new <= 200000:
                    if not visited[new]:
                        visited[new] = True
                        if new % 2 == 0 and new - 1 >= 0:
                            minD = min(dist + 1, distance[new + 1] + 1, distance[new // 2])
                            distance[new] = minD
                            q.append((new, minD))
                        elif new - 1 >= 0:
                            minD = min(dist + 1, distance[new + 1] + 1)
                            distance[new] = minD
                            q.append((new, minD))
                        else:
                            distance[new] = dist + 1
                            q.append((new, dist + 1))

            else: # *2 이동
                new = now * 2
                if 0 <= new <= 200000:
                    if not visited[new]:
                        visited[new] = True
                        distance[new] = dist
                        q.append((new, dist))



n, k = map(int, input().split())

distance = [100001] * 200001
visited = [False] * 200001

solve(n, k)

print(distance[k])
