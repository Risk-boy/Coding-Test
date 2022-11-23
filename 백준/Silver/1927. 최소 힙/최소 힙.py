import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        c = len(self.data) - 1
        while c > 1:
            p = c // 2
            if self.data[c] < self.data[p]:
                self.data[c], self.data[p] = self.data[p], self.data[c]
                c = p
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.minheapify(1)
        else:
            data = 0
        print(data)

    def minheapify(self, i):
        left = i * 2
        right = i * 2 + 1
        largest = i
        if left < len(self.data) and self.data[left] < self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] < self.data[largest]:
            largest = right
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.minheapify(largest)

n = int(input())
heap = MinHeap()
for _ in range(n):
    x = int(input())
    if x == 0:
        heap.remove()
    else:
        heap.insert(x)