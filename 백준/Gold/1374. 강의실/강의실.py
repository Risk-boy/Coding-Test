import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline

'''
11000번 문제랑 똑같다..?
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[1], x[2]))
heap = []
heapq.heappush(heap, arr[0][2])
for i in range(1, n):
    if heap[0] > arr[i][1]:
        heapq.heappush(heap, arr[i][2])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][2])

print(len(heap))