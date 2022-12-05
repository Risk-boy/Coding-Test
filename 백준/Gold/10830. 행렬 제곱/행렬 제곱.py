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
            result[r][c] %= 1000

    return result


def solve(mat, b):
    if b == 1:
        return mat

    temp = solve(mat, b // 2)
    if b % 2 == 1:
        return multiply(multiply(temp, temp), mat)
    else:
        return multiply(temp, temp)

n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

answer = solve(mat, b)

for ls in answer:
    for ele in ls:
        print(ele % 1000, end=" ")
    print()



