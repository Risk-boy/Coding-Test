import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n + 1)
# tree의 index의 마지막 비트 = 저장 할 값의 개수
tree = [0] * (n + 1)

# tree에 반영해주는 함수
def update(i, diff):
    while i <= n:
        tree[i] += diff
        # 0이 아닌 마지막 비트 더해주기
        i += (i & -i)

# 누적합 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        # 맨 뒤부터 앞으로 이동
        result += tree[i]
        i -= (i & -i)
    return result

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    # tree에 바로 반영
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    # update인 경우
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    # 구간합 구하기인 경우
    else:
        print(prefix_sum(c) - prefix_sum(b - 1))