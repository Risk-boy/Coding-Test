import sys
# sys.stdin = open("input.txt")

'''
A의 자리수가 B보다 더 크면 안됨
A의 숫자들을 B의 자리수와 비교
'''
def solve(idx, number):
    global answer
    if number[0] == '0':
        return
    if len(number) == len(a): # 숫자를 다쓰고
        if int(number) < int(b): # b보다 작으면!
            if int(answer) < int(number):
                answer = int(number)
        return

    for j in range(len(a)):
        if not visited[j]:
            next = a[j]
            visited[j] = True
            solve(idx + 1, number + str(next))
            visited[j] = False
    return

A, b =  input().split()
a = []
for num in A:
    a.append(int(num))
visited = [False for _ in range(len(a))]
answer = -1

if len(a) > len(b):
    print(-1)
else:
    for i in range(len(a)):
        start = a[i]
        visited[i] = True
        solve(0, str(start))
        visited[i] = False
    print(answer)


