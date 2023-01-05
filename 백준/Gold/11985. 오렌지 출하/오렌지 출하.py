import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
dp[i] = i 번째 까지 오렌지를 담았을 때의 최소값
각각의 i에서 최대한 담을 수 있는 만큼 담아가면서 비교
'''

# 오렌지 개수 / 최대 담을 수 있는 개수 / 포장 비용
n, m, k = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(1, n + 1):
    # 상자 하나에 오렌지 하나씩만 담았을 때를 초기 값으로 설정
    dp[i] = i * k

for i in range(n):
    max_w = arr[i + 1]
    min_w = arr[i + 1]
    for j in range(1, m + 1):
        if i + j <= n:
            max_w = max(max_w, arr[i + j])
            min_w = min(min_w, arr[i + j])
            dp[i + j] = min(dp[i + j], dp[i] + k + j * (max_w - min_w))
        else:
            break
print(dp[n])