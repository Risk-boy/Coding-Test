import sys
# sys.stdin = open("input.txt")

n = int(input())
visited = [[False] * 100 for _ in range(100)]
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if not visited[a + i][b + j]:
                answer += 1
                visited[a + i][b + j] = True

print(answer)