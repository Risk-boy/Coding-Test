# import sys
# sys.stdin = open('input.txt')

# def binsearch(list, target):
#     left = 0
#     right = len(list) - 1
#     while left <= right:
#         middle = (left + right) // 2
#         if list[middle] == target:
#             return 1
#         elif list[middle] < target:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return 0

N = int(input())    # 상근이가 가진 카드 개수
cards = list(map(int, input().split())) # 갖고 있는 숫자 카드들
M = int(input())    # 비교해야 할 대상의 개수
compare = list(map(int, input().split()))   # 비교 대상 카드들

my_dict = {}    # 각 숫자가 몇개 있는지 저장 할 공간

for num in cards:
    if num not in my_dict:
        my_dict.setdefault(num, 1)
    else:
        my_dict[num] += 1

for num in compare:
    if my_dict.get(num) == None:
        print(0, end=' ')
    else:
        print(my_dict.get(num), end=' ')


