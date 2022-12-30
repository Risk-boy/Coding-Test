import sys
# sys.stdin = open("input.txt")
from collections import deque


'''
서로 맞닿아 있는 부분 idx
1번 톱니바퀴: 2
2번 톱니바퀴: 2, 6
3번 톱니바퀴: 2, 6
4번 톱니바퀴: 6 
deque의 rotate 사용 
rotate(1): 시계 방향
rotate(-1): 반시계 방향
'''
def check_left(number, direction):
    # 범위를 벗어나거나 극이 서로 같으면 return
    if number < 1 or dict[number][2] == dict[number + 1][6]:
        return

    # 역시 먼저 체크해주고 회전
    check_left(number - 1, -direction)
    dict[number].rotate(direction)

def check_right(number, direction):
    if number > 4 or dict[number][6] == dict[number - 1][2]:
        return

    check_right(number + 1, -direction)
    dict[number].rotate(direction)
dict = {}
for i in range(1, 5):
    dict[i] = deque(list(map(int, input())))

k = int(input())
for i in range(k):
    number, direction = map(int, input().split())

    # 기준 톱니를 먼저 돌리지 말고 돌릴 수 있는 아이들을 돌려야함
    # 왼쪽 확인
    check_left(number - 1, -direction)
    # 오른쪽 확인
    check_right(number + 1, -direction)
    # 기준 톱니 회전
    dict[number].rotate(direction)


answer = 0
for i in range(1, 5):
    answer += 2 ** (i - 1) * dict[i][0]

print(answer)




