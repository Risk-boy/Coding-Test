import sys
# sys.stdin = open("input.txt")

'''
최악의 경우 abs(n - 100)만큼 이동해야함
0부터 abs(n - 100) + n - 1까지 탐색하면서 최소값 갱신
'''

n = int(input()) # 가고자 하는 채널
m = int(input()) # 고장난 버튼 개수
if m >= 1:
    broken = list(input().split())
else:
    broken = list()

ans = abs(n - 100)
for i in range(ans + n):
    for num in str(i):
        if num in broken:
            break
    else:
        ans = min(ans, abs(n - i) + len(str(i)))

print(ans)

