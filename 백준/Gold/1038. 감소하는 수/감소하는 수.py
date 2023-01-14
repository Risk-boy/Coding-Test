import sys
# sys.stdin = open("input.txt")

def solve():
    if ls:
        result.add(int("".join(map(str, ls))))

    for i in range(10):
        if len(ls) == 0 or ls[-1] > i:
            ls.append(i)
            solve()
            ls.pop()
n = int(input())
ls = []
result = set()

solve()

result = list(result)
result.sort()

if n >= 1023:
    print(-1)
else:
    print(result[n])