import sys
# sys.stdin = open("input.txt")

n, b, c = map(int, input().split())
arr = list(map(int, input().split())) + [0, 0]

'''
b <= c 일 경우 하나씩 구매
'''
answer = 0
if b <= c:
    print(b * sum(arr))
else:
    for i in range(n):
        if arr[i+1] > arr[i+2]:
            cnt = min(arr[i], arr[i+1] - arr[i+2])
            answer += (b+c) * cnt
            arr[i] -= cnt
            arr[i+1] -= cnt
            cnt = min(arr[i], arr[i+1], arr[i+2])
            answer += (b + 2*c) * cnt
            arr[i] -= cnt
            arr[i+1] -= cnt
            arr[i+2] -= cnt
        else:
            cnt = min(arr[i], arr[i+1], arr[i+2])
            answer += (b + 2*c) * cnt
            arr[i] -= cnt
            arr[i+1] -= cnt
            arr[i+2] -= cnt
            cnt = min(arr[i], arr[i+1])
            answer += (b+c) * cnt
            arr[i] -= cnt
            arr[i+1] -= cnt

        answer += b * arr[i]

    print(answer)
