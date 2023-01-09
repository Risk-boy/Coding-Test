import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

dict = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in dict:
        dict[a] = [b]
    else:
        dict[a].append(b)

answer = 0

for key in list(dict.keys()):
    record = dict[key]
    m = len(record)
    for i in range(m):
        if i == 0 and record[i] == 0: # 첫 기록이 나온기록
            answer += 1
        if i != (m - 1): # 
            if record[i] == record[i + 1]:
                answer += 1
        if i == (m - 1) and record[i] == 1:
            answer += 1

print(answer)