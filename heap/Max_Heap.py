class MaxHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, arr):
        self.heap = arr
        n = len(self.heap)

        # start from last non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def remove(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


x = MaxHeap()

x.build_heap([10, 20, 5, 6, 1, 8])
print(x.heap)  # max heap

x.insert(30)
print(x.heap)

print(x.remove())  # removes max
print(x.heap)




