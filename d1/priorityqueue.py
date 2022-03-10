'''
PriorityQueue using a fixed-length numpy array.
'''
import numpy as np
from collections import deque


class PriorityQueue:
    def __init__(self, capacity=5):
        self.queue = np.empty(capacity, np.uint8)
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def expand(self):
        self.capacity *= 2
        self.queue.resize((self.capacity,), refcheck=False)

    def insert(self, value):
        if self.is_empty():
            self.queue[0] = value
            self.size += 1
        else:
            if self.is_full(): self.expand()
            idx = self.shift_items_to_insert(value)
            self.queue[idx] = value
            self.size += 1

    def shift_items_to_insert(self, value):
        idx = self.size - 1
        while value < self.queue[idx] and idx > -1:
            self.queue[idx + 1] = self.queue[idx]
            idx -= 1
        return idx + 1
    
    def remove(self):
        if self.is_empty(): raise IndexError()
        self.size -= 1
        return self.queue[self.size]

    def __str__(self):
        lst = list(self.queue)[:self.size]
        return f'{lst}'


class QueueReverser:

    def reverse(queue, k):
        stack = deque()
        for idx in range(k):
            stack.append(queue[idx])
        for idx in range(k):
            queue[idx] = stack.pop()
        return queue


def main():
    pq = PriorityQueue()
    for x in range(1, 11):
        pq.insert(x)
    print('\n\t', pq)
    print('\n\t reversing first 3 elements, ')
    print('\t then the first 7 elements, then 10...\n ')
    QueueReverser.reverse(pq.queue, 3)
    QueueReverser.reverse(pq.queue, 7)
    QueueReverser.reverse(pq.queue, 10)
    print('\t', pq, '\n')

if __name__ == '__main__':
    main()

def main2():

    def isfull(queue):
        if queue.is_full():
            return 'yes'
        else:
            return 'no'

    print()
    q = PriorityQueue()
    q.insert(2)
    q.insert(4)
    q.insert(6)
    q.insert(3)
    q.insert(1)
    q.insert(5)
    print('\t', q)
    print('\n\t capacity: ', q.capacity)
    print('\t is the queue full? ', isfull(q)) 
    item = q.remove()
    print('\t after removing 1 item: ', q)
    print('\t removed item: ', item)
    print('\t removing the rest of the items: ')
    while not q.is_empty():
        print('\t', q.remove())
    print('\t after all items removed: ', q)
    print()


