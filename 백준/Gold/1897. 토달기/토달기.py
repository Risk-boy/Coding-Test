import sys
# sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline


def bfs():
    global start, maxCnt
    q = deque()
    q.append((start, 3))
    visited[dict[start]] = True
    while q:
        word, length = q.popleft()
        if length > maxCnt:
            maxCnt = length
        if (length + 1) > max(words.keys()):
            continue
        if length + 1 in words:
            for x in words[length + 1]:
                if not visited[dict[x]]:
                    for i in range(length + 1):
                        if x[:i] + x[i + 1:] == word:
                            visited[dict[x]] = True
                            q.append((x, length + 1))


n, start = input().strip().split()
words = {}  # 길이별 단어 목록
dict = {}   # 단어별 고유 번호
visited = [False] * int(n) # 고유번호에 따른 방문 유무
for i in range(int(n)):
    word = input().strip()
    if len(word) not in words:
        words.setdefault(len(word), [word])
    else:
        words[len(word)].append(word)
    if word not in dict:
        dict.setdefault(word, i)



maxCnt = 3
bfs()

check = True
while check:
    if maxCnt in words:
        for x in words[maxCnt]:
            if visited[dict[x]]:
                print(x)
                check = False
                break
    maxCnt -= 1
