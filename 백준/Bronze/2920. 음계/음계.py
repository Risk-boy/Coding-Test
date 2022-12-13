import sys
# sys.stdin = open("input.txt")

arr = list(map(int, input().split()))
temp1 = [i for i in range(1, 9)]
temp2 = [i for i in range(8, 0, -1)]

if arr == temp1:
    print("ascending")
elif arr == temp2:
    print("descending")
else:
    print("mixed")
