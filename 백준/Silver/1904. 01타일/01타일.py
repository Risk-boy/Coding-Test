# import sys
# sys.stdin = open("input.txt")

n = int(input())

# n이 2보다 작을 경우
if n <= 2:
    print(n)
else:
    dp = [1, 2]
    # 3번째 자리부터 시작
    idx = 2
    while idx != n:
        # n번째 수는 n-1 번째 + n-2번째
        dp.append((dp[idx-1] + dp[idx-2])%15746)
        idx += 1
    print(dp[n-1])