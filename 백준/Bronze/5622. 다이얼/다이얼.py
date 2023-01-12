import sys
# sys.stdin = open("input.txt")

phone = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

num = input()
answer = 0
for x in num:
    for i in range(len(phone)):
        if x in phone[i]:
            answer += (i + 3)
            break
print(answer)