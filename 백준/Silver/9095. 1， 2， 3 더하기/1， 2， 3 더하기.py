import sys, math
# sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):
    n = int(input())

    cnt = 0
    for i in range(n + 1):
        for j in range((n // 2) + 1):
            for k in range((n // 3) + 1):
                if i + 2 * j + 3 * k == n:
                    temp = math.factorial(i+j+k) // (math.factorial(i)*math.factorial(j)*math.factorial(k))
                    cnt += temp
    print(cnt)