import sys
# sys.stdin = open("input.txt")


'''
나와 동생의 상대적 위치의 최대 공약수를 구하면 된다
'''

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b:
        a = a % b
        a, b = b, a
    return a

# 동생 수, 나의 위치
n, s = map(int, input().split())
arr = list(map(int, input().split()))

diff = list()
for i in range(n):
    diff.append(abs(arr[i] - s))

d = diff[0]

for i in range(1, n):
    d = gcd(d, diff[i])
print(d)

