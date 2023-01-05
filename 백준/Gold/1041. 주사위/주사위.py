import sys
# sys.stdin = open("input.txt")

'''
맨위 부분과 맨위가 아닌 부분을 나눠서 구하자
1. 맨위
4개 꼭지점부분: min(1, 2, 3) * 4
모서리 중 꼭지점 제외: min(1, 2) * 4 * (n - 2) 
나머지: (n ** 2 - 4 * n + 4) * min(1)

2. 나머지 부분
4개 꼭지점 부분: min(1, 2) * 4
나머지: 4 * (n - 2) * min(1)
위 두개 * (n - 1)

# 주의 할것: 무조건 가장 작은 3개의 수 혹은 2개의 수를 찾으면 안됨!!!
주사위임!!!!
'''

n = int(input())
arr = list(map(int, input().split()))

min_one = min(arr)
min_two = 2000000
for i in range(6):
    for j in range(i + 1, 6):
        if (i + j) != 5:
            min_two = min(min_two, arr[i] + arr[j])
min_three = 3000000
three = [[0, 1, 2], [0, 1, 3], [0, 2, 4], [0, 3, 4], [1, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]
for case in three:
    temp = 0
    for idx in case:
        temp += arr[idx]
    min_three = min(min_three, temp)

if n == 1:
    arr.sort()
    print(sum(arr[:5]))
    exit()

answer = 0

# 1. 맨위
# 4개 꼭지점부분: min(1, 2, 3) * 4
answer += min_three * 4
# 모서리 중 꼭지점 제외: min(1, 2) * 4 * (n - 2)
answer += min_two * 4 * (n - 2)
# 나머지: (n ** 2 - 4 * n + 4) * min(1)
answer += min_one * (n ** 2 - 4 * n + 4)

# 2. 나머지
# 4개 꼭지점 부분: min(1, 2) * 4
answer += min_two * 4 * (n - 1)
# 나머지: 4 * (n - 2) * min(1)
answer += min_one * 4 * (n - 2) * (n - 1)

print(answer)


