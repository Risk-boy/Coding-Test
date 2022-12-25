import sys
# sys.stdin = open("input.txt")

'''
협곡이든 나락이든 m이상 차이 나지 않는 용이 최소 2마리가 있어야함
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dragons = list()
for i in range(1, n + 1):
    # 고유 힘과 고유 번호 저장
    dragons.append((arr[i - 1], i))
dragons.sort(reverse=True) # 역순으로 저장
check = True
if n <= 4: # 용이 네마리 이하인 경우 모든 용이 같은 집단에 있어야함
    for i in range(n - 1):
        if dragons[i][0] - dragons[i + 1][0] > m:
            check = False
            break
    if check:
        print("YES")
        for i in range(n):
            print(dragons[i][1], end=" ")
    else:
        print("NO")

else:
    d = n - 1
    for i in range(n - 1):
        if dragons[i][0] - dragons[i + 1][0] > m:
            if i < 3: # 쎈 집단에 용이 4마리보다 적다면
                check = False
                break
            d = i
            break

    if check:
        print("YES")
        for j in range(2):
            print(dragons[j][1], end=" ")
        for k in range(d + 1, n):
            print(dragons[k][1], end=" ")
        for l in range(2, d + 1):
            print(dragons[l][1], end=" ")
    else:
        print("NO")