# import sys
# sys.stdin = open("input.txt")

n, k = map(int, input().split())


# 인덱스: 무게,
# 값: 해당 무게까지의 최대 가치
dp = [0] * (k+1)

for _ in range(n):
    # w: 무게, v: 가치
    w, v = map(int, input().split())
    # 최대 무게 ~ w를 포함할 수 있는 무게
    for i in range(k, w-1, -1):
        # 현재 무게를 뺀 무게의 가치 + 현재 무게의 가치가 크다면
        if dp[i] < dp[i-w] + v:
            # 최대 가치 갱신
            dp[i] = dp[i-w] + v

print(dp[k])






