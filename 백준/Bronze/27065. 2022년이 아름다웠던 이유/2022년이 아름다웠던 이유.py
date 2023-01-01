import sys
# sys.stdin = open("input.txt")

def solve(x): # 과잉수
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    if sum > x:
        return True

T = int(input())
for _ in range(T):
    n = int(input())
    if solve(n): # 과잉수 이면서
        for i in range(1, n):
            if n % i == 0: # 약수가
                if solve(i): # 과잉수 이면
                    print("BOJ 2022")
                    break
        else:
            print("Good Bye")
    else:
        print("BOJ 2022")