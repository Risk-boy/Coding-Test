import sys
# sys.stdin = open("input.txt")

n = int(input())
ls = list()
for i in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))


answer = [0] * n
for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if ls[j][0] > ls[i][0] and ls[j][1] > ls[i][1]:
                cnt += 1
    answer[i] = cnt

print(*answer)
