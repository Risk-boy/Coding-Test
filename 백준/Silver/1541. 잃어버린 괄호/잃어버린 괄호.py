import sys
# sys.stdin = open("input.txt")

'''
괄호를 여러번 사용 가능
뺄셈 기준 분할?파싱?해서 ()-()-()형태로 만들어 계산
'''

arr = input().split('-')
# print(arr)
ls = list()
for x in arr:
    y = x.split('+')

    temp = 0
    for z in y:
        temp += int(z)

    ls.append(temp)

answer = 0
for i in range(len(ls)):
    if i == 0:
        answer += ls[i]
    else:
        answer -= ls[i]
print(answer)

