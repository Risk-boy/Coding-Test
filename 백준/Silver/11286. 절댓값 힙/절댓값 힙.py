import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

class AbsHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        c = len(self.data) - 1
        while c > 1:
            p = c // 2
            # 절대값이 작으면 무조건 위로
            if abs(self.data[c]) < abs(self.data[p]):
                self.data[c], self.data[p] = self.data[p], self.data[c]
                c = p
            # 절대값이 같지만 부호가 다르면 음수를 위로
            elif abs(self.data[c]) == abs(self.data[p]) and self.data[c] < self.data[p]:
                self.data[c], self.data[p] = self.data[p], self.data[c]
                c = p
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.absheapify(1)
        else:
            data = 0
        print(data)

    def absheapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if left < len(self.data):
            if abs(self.data[left]) < abs(self.data[largest]):
                largest = left
            elif abs(self.data[left]) == abs(self.data[largest]) and self.data[left] < self.data[largest]:
                largest = left
        if right < len(self.data):
            if abs(self.data[right]) < abs(self.data[largest]):
                largest = right
            elif abs(self.data[right]) == abs(self.data[largest]) and self.data[right] < self.data[largest]:
                largest = right
        if largest != i:
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            self.absheapify(largest)

n = int(input())
heap = AbsHeap()
for _ in range(n):
    x = int(input())
    if x == 0:
        heap.remove()
    else:
        heap.insert(x)