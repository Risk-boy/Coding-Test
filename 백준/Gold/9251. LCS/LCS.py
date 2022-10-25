# import sys
# sys.stdin = open("input.txt")

str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

# 해당 index가 포함된 공통 부분의 최대 길이 저장
dp = [0] * m

# 첫번째 문자열 기준
for i in range(n):
    # 공통 부분 길이 측정 변수
    cnt = 0
    for j in range(m):
        # 현재까지 공통부분 중 가장 긴 것 찾기
        if cnt < dp[j]:
            cnt = dp[j]
        # 공통부분이 더 있을 경우 최대 길이 늘리기
        elif str1[i] == str2[j]:
            dp[j] = cnt + 1

print(max(dp))

