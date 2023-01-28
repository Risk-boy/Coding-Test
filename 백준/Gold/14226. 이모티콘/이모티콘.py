import sys
# sys.stdin = open("input.txt")
from collections import deque

def solve(start):
    q = deque()
    q.append((start, 0, 0))    # 화면에 있는 개수 / 클립보드에 있는 개수 / 시간
    visited[start][0] = True

    while q:
        cur, clip, time = q.popleft()
        if cur == n:
            return time

        # 화면에 있는 거 삭제
        next = cur - 1
        if 1 < next <= n + 1:
            if not visited[next][clip]:
                q.append((next, clip, time + 1))
                visited[next][clip] = True
        # 클립보드에 있는 거 바로 붙여넣기
        next = cur + clip
        if next <= n + 1:
            if not visited[next][clip]:
                q.append((next, clip, time + 1))
                visited[next][clip] = True
        # 화면꺼 복사해서 클립에 붙여넣기
        clip = cur
        if not visited[cur][clip]:
            q.append((cur, clip, time + 1))
            visited[cur][clip] = True

    return

n = int(input())

visited = [[False] * (n + 2) for _ in range(n + 2)]
answer = solve(1)

print(answer)