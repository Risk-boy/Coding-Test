import sys
# sys.stdin = open("input.txt")

'''
A로 문자열을 초기화 시키고 맨 뒤부터 Z로 채워오다가
Z가 들어갈 수 없는 순간이 오면 최대로 들어갈 수 있는
문자열을 채우고 출력
'''
n, x = map(int, input().split())

# 문자열을 만들 수 없는 경우
if n * 26 < x or n > x:
    print("!")
    exit()

ls = ["A" for _ in range(n)]

idx = n - 1
while idx >= 0:
    if x - idx >= 26: # 맨 뒤에 Z를 넣을 수 있으면
        ls[idx] = "Z"
        idx -= 1
        x -= 26
    else:
        ls[idx] = chr(x - idx + 64)
        break

for i in range(n):
    print(ls[i], end="")


