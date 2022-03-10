'''
Queue implemented using a LinkedList.
'''


from linked_list import Node, LinkedList

# LL attrs & methods: first, last, is_empty, get_size, index_of, 
#  get_previous, add_first, add_last, remove_first, remove_last,
#  contains, reverse, to_list, print_list

class LinkedListQueue:
    def __init__(self):
        self.items = LinkedList()
        self.size = self.items.get_size()

    def is_empty(self):
        return self.items.get_size() == 0

    def peek(self):
        return self.items.first.get_value()

    def enqueue(self, item):
        self.size += 1
        self.items.add_last(item)

    def dequeue(self):
        if self.is_empty(): raise IndexError()
        self.size -= 1
        item = self.items.first
        self.items.remove_first()
        return item

    def __str__(self):
        lst = self.items.to_list()
        return f'{lst}'


def main():
    print()

    llq = LinkedListQueue()
    for x in range(1, 5):
        llq.enqueue(x)
    llq.dequeue()

    print('----------------------------------------------------------------------')
    print('\n\t', llq)
    print('\n\t peek: ', llq.peek())
    print()
    print('----------------------------------------------------------------------')

if __name__ == '__main__':
    main()


