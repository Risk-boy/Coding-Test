import sys
# sys.stdin = open("input.txt")

'''
전부 탐색해서 똑같으면 문자 그대로
하나라도 다르면 ?  
'''
n = int(input())
cmd = [input() for _ in range(n)]
answer = ''

if n == 1:
    print(cmd[0])
else:
    for i in range(len(cmd[0])):
        x = cmd[0][i]
        for j in range(1, n):
            if cmd[j][i] != x:
                answer += '?'
                break
        else:
            answer += x

print(answer)