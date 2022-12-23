import sys
# sys.stdin = open("input.txt")

n = int(input())
dict = {}
for _ in range(n):
    s, x = input().split()
    if s not in dict:
        dict.setdefault(s, int(x))
    else:
        dict[s] += int(x)

check = False
ls = list(dict.keys())
for i in range(len(ls) - 1):
    for j in range(i + 1, len(ls)):
        if dict[ls[i]] == int(dict[ls[j]] * 1.618) or dict[ls[j]] == int(dict[ls[i]] * 1.618):
            check = True

if check:
    print("Delicious!")
else:
    print("Not Delicious...")