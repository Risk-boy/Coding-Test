import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        c = len(self.data) - 1
        while c > 1:
            p = c // 2
            if self.data[c] > self.data[p]:
                self.data[c], self.data[p] = self.data[p], self.data[c]
                c = p
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxheapify(1)
        else:
            data = 0
        print(data)


    def maxheapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left

        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right

        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxheapify(smallest)

n = int(input())
heap = MaxHeap()

for _ in range(n):
    x = int(input())
    if x == 0:
        heap.remove()
    else:
        heap.insert(x)
