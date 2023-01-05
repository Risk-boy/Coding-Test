import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
1. 행렬이 대칭인지 확인
2. 각 행마다 적어도 두개의 0이 있는지 확인
3. visited를 이용해 소집단 구해주기
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = True    # 1, 2번 조건 맞는지 확인 용도

# 1. 대칭 확인
for i in range(n):
    for j in range(i + 1, n):
        if arr[i][j] != arr[j][i]:
            check = False
            break
    if not check:
        break

# 2. 각 행의 0 개수 확인(2개이상인지)
for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][j] == 0:
            cnt += 1
    if cnt == 1:
        check = False
        break

# 3. check 이면 소집단 나눠주기
if check:
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                graph[i + 1].append(j + 1)
    # print(graph)
    answer = []
    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(graph[i])
            for x in graph[i]:
                visited[x] = True
    print(len(answer))
    for group in answer:
        print(*group)
else:
    print(0)
