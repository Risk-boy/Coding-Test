import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
시작 시간 순으로 정렬 후
순차적으로 방문 하면서 가장 많이 배정 할 수 있게 구현
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x : (x[0], x))
cur_s  = arr[0][0]
cur_e  = arr[0][1]
answer = [(cur_s, cur_e)]

for i in range(1, n):
    nxt_s = arr[i][0]
    nxt_e = arr[i][1]
    if nxt_s < cur_e:
        if nxt_e < cur_e:
            answer.pop()
            answer.append((nxt_s, nxt_e))
            cur_s = nxt_s
            cur_e = nxt_e
    elif nxt_s >= cur_e:
        answer.append((nxt_s, nxt_e))
        cur_s = nxt_s
        cur_e = nxt_e

print(len(answer))

