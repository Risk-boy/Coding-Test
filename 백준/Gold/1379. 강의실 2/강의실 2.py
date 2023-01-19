import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[1], x[2]))
heap = []
heapq.heappush(heap, (arr[0][2], arr[0][0]))
cur = 1
lecture_num = [0] * (n + 1)
lecture_num[arr[0][0]] = cur
for i in range(1, n):
    if heap[0][0] > arr[i][1]:
        heapq.heappush(heap, (arr[i][2], arr[i][0]))
        cur += 1
        lecture_num[arr[i][0]] = cur
    else:
        end, num = heapq.heappop(heap)
        heapq.heappush(heap, (arr[i][2], arr[i][0]))
        lecture_num[arr[i][0]] = lecture_num[num]

print(len(heap))
for i in range(1, n + 1):
    print(lecture_num[i])