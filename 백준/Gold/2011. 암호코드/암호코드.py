import sys
# sys.stdin = open("input.txt")

'''
맨 앞자리에 0이 오거나 연속된 두자리가 0이면 해석 불가
dp[n]: n번째 까지 만들 수 있는 암호코드 개수 
'''
arr = [0] + list(map(int, input()))
n = len(arr) - 1
dp = [0] * (n + 1)
p = int(1e6)
if arr[1] == 0:
    print(0)
else:
    dp[0] = 1
    for i in range(1, n + 1):
        if i != n:
            if arr[i] == 0 and arr[i + 1] == 0:
                print(0)
                exit()
        if 0 < arr[i] < 10:
            dp[i] = (dp[i] + dp[i - 1]) % p
        if 10 <= 10 * arr[i - 1]  + arr[i] <= 26:
            dp[i] = (dp[i] + dp[i - 2]) % p

    print(dp[n])