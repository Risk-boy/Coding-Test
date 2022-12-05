import sys
# sys.stdin = open("input.txt")


def multiply(A, B):
       result = [[0] * 8 for _ in range(8)]
       for r in range(8):
           for c in range(8):
               for k in range(8):
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


d = int(input())
p = int(1e9) + 7

mat = [[0,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0],
       [0,0,1,1,0,1,0,1],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,1,0,1],
       [0,0,0,0,1,0,1,0]]

print(solve(mat, d)[0][0])