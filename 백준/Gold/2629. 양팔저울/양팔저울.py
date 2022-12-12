import sys
# sys.stdin = open("input.txt")

n = int(input()) # 30개 이하
chu = [0] + list(map(int, input().split())) # 500g 이하
T = int(input()) # 확인하고자 하는 구슬 개수
w = list(map(int, input().split())) # 확인용 구슬 무게들 40000g 이하

# dp[i][j]: i번째 까지 썼을 때 j무게 확인 여부

dp = [[False] * 15001 for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = True

for i in range(1, n+1):
    for j in range(15001):
        if dp[i-1][j] == True:
            dp[i][j] = True
            dp[i][j + chu[i]] = True
            if j - chu[i] >= 0:
                dp[i][j - chu[i]] = True
            if chu[i] - j >= 0:
                dp[i][chu[i] - j] = True


for tc in range(T):
    target = w[tc]
    if target >= 15001:
        print("N", end=" ")
        continue
    flag = False
    for i in range(n+1):
        if dp[i][target] == True:
            flag = True
    if flag:
        print("Y", end=" ")
    else:
        print("N", end=" ")



