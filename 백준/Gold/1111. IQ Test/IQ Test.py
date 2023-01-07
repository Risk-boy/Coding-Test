import sys
# sys.stdin = open("input.txt")

def find():
    global a, b
    if arr[0] == arr[1]:
        a = 1
        b = 0
        return
    else:
        a = int((arr[2] - arr[1]) / (arr[1] - arr[0]))
        b = arr[1] - a * arr[0]
        return


def solve():
    global a, b
    for i in range(n - 1):
        if a * arr[i] + b != arr[i + 1]:
            print("B")
            return
    print(a * arr[n - 1] + b)
    return


n = int(input())
arr = list(map(int, input().split()))
a = b = 0
if n == 1:
    print("A")
elif n == 2 and arr[0] == arr[1]:
    print(arr[0])
elif n == 2 and arr[0] != arr[1]:
    print("A")
else:
    find()
    solve()