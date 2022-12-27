import sys
# sys.stdin = open("input.txt")


def dfs(s):
    global cnt
    if s == x: # 제거 노드라면
        return
    if not graph[s]: # 리프 노드라면
        cnt += 1
        return
    for node in graph[s]:
        dfs(node)
        # 자식이 하나인데 그 자식이 제거 대상이라면
        if len(graph[s]) == 1 and node == x: 
            cnt += 1
        


n = int(input())    # 노드 개수
# 0번 노드부터 n-1 번 노드까지 각 노드의 부모
# -1 : 루트노드
parent = list(map(int, input().split()))
x = int(input())    # 제거할 노드

graph = [[] for _ in range(n)]
start = -1
for i in range(n):
    if parent[i] == -1:
        start = i
    else:
        graph[parent[i]].append(i)

cnt = 0
dfs(start)
print(cnt)