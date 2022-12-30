import sys
# sys.stdin = open("input.txt")

'''
dfs 접근 -> 종료조건 최초 달성 시 출력
'''
def check(): # 합이 전부 26인지 확인
    if ord(arr[0][4]) + ord(arr[1][3]) + ord(arr[2][2]) + ord(arr[3][1]) - 256 != 26: return False
    if ord(arr[0][4]) + ord(arr[1][5]) + ord(arr[2][6]) + ord(arr[3][7]) - 256 != 26: return False
    if ord(arr[1][1]) + ord(arr[1][3]) + ord(arr[1][5]) + ord(arr[1][7]) - 256 != 26: return False
    if ord(arr[1][1]) + ord(arr[2][2]) + ord(arr[3][3]) + ord(arr[4][4]) - 256 != 26: return False
    if ord(arr[1][7]) + ord(arr[2][6]) + ord(arr[3][5]) + ord(arr[4][4]) - 256 != 26: return False
    if ord(arr[3][1]) + ord(arr[3][3]) + ord(arr[3][5]) + ord(arr[3][7]) - 256 != 26: return False
    return True

def solve(idx, cnt):
    global cnt_x
    if cnt == cnt_x and check():
        for i in range(5):
            for j in range(9):
                print(arr[i][j], end="")
            print()
        sys.exit()

    for num in range(1, 13):
        if not visited[num]:
            visited[num] = True
            arr[location[idx][0]][location[idx][1]] = chr(num + 64)
            solve(idx + 1, cnt + 1)
            visited[num] = False
            arr[location[idx][0]][location[idx][1]] = "x"


arr = list()
for _ in range(5):
    arr.append(list(input()))

visited = [False] * 13 # 숫자 사용 여부
location = list() # x 좌표의 위치
cnt_x = 0 # x좌표 개수
for i in range(5):
    for j in range(9):
        if ord("A") <= ord(arr[i][j]) <= ord("L"):
            visited[ord(arr[i][j]) - 64] = True
        if arr[i][j] == "x":
            location.append([i, j])
            cnt_x += 1

solve(0, 0) # location idx, cnt

