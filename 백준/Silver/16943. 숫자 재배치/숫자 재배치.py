import sys
# sys.stdin = open("input.txt")
from copy import deepcopy

'''
A의 자리수가 B보다 더 크면 안됨
A의 숫자들을 B의 자리수와 비교
'''
def solve(x, idx, number):
    global answer
    if idx == 0 and x == 0:
        return

    if len(number) == len(a): # 숫자를 다쓰고
        if int(number) < int(b): # b보다 작으면!
            print(number)
            exit()
        else:
            return

    for j in range(len(temp)):
        next = temp[j]
        temp.remove(next)
        temp.sort(reverse=True)
        solve(next, idx + 1, number + str(next))
        temp.append(next)
        temp.sort(reverse=True)
    return

A, b =  input().split()
a = []

for num in A:
    a.append(int(num))

a.sort(reverse=True)
if len(a) > len(b):
    print(-1)
else:
    answer = ''
    for i in range(len(a)):
        start = a[i]
        temp = deepcopy(a)
        temp.remove(start)
        temp.sort(reverse=True)
        solve(a[i], 0, str(start))
    else:
        print(-1)


