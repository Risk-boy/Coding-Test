import sys
# sys.stdin = open("input.txt")

def multipy(A, B):
    result = [[0, 0], [0, 0]]
    for r in range(2):
        for c in range(2):
            for k in range(2):
                result[r][c] += A[r][k] * B[k][c]
            result[r][c] %= m
    return result

def fibo(n):
    if n == 1:
        return mat

    temp = fibo(n // 2)
    if n % 2 == 1:
        return multipy(multipy(temp, temp), mat)
    else:
        return multipy(temp, temp)


n = int(input())
m = 1000000007

mat = [[1, 1], [1, 0]]

print(fibo(n)[0][1])


