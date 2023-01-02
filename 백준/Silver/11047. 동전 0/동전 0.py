import sys
# sys.stdin = open("input.txt")

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.reverse()

answer = 0
for coin in coins:
    cnt = k // coin
    if cnt > 0:
        answer += cnt
        k = k % coin

print(answer)