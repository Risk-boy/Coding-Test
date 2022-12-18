import sys
# sys.stdin = open("input.txt")

n = int(input())
string = input()

# bigdata / security
arr = [0, 0]

i = 0
while i < len(string):
    if string[i] == "b":
        arr[0] += 1
        i += 7
    elif string[i] == "s":
        arr[1] += 1
        i += 8

if arr[0] < arr[1]:
    print("security!")
elif arr[0] > arr[1]:
    print("bigdata?")
else:
    print("bigdata? security!")

