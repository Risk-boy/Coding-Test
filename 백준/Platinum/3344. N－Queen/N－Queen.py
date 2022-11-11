# import sys
# sys.stdin = open("input.txt")
'''
1. If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n.
2. Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
3. If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
4. If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 1, 3).
5. Append odd list to the even list and place queens in the rows given by these numbers, from left to right (a2, b4, c6, d8, e3, f1, g7, h5).
6. For n = 8 this results in fundamental solution 1 above. A few more examples follow.

14 queens (remainder 2): 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 9, 11, 13, 5.
15 queens (remainder 3): 4, 6, 8, 10, 12, 14, 2, 5, 7, 9, 11, 13, 15, 1, 3.
20 queens (remainder 2): 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 1, 7, 9, 11, 13, 15, 17, 19, 5.
출처: 위키
'''

n = int(input())
# 8, 26, 213, 2012, 99991, 99999 중 하나

answer = []
if (n % 6 != 2) and (n % 6 != 3):
    for i in range(1, n + 1, 2):
        answer.append(i)
    for j in range(2, n + 1, 2):
        answer.append(j)

elif n % 6 == 2:
    for i in range(2, n + 1, 2):
        answer.append(i)
    odd = []
    for j in range(1, n + 1, 2):
        if j == 5:
            continue
        odd.append(j)
    # 1, 3 자리 바꾸기
    odd[0], odd[1] = odd[1], odd[0]
    # 5 추가하기
    odd.append(5)
    answer += odd

elif n % 6 == 3:
    even = []
    for i in range(4, n + 1, 2):
        even.append(i)
    even.append(2)

    odd = []
    for j in range(5, n + 1, 2):
        odd.append(j)
    odd.append(1)
    odd.append(3)
    answer = even + odd

for num in answer:
    print(num)