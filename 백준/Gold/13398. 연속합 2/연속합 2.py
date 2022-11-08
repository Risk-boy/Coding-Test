# import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

dl = [0] * n    # 왼쪽부터 수의 합 구하기
dr = [0] * n    # 오른쪽부터 수의 합 구하기

for i in range(n):
    dl[i] = arr[i]
    if i == 0:
        continue
    if dl[i] < dl[i-1] + arr[i]:
        dl[i] = dl[i-1] + arr[i]

for i in range(n-1, -1, -1):
    dr[i] = arr[i]
    if i == n-1:
        continue
    if dr[i] < dr[i+1] + arr[i]:
        dr[i] = dr[i+1] + arr[i]

answer = max(dl)

for k in range(1, n-1):
    # k번째 수를 제외 한 양 사이드 더해주기
    if answer < dl[k-1] + dr[k+1]:
        answer = dl[k-1] + dr[k+1]

print(answer)