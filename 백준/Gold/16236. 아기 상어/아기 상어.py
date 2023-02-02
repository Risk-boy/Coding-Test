import sys
# sys.stdin = open("input.txt")
from collections import deque

'''
큰 물고기는 못 먹는다
작은 물고기만 먹을 수 있다
크기가 같으면 지나갈 수는 있다
거리가 최소이면서 가장 위쪽, 왼쪽 먼저 먹기
자기 크기만큼의 마리 수를 먹으면 크기가 커진다

ls라는 리스트변수를 통해 최소 거리위치의 물고기들을 저장한 후
가장 위쪽 그리고 왼쪽에 있는 곳으로 이동시키기
'''
def solve(s, e, k, m, d):

    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((s, e, k, m, d))
    visited[s][e] = True
    ls = []
    min_dist = 0
    while q:
        r, c, size, cnt, dist = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    if size < arr[nr][nc]:  # 못지나가면
                        continue
                    if size == arr[nr][nc] or arr[nr][nc] == 0: # 지나 갈 수만 있는 경우
                        q.append((nr, nc, size, cnt, dist + 1))
                        visited[nr][nc] = True
                    if size > arr[nr][nc] and arr[nr][nc]: # 먹을 수 있는 경우
                        if not ls:  # 처음 먹는 경우
                            min_dist = dist + 1
                            ls.append((nr, nc, size, cnt + 1, min_dist))
                        else:
                            if dist + 1 == min_dist:
                                ls.append((nr, nc, size, cnt + 1, min_dist))

    ls.sort(key = lambda x: (x[0], x[1]))
    if ls:
        arr[ls[0][0]][ls[0][1]] = 0
        Q.append(ls[0])
        return
    else:
        return




n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
start = end = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            start, end = i, j
            break
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
answer = 0
Q = deque()
Q.append((start, end, 2, 0, 0))

while Q:
    s, e, k, m, d = Q.popleft()
    if k == m:
        k += 1
        m = 0
    answer += d
    solve(s, e, k, m, 0)


print(answer)
