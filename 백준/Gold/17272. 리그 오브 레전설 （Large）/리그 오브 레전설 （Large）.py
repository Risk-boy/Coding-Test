import sys
# sys.stdin = open("input.txt")


def multiply(A, B):
    global m
    result = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            for k in range(m):
                result[r][c] += A[r][k] * B[k][c]
            result[r][c] %= p
    return result

def solve(matrix, d):
    if d == 1:
        return matrix

    temp = solve(matrix, d // 2)
    if d % 2 == 1:
        return multiply(multiply(temp, temp), matrix)
    else:
        return multiply(temp, temp)


n, m = map(int, input().split())

if n == m:
    print(2)
    sys.exit()
if n < m:
    print(1)
    sys.exit()

mat = []
# 점화식행렬 만들기
for i in range(m):
    if i == 0:
        mat.append([1] + list(0 for _ in range(m-2)) +[1])
    else:
        temp = [0] * m
        temp[i-1] = 1
        mat.append(temp)

# 몇번 행렬식 곱할건지
N = n - m + 1
# 0 부터 m-1 까지는 조합수가 1
base = [1] * m
p = int(1e9) + 7

print(sum(solve(mat, N)[0]) % p)

