import sys
# sys.stdin = open("input.txt")

'''
각 숫자를 index로 하는 visited 배열 만들기
two pointers 를 이용해 전진
'''
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * 100001
answer = 0
end = 0

for start in range(n):
    while end < n:
        if not visited[arr[end]]:
            visited[arr[end]] = True
            end += 1
        else:
            break
    answer += (end - start)
    visited[arr[start]] = False

print(answer)
