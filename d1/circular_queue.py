'''
Queue implementation using a circular numpy array.
'''

import numpy as np
from stack import Stack


class QueueNP:
    def __init__(self, capacity=3):
        self.array = np.empty(capacity, dtype=np.uint8)
        self.length = capacity
        self.count = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.length

    def peek(self):
        return self.array[self.front]

    def increment_front(self):
        self.front = (self.front + 1) % self.length

    def increment_rear(self):
        self.rear = (self.rear + 1) % self.length
        
    def enqueue(self, item):
        self.array[self.rear] = item
        self.increment_rear()
        if self.is_full():
            self.increment_front()
        else:
            self.count += 1

    def dequeue(self):
        if self.is_empty(): raise IndexError()
        item =  self.array[self.front]
        self.array[self.front] = 0
        self.increment_front()
        self.count -= 1
        return item

    def reverse(self):
        stack = Stack()

        while not self.is_empty():
            stack.push(self.dequeue())

        while not stack.is_empty():
            self.enqueue(stack.pop())

    def __str__(self):
        lst = list(self.array)
        front, length  = self.front, self.length
        ans = []
        for _ in range(self.count):
            ans.append(lst[front])
            front = (front + 1) % length
        return f'{ans}'



def main():
    def prnq(q):
        print('\n\t q: ', q)

    def prndq(q):
        print('\n\t dequeue: ', q.dequeue())

    q = QueueNP()
    for x in range(1, 5):
        q.enqueue(x)
        prnq(q)
    
    prndq(q)
    prnq(q)
    print()
    quit()

    for y in range(55, 66):
        q.enqueue(y)
        print('\t q.enqueue', y, ':  ', q)
        print('\t dequeue: ', q.dequeue(), ':  ', q)

main()


