import sys
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

'''
postorder의 마지막 숫자는 root node 인 것을 이용
root 들을 순차적으로 저장
서브 postorder에서 inorder를 시행
'''

idx = [0] * (n+1)  # inorder의 숫자가 몇번째 있는지 확인용
for i in range(n):
    idx[inorder[i]] = i


def solve(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    root = postorder[post_end]
    preorder.append(root)
    left = idx[root] - in_start
    right = in_end - idx[root]

    # root 기준 좌측
    solve(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # root 기준 우측
    solve(in_end - right + 1, in_end, post_end - right, post_end - 1)


solve(0, n-1, 0, n-1)
print(*preorder)
