import sys
# sys.stdin = open("input.txt")


# 도감에 수록되어 있는 포켓몬 수 / 맞춰야 하는 문제의 개수
n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    name = input()
    dict[name] = i
    dict[str(i)] = name

for _ in range(m):
    x = input()
    print(dict[x])
