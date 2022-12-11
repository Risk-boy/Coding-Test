import sys
# sys.stdin = open("input.txt")


def preorder(x):
    if x == ".":
        return
    print(x, end="")
    preorder(graph[x][0])
    preorder(graph[x][1])


def inorder(x):
    if x == ".":
        return
    inorder(graph[x][0])
    print(x, end="")
    inorder(graph[x][1])

def postorder(x):
    if x == ".":
        return
    postorder(graph[x][0])
    postorder(graph[x][1])
    print(x, end="")

n = int(input())

graph = {}

for _ in range(n):
    a, b, c = input().split()
    graph[a] = [b, c]

preorder('A')
print()
inorder('A')
print()
postorder('A')

