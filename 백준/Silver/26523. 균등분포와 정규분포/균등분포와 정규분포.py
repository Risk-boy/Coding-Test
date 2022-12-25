import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


'''
출제자 풀이
: 0.05 이하의 값이 180개 이상이면 A, 아니면 B
좀 더 이해가 필요한 문제이당..
'''

for _ in range(100):
    arr = [0]
    for _ in range(5000):
        arr.append(float(input()))

    arr.sort()
    for i in range(1, 5001):
        if arr[i] > 0.05:
            break
    if i <= 180:
        print("B")
    else:
        print("A")