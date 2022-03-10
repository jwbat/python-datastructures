'''
PriorityQueue implemented with a Heap.
'''

from heap import Heap

class PQHeap:
    def __init__(self):
        self.heap = Heap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def is_empty(self):
        return self.heap.is_empty()
