import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline
'''
heapq 사용
'''

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[0], x[1]))
heap = []
heapq.heappush(heap, arr[0][1])
for i in range(1, n):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))