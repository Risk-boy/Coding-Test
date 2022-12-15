import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())


counts = [0] * 10001
# DAT 등록
for _ in range(n):
    counts[int(input())] += 1

for i in range(1, 10001):
    if counts[i] != 0:
        for j in range(counts[i]):
            print(i)

