import sys
# sys.stdin = open("input.txt")

'''
k번 이상 연산할 수 없는 경우 -1 
max_num을 갱신하면서 bfs
정확히 k번 반복했을 때 최대 숫자를 찾아야하므로
deque 대신 set 사용?
'''

def solve(num):
    global m, k, answer
    q = set()
    q.add((num, 0))

    while q:
        num, cnt = q.pop()
        if cnt == k:
            if answer < num:
                answer = num
            continue
        for i in range(m - 1):
            for j in range(i + 1, m):
                if i == 0 and str(num)[j] == '0':
                    continue
                temp = str(num)
                ls = list(temp)
                ls[i], ls[j] = ls[j], ls[i]
                temp = "".join(ls)
                temp = int(temp)
                q.add((temp, cnt + 1))


n, k = map(int, input().split())
m = len(str(n))
answer = -1
solve(n)
print(answer)