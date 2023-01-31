import sys
# sys.stdin = open("input.txt")

'''
dp[i][j]: i명 사용했을 때 합이 j인 경우가 존재하는지 true/false
어떤 분 걸 참고했는데 진짜 아직 갈길이 멀다 ㅠ
'''
n, k, x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ls = []
for i in range(n):
    ls.append(arr[i][0])

dp = [[False] * (n * x + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(min(i + 1, k), 0, -1):
        for a in range(x * j, ls[i] - 1, -1):
            dp[j][a] = (dp[j][a] or dp[j - 1][a - ls[i]])


answer = 0

for i in range(k * x + 1):
    if dp[k][i]:
        answer = max(answer, i * (k * x - i))

print(answer)


