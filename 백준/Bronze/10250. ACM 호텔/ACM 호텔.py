import sys
# sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    ho = n // h
    height = n % h
    if height == 0:
        height = h
    else:
        ho += 1

    if ho < 10:
        print(f"{height}0{ho}")
    else:
        print(f"{height}{ho}")
