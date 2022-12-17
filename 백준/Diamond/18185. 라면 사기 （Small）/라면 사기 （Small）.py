import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split())) + [0, 0]

'''
2, 3번째 라면 중 2번째 라면이 크다면 3번째 라면만큼 최소한 남겨두고
1, 2번째 라면을 먼저 구입
'''
answer = 0
for i in range(n):
    if arr[i+1] > arr[i+2]:
        cnt = min(arr[i], arr[i+1] - arr[i+2])
        answer += 5 * cnt
        arr[i] -= cnt
        arr[i+1] -= cnt
        cnt = min(arr[i], arr[i+1], arr[i+2])
        answer += 7 * cnt
        arr[i] -= cnt
        arr[i+1] -= cnt
        arr[i+2] -= cnt
    else:
        cnt = min(arr[i], arr[i+1], arr[i+2])
        answer += 7 * cnt
        arr[i] -= cnt
        arr[i+1] -= cnt
        arr[i+2] -= cnt
        cnt = min(arr[i], arr[i+1])
        answer += 5 * cnt
        arr[i] -= cnt
        arr[i+1] -= cnt

    answer += 3 * arr[i]

print(answer)
