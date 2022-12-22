import sys
# sys.stdin = open("input.txt")

'''
처음 풀어보는 애드혹 문제!
각 숫자들이 유일하게 가지고 있는 알파벳을 체크
Z가 있으면 0
W가 있으면 2 
U가 있으면 4
X가 있으면 6
G가 있으면 8
--- 여기까진 유일한 알파벳
O가 있으면 1
H가 있으면 3
F가 있으면 5
S가 있으면 7
I가 있으면 9 를 지워준당 
'''

T = int(input())

for tc in range(1, T + 1):
    string = input()
    dict = {}
    for i in string:
        if i not in dict:
            dict.setdefault(i, 1)
        else:
            dict[i] += 1

    answer = []

    if "Z" in dict: # ZERO 삭제
        while dict["Z"] != 0:
            for i in "ZERO":
                dict[i] -= 1
            answer.append(0)
    if "W" in dict: # TWO 삭제
        while dict["W"] != 0:
            for i in "TWO":
                dict[i] -= 1
            answer.append(2)
    if "U" in dict: # FOUR 삭제
        while dict["U"] != 0:
            for i in "FOUR":
                dict[i] -= 1
            answer.append(4)
    if "X" in dict: # SIX 삭제
        while dict["X"] != 0:
            for i in "SIX":
                dict[i] -= 1
            answer.append(6)
    if "G" in dict: # EIGHT 삭제
        while dict["G"] != 0:
            for i in "EIGHT":
                dict[i] -= 1
            answer.append(8)
    if "O" in dict: # ONE 삭제
        while dict["O"] != 0:
            for i in "ONE":
                dict[i] -= 1
            answer.append(1)
    if "H" in dict: # THREE 삭제
        while dict["H"] != 0:
            for i in "THREE":
                dict[i] -= 1
            answer.append(3)
    if "F" in dict: # FIVE 삭제
        while dict["F"] != 0:
            for i in "FIVE":
                dict[i] -= 1
            answer.append(5)
    if "S" in dict: # SEVEN 삭제
        while dict["S"] != 0:
            for i in "SEVEN":
                dict[i] -= 1
            answer.append(7)
    if "I" in dict: # NINE 삭제
        while dict["I"] != 0:
            for i in "NINE":
                dict[i] -= 1
            answer.append(9)

    answer.sort()
    phone = ''
    for i in range(len(answer)):
        phone += str(answer[i])
    print(f"Case #{tc}: {phone}")