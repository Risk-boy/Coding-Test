import sys
# sys.stdin = open("input.txt")
from itertools import combinations

'''
모음: 최소 한개
자음: 최소 두개
'''
L, C = map(int, input().split())

arr = list(input().split())
mo = list()
ja = list()
# 모음
for x in arr:
    if x in "aeiou":
        mo.append(x)
    else:
        ja.append(x)


answer = list()
# 모음 개수별로
# 모음 n개 -> 자음: L - n개
for i in range(1, 6):
    if len(mo) >= i:
        if L - i >= 2 and len(ja) >= (L - i):
            mo_ls = list(combinations(mo, i))
            ja_ls = list(combinations(ja, L - i))
            for ls1 in mo_ls:
                for ls2 in ja_ls:
                    answer.append(sorted(ls1 + ls2))

answer.sort()

for code in answer:
    print("".join(code))


