import sys
# sys.stdin = open("input.txt")

n = int(input())
cards = list(map(int, input().split()))
answer = 0
for i in range(n):
    if i == 0:
        answer += cards[i]
    else:
        if cards[i] == cards[i - 1] + 1:
            continue
        else:
            answer += cards[i]

print(answer)