import sys
# sys.stdin = open("input.txt")

ls = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
n = len(word)
i = 0
cnt = 0
while i < n:
    if i + 1 < n:
        if word[i: i + 2] in ls:
            cnt += 1
            i += 2
            continue
    if i + 2 < n:
        if word[i: i + 3] in ls:
            cnt += 1
            i += 3
            continue
    cnt += 1
    i += 1

print(cnt)
