import sys
# sys.stdin = open("input.txt")

'''
노래가 끝나는 시간: L * N + 5 * (N - 1)
'''
N, L, D = map(int, input().split())

start = L
finish = L * N + 5 * (N - 1)
answer = 0
check = False
while start <= finish:
    if check:
        break
    for x in range(start, start + 5):
        if x % D == 0:
            answer = x
            check = True
            break
    start = start + 5 + L

if check:
    print(answer)
else:
    for i in range(finish, finish + 1 + D):
        if i % D == 0:
            print(i)
            exit()
