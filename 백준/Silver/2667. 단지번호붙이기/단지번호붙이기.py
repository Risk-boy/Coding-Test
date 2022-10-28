# import sys
# sys.stdin = open("input.txt")

def dfs(r, c):
    global sub_total
    # 지도를 벗어나는 경우
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    # 아직 방문하지 않은 집이라면
    if arr[r][c] == 1:
        arr[r][c] = 2   # 방문 표시
        sub_total += 1  # 집 카운트해주기
        # 상 하 좌 우 방문
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        # 연결된 곳을 전부 방문 후
        return True
    return False


n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

total = 0   # 총 단지수
houses = []
for i in range(n):
    for j in range(n):
        sub_total = 0   # 단지내 집의 수
        if dfs(i, j):
            total += 1
            houses.append(sub_total)

print(total)
houses.sort()
for house in houses:
    print(house)