import sys
# sys.stdin = open("input.txt")

n = int(input())

dict = {}

for _ in range(n):
    mento, mentee = input().split()
    if mento not in dict.keys():
        dict[mento] = [mentee]
    else:
        dict[mento].append(mentee)

sorted_dict = sorted(dict.items())

for i in range(len(sorted_dict)):
    for mentee in sorted(sorted_dict[i][1], reverse=True):
        print(sorted_dict[i][0], mentee)
