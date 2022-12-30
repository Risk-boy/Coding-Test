import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


words = list()
while True:
    word = input().strip()
    if word == "-":
        break
    else:
        words.append(word)

cards = list()
while True:
    card = input().strip()
    if card == "#":
        break
    else:
        cards.append(card)

for card in cards:
    dict = {}
    for x in card:
        if x not in dict.keys():
            dict.setdefault(x, [1, 0]) # 단어 개수 / 쓰인 개수
        else:
            dict[x][0] += 1
    for word in words:
        for x in set(word):
            cnt_x = word.count(x)
            if x not in dict.keys() or cnt_x > dict[x][0]:
                break
        else:
            for x in set(word):
                dict[x][1] += 1

    cnt_max = 0
    cnt_min = int(1e9)
    for key in dict.keys():
        if dict[key][1] > cnt_max:
            cnt_max = dict[key][1]
        if dict[key][1] < cnt_min:
            cnt_min = dict[key][1]

    max_ls = [cnt_max]
    min_ls = [cnt_min]
    for key in dict.keys():
        if dict[key][1] == cnt_max:
            max_ls.append(key)
        if dict[key][1] == cnt_min:
            min_ls.append(key)

    for x in sorted(min_ls[1:]):
        print(x, end="")
    print(end=" ")
    print(min_ls[0], end="")
    print(end=" ")
    for x in sorted(max_ls[1:]):
        print(x, end="")
    print(end=" ")
    print(max_ls[0])
