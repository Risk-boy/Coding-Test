import sys
# sys.stdin = open("input.txt")
# from pprint import pprint as pp

# def dfs(r, c, check):
#     # check: 현재 가로/세로/대각선 방향 체크
#     global cnt
#     if r == n-1 and c == n-1:
#         cnt += 1
#         return
#
#     for i in range(3):
#         if dr[check][i] == 0 and dc[check][i] == 0:
#             continue
#
#         nr = r + dr[check][i]
#         nc = c + dc[check][i]
#
#         if 0 <= nr < n and 0 <= nc < n:
#             # 가로 세로 방향
#             if i == 0 or i == 1:
#                 if arr[nr][nc] != 1:
#                     dfs(nr, nc, i)
#
#             # 대각선 방향
#             elif i == 2:
#                 if arr[nr][nc] != 1 and arr[nr-1][nc] != 1 and arr[nr][nc-1] != 1:
#                     dfs(nr, nc, i)


n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 직전 위치가 가로 / 세로 / 대각선
dp = [[[0, 0, 0] for _ in range(n)]  for _ in range(n)]

dp[0][1][0] = 1 # 시작점

for r in range(n):
    for c in range(n):
        if arr[r][c] != 1:
            # 가로 방향으로 오는 경우
            if c-1 >= 0:
                dp[r][c][0] += dp[r][c-1][0]
                dp[r][c][0] += dp[r][c-1][2]
            # 세로 방향으로 오는 경우
            if r-1 >= 0:
                dp[r][c][1] += dp[r-1][c][1]
                dp[r][c][1] += dp[r-1][c][2]

            # 대각선 방향으로 오는 경우
            if r-1 >= 0 and c-1 >= 0 and arr[r-1][c] != 1 and arr[r][c-1] != 1:
                dp[r][c][2] += dp[r-1][c-1][0]
                dp[r][c][2] += dp[r-1][c-1][1]
                dp[r][c][2] += dp[r-1][c-1][2]
# pp(dp)
print(sum(dp[n-1][n-1]))


