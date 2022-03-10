'''
Stack implemented using two queues.
'''
from queue import Queue

class StackWithTwoQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = self.get_size()

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.queue1.size 

    def peek(self):
        if self.queue1.is_empty(): return

        self.reduce_queue1_to_one_item()
        item = self.queue1.peek()
        self.queue2.enqueue(self.queue1.dequeue())
        self.swap_queues()
        return item

    def push(self, item):
        self.queue1.enqueue(item)

    def pop(self):
        if self.queue1.is_empty(): raise IndexError()

        self.reduce_queue1_to_one_item()
        item = self.queue1.dequeue()
        self.swap_queues()
        return item

    def swap_queues(self):
        self.queue1, self.queue2 = self.queue2, self.queue1

    def reduce_queue1_to_one_item(self):
        while self.queue1.size > 1:
            self.queue2.enqueue(self.queue1.dequeue())

    def __str__(self):
        q1 = self.queue1.copy()
        lst = list(q1) 
        return f'{lst}'

def main():
    print()

    stack = StackWithTwoQueues()
    for x in range(1, 7):
        stack.push(x)
        print(f'{stack}'.rjust(40), f'\t peek: {stack.peek()}'.rjust(20))
        print()
    for _ in range(6):
        stack.pop()
        print(f'\t\tpop: {stack}'.ljust(20), f'\t peek: {stack.peek()}'.rjust(26))
        print()
    print()

main()
