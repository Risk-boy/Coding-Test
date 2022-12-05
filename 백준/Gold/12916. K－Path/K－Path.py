import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def multiply(A, B):
    global n
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(n):
                result[r][c] += A[r][k] * B[k][c]
            result[r][c] %= p

    return result

def solve(matrix, n):
    if n == 1:
        return matrix


    temp = solve(matrix, n // 2)
    if n % 2 == 1:
        return multiply(multiply(temp, temp), matrix)
    else:
        return multiply(temp, temp)

n, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

p = int(1e9) + 7

answer = 0
for ls in solve(mat, k):
    answer += sum(ls)

print(answer % p)