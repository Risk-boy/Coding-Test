import sys
# sys.stdin = open("input.txt")

N, L = map(int, input().split())
answer = list()

while L <= 100:
    temp = int(N - (L - 1) * L // 2)
    if temp < 0:
        break
    elif temp % L == 0:
        for i in range(temp // L, temp // L + L):
            answer.append(i)
        break
    else:
        L += 1

if len(answer) > 100 or not answer:
    print(-1)
else:
    print(*answer)