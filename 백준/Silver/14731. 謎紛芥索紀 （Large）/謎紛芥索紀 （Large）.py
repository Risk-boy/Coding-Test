import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def solve(k):
    if k == 1:
        return 2

    temp = solve(k // 2)
    if k % 2 == 1:
        return (temp * temp * 2) % p
    else:
        return (temp * temp) % p

N = int(input())
p = int(1e9) + 7
answer = 0
for _ in range(N):
    c, n = map(int, input().split())
    if n == 0:
        continue
    if n == 1:
        answer += c
        continue
    answer = (answer + c * n * solve(n - 1)) % p

print(answer)