import sys
# sys.stdin = open("input.txt")

'''
1번 200~209: 8개
2번 200~219: 4개
3번 200~229: 2개
4번 태풍: 1개

200 <= n <= 239
여러개의 답이 있는 경우 아래쪽의 비약 선택
'''

n = int(input())
if n <= 205: # 2번 선택시 최대 209 -> 1번 선택
    print(1)
elif 206 <= n <= 217: # 2번
    print(2)
elif 218 <= n <= 228: # 3번
    print(3)
else:
    print(4)