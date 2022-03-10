'''
Stack class using collections.deque
'''
from collections import deque
#from time import perf_counter as pc
#from stackarray import Stack2


class Stack:
    def __init__(self):
        self.items = deque()
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty(): 
            raise IndexError()

        self.size -= 1
        return self.items.pop()

    def peek(self):
        if self.is_empty(): return
            
        return self.items[-1]

    def is_empty(self):
        return self.size == 0 

    def copy(self):
        return self.items.copy()

    def __str__(self):
        copy = self.items.copy()
        arr = [copy.popleft() for _ in range(self.size)]
        return f'{arr}'


def main(STACKS):
    for STACK in STACKS:
        stack = STACK()

        t0 = pc()
        for x in range(1, 10 ** 6 + 1):
            stack.push(x)
        print('\n peek:  ', stack.peek(), '\n')
        while not stack.is_empty():
            stack.pop()
        t = pc() - t0

        classname = STACK.__name__
        print('\n\t', classname, 'time: ', t, '\n')


if __name__ == '__main__':
    main([Stack, Stack2])




