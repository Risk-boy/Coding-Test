import sys
# sys.stdin = open("input.txt")
from collections import deque

def bfs(n, k):
    global cnt, answer
    q = deque()
    q.append((n, 0))

    flag = False

    while q:
        now, dist = q.popleft()
        # 방문 표시를 여기다가 해줘야 여러 경로 탐색 가능!!!!!
        visited[now] = True
        
        if flag and dist > answer:
            break

        if now == k:
            if not flag:
                answer = dist
                flag = True
            cnt += 1


        for new in [now-1, now+1, now*2]:
            if 0 <= new <= 100000 and not visited[new]:
                q.append((new, dist+1))

n, k = map(int, input().split())
visited = [False] * 100001
answer = 0
cnt = 0

bfs(n, k)

print(answer)
print(cnt)