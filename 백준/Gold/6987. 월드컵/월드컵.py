import sys
# sys.stdin = open("input.txt")
from itertools import combinations

'''
각 국가별 총 15개의 경기를 확인하면서
승 무 패 각각에 대하여 1씩 차감 후 
최종 경기때 승 무 패에 0이 아닌 숫자가 있으면 불가능
'''

def solve(cnt):
    global result
    if cnt == 15: # 15 경기 모두 마침
        for x in res:
            if sum(x) > 0:
                break
        else:
            result = 1
        return

    c1, c2 = country[cnt]
    for r1, r2 in [(0, 2), (1, 1), (2, 0)]:
        if res[c1][r1] > 0 and res[c2][r2] > 0:
            res[c1][r1] -= 1
            res[c2][r2] -= 1
            solve(cnt + 1)
            res[c1][r1] += 1
            res[c2][r2] += 1
    return

country = list(combinations(range(6), 2))
answer = []
for _ in range(4):
    arr = list(map(int, input().split()))
    res = []
    for i in range(0, 16, 3):
        res.append(arr[i:i + 3])
    result = 0
    solve(0)
    answer.append(result)

print(*answer)