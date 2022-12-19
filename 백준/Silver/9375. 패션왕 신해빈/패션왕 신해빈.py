import sys
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    n = int(input()) # 가지고 있는 의상 수
    dict = {}
    for _ in range(n):
        a, b = input().split()
        if b not in dict:
            dict.setdefault(b, 1)
        else:
            dict[b] += 1

    answer = 1
    for value in dict.values():
        answer *= (value+1)

    print(answer-1) # 전부 안입은거 제외