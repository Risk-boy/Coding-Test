import sys
# sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# cnt의 인덱스 = 나머지
cnt = [0] * m
# 누적합 구하기
for i in range(1, n + 1):
    arr[i] += arr[i - 1]
    arr[i] %= m
    cnt[arr[i]] += 1

answer = 0
for i in range(m):
    # 나머지가 0인 경우는 자기 자신 또한 구간이 됨
    if i == 0:
        answer += cnt[i] * (cnt[i] + 1) // 2
    else:
        answer += cnt[i] * (cnt[i] - 1) // 2

print(answer)