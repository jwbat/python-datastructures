'''
Queue implemented with deque
'''

from collections import deque
from stack import Stack

class Queue:
    def __init__(self):
        self.items = deque()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.items[0]

    def enqueue(self, item):
        self.size += 1
        self.items.append(item)

    def dequeue(self):
        if self.is_empty(): raise IndexError()
        self.size -= 1
        item = self.items.popleft()
        return item

    def reverse(self):
        stack = Stack()

        while not self.is_empty():
            stack.push(self.dequeue())

        while not stack.is_empty():
            self.enqueue(stack.pop())

    def copy(self):
        return self.items.copy()

    def __str__(self):
        size = self.size
        copy = self.copy()
        return f'{[copy.popleft() for _ in range(size)]}'


def main():
    q = Queue()
    for idx in range(1, 11):
        q.enqueue(idx)
    print('\n\t', q)
    q.reverse()
    print('\t', q, '\n')
    print('\t peek: ', q.peek(), '\n')


if __name__ == '__main__':
    main()



