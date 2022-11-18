import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def open(start):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    temp=deque([start])
    union=[]
    sum=0
    while temp:
        x,y=temp.pop()
        union.append([x,y])
        sum+=A[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]: continue
            if L<=abs(A[nx][ny]-A[x][y])<=R:
                temp.append([nx,ny])
                visited[nx][ny]=1
    avg=sum//len(union)
    for x,y in union:
        A[x][y]=avg
    return len(union)

day=0
while True:
    flag=1
    visited=[[0]*N for _ in range(N)]
    for  i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j]=1
                if open([i,j])>1: flag=0
    if flag: break
    else: day+=1

print(day)


