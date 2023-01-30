import sys
# sys.stdin = open("input.txt")

x = int(input())

prefix_sum = [i for i in range(4500)]

for i in range(1, 4500):
    prefix_sum[i] += prefix_sum[i - 1]

for i in range(1, 4499):
    if x == prefix_sum[i]:
        if i % 2 == 0:
            print(f"{i}/1")
        else:
            print(f"1/{i}")
        break
    elif prefix_sum[i] < x < prefix_sum[i + 1]:
        temp = x - prefix_sum[i]
        if (i + 1) % 2 == 0:
            print(f"{temp}/{i + 2 - temp}")
        else:
            print(f"{i + 2 - temp}/{temp}")
        break
