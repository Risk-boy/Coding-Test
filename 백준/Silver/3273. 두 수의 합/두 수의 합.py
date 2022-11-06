# import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
x = int(input())    # 구해야 하는 값
arr.sort()

end = 0
cnt = 0
for start in range(n):
    two_sum = arr[start]
    end = start + 1
    while two_sum < x and end < n:
        two_sum += arr[end]
        # x랑 같다면
        if two_sum == x:
            # count
            cnt += 1
            # 더하기 전의 값으로
            two_sum -= arr[end]
            # end를 다음 칸으로
            end += 1
        elif two_sum < x:
            two_sum -= arr[end]
            end += 1
        elif two_sum > x:
            break
print(cnt)

