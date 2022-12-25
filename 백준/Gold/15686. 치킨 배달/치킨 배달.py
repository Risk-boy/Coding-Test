import sys
# sys.stdin = open("input.txt")
from itertools import combinations

'''
각각의 치킨집으로부터 모든 집까지 거리 구하기
정렬 후 앞에 m개의 거리만 합산
'''

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

house = []
chicken = []

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            house.append((r, c))
        elif arr[r][c] == 2:
            chicken.append((r, c))

distance = [[] for _ in range(len(house))]
for i in range(len(house)):
    dist = 0
    for chick in chicken:
        dist = (abs(chick[0] - house[i][0]) + abs(chick[1] - house[i][1]))
        distance[i].append(dist)

ls = [i for i in range(len(chicken))]
# distance[i][j] = i 번째 집에서 j 번째 치킨 집 까지 거리
distMin = int(1e9)
combination = list(combinations(ls, m))

for comb in combination:
    dist = 0
    for i in range(len(distance)):
        temp = int(1e9)
        for x in comb:
            temp = min(distance[i][x], temp)
        dist += temp
    if dist < distMin:
        distMin = dist

print(distMin)
