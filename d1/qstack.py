'''
Implementation of a queue using 2 stacks -
  i.e., only stack operations are allowed.
  • enqueue(item) is   0(1)
  • dequeue() is       0(n)
'''
from collections import deque


class Q:
    def __init__(self):
        self.stack1 = deque() # used for enqueue
        self.stack2 = deque() # used for dequeue

    def is_empty(self):
        return self.empty(self.stack1) and self.empty(self.stack2)

    def empty(self, stack):
        try:
            stack[0]
        except IndexError:
            return True
        return False

    def peek(self):
        self.stack1_to_stack2()
        return self.stack2[-1]

    def enqueue(self, item):
        while not self.empty(self.stack2):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty(): return IndexError()

        self.stack1_to_stack2()
        self.stack2.pop()

    def stack1_to_stack2(self):
        '''Move stack1 to stack2.'''
        while not self.empty(self.stack1):
            self.stack2.append(self.stack1.pop())

    def stack2_to_stack1(self):
        '''Move stack2 to stack1.'''
        while not self.empty(self.stack2):
            self.stack1.append(self.stack2.pop())

    def __str__(self):
        self.stack2_to_stack1()
        copy = list(self.stack1)
        return f'{copy}'


def main():

    q = Q()
    print()
    for x in range(1, 6):
        q.enqueue(x)
        print(q)

    q.dequeue()
    q.dequeue()
    q.enqueue(33)
    q.enqueue(44)
    print(q)
    for _ in range(3):
        q.dequeue()
        print(q)


main()
