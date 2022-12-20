import sys
# sys.stdin = open("input.txt")

'''
평문 + key = 암호문 <=> 암호문 - 평문 = key
key 길이는 평문 길이의 약수여야함
가장 짧은 key 찾기
A:1, B:2 ...
'''


def check(m):
    global n
    for i in range(m, n):
        if key[i] != key[i % m]:
            return False
    return True


origin = input()
encoded = input()
n = len(origin)
key = []

for i in range(len(origin)):
    x = ord(encoded[i]) - ord(origin[i])
    if x < 1:
        x += 26
    key.append(x)

minLen = 0

for i in range(1, n + 1):
    if n % i != 0:  # 약수가 아니라면
        continue
    if not check(i): # 반복적인 형태가 나타나는지 체크
        continue
    minLen = i
    break

answer = ""
for j in range(minLen):
    answer += chr(key[j] + 64)

print(answer)