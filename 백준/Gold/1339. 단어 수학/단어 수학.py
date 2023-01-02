import sys
# sys.stdin = open("input.txt")

'''
단어마다 알파벳이 차지하는 자리수 저장
내림차순 정렬 후 9부터 곱해줘서 계산
ex) AAA -> {"A": 111}
'''
n = int(input())
dict = {}
for _ in range(n):
    word = input()
    m = len(word)
    for i in range(m, 0, -1):
        if word[m - i] not in dict:
            dict[word[m - i]] = 10 ** (i - 1)
        else:
            dict[word[m - i]] += 10 ** (i - 1)

answer = 0
numbers = sorted(dict.values(), reverse=True)
x = 9
for num in numbers:
    answer += num * x
    x -= 1

print(answer)



