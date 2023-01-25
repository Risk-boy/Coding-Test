import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
'''
왼쪽 서브트리를 먼저 찾아서 출력
어렵다!!
'''
def postorder(start, end):
    if start > end:
        return

    root = end + 1
    for i in range(start + 1, end + 1):
        if nums[start] < nums[i]:
            root = i
            break

    postorder(start + 1, root - 1)
    postorder(root, end)
    print(nums[start])


nums = []
check = True
while check:
    try:
        x = int(input())
        nums.append(x)
    except:
        check = False

n = len(nums)
postorder(0, n - 1)


