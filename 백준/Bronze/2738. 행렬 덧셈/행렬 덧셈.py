# import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())

arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

for _ in range(n):
    arr2.append(list(map(int, input().split())))

result = [[0] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        result[r][c] += arr1[r][c] + arr2[r][c]

for r in range(n):
    for c in range(m):
        print(result[r][c], end=" ")
    print()