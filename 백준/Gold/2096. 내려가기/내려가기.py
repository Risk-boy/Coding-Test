import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
dp0 = [[0, 0], [0, 0]]
dp1 = [[0, 0], [0, 0]]
dp2 = [[0, 0], [0, 0]]

# 메모리 중요!!!!!!

for i in range(n):
    a, b, c = map(int, input().rstrip().split())
    if i == 0:
        dp0[i][0] = a
        dp1[i][0] = b
        dp2[i][0] = c

        dp0[i][1] = a
        dp1[i][1] = b
        dp2[i][1] = c

    else:
        # 최대
        dp0[1][0] = a + max(dp0[0][0], dp1[0][0])
        dp1[1][0] = b + max(dp0[0][0], dp1[0][0], dp2[0][0])
        dp2[1][0] = c + max(dp1[0][0], dp2[0][0])
        # 최소
        dp0[1][1] = a + min(dp0[0][1], dp1[0][1])
        dp1[1][1] = b + min(dp0[0][1], dp1[0][1], dp2[0][1])
        dp2[1][1] = c + min(dp1[0][1], dp2[0][1])
        # 최대 갱신
        dp0[0][0] = dp0[1][0]
        dp1[0][0] = dp1[1][0]
        dp2[0][0] = dp2[1][0]
        # 최소 갱신
        dp0[0][1] = dp0[1][1]
        dp1[0][1] = dp1[1][1]
        dp2[0][1] = dp2[1][1]

# N이 1일 때!!!!!
print(max(dp0[0][0], dp1[0][0], dp2[0][0]), end=" ")
print(min(dp0[0][1], dp1[0][1], dp2[0][1]))
