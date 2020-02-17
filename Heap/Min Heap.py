class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        self.heap.append(data)
        self.up(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def up(self, index):
        parent = index // 2
        if index <= 1:
            return False
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.up(parent)

    def heapsort(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.swap(0, i)
            self.down(0)
        return self.heap
    def down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] > self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.down(largest)


m = MinHeap()
m.push(43)
m.push(23)
m.push(13)
m.push(133)
m.push(63)
print(m.heapsort())
