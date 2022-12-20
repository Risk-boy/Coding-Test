import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
임의의 좌표 x에서 출발하였을 때
어떤 i에 대하여 Xi - Ti = x 가 성립해야 은행 방문 가능 
'''

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dict = {}

for i in range(n):
    x = arr[i][0] - arr[i][1]
    if x not in dict:
        dict.setdefault(x, arr[i][2])
    else:
        dict[x] += arr[i][2]

print(max(dict.values()))
