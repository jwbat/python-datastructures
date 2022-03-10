'''
LinkedList and Node classes.
'''
class Node:

    def __init__(self, value, node=None):
        self.value = value
        self.next_node = node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def has_next(self):
        return self.next_node != None

    def to_string(self):
        return str(self.value)

    def __str__(self):
        return f'Node({self.value}, {self.next_node})'


class LinkedList:

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.size = 0

    def is_empty(self):
        return not self.first

    def get_size(self):
        return self.size

    def index_of(self, value):
        idx = 0
        current = self.first
        while current:
            if current.get_value() == value:
                return idx
            current = current.get_next()
            idx += 1
        return -1

    def get_previous(self, node):
        current = self.first
        while current:
            if current.get_next() == node:
                return current
            current = current.get_next()
        return None

    def add_first(self, value):
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.set_next(self.first)
            self.first = node
        self.size += 1

    def add_last(self, value):
        node = Node(value)
        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.set_next(node)
            self.last = node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError()
        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.get_next()
            self.first.set_next(None)
            self.first = second
        self.size -= 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError()
        if self.size == 1: 
            self.first = self.last = None
        else:
            previous = self.get_previous(self.last)
            self.last = previous
            self.last.set_next(None)
        self.size -= 1

    def contains(self, value):
        return self.index_of(value) != -1

    def reverse(self):
        if self.is_empty(): return
        previous = self.first
        current = self.first.get_next()
        while current:
            # next is a reserved word in python
            nekst = current.get_next()
            current.set_next(previous)
            previous = current
            current = nekst 

        self.last = self.first
        self.last.set_next(None)
        self.first = previous

    def get_kth_from_end(self, k):
        if self.is_empty():
            raise IndexError()
        a = b = self.first
        for _ in range(k - 1):
            b = b.get_next()
            if not b: raise IndexError()
        while b != self.last:
            a = a.get_next()
            b = b.get_next()
        return a.get_value()

    def print_middle(self):
        if self.is_empty(): return
        a = b = self.first
        while b != self.last and b.get_next() != self.last:
            a = a.get_next()
            b = b.get_next().get_next()
        if b == self.last:
            print('\n\t middle: ', a.get_value(), '\n')
        else:
            print('\n\t middles: ', a.get_value(), ', ', a.get_next().get_value(),'\n')

    def has_loop(self):
        if self.is_empty(): return False
        a = b = self.first
        while b.has_next():
            a = a.get_next()
            b = b.get_next()
            if b.has_next():
                b = b.get_next()
            if a is b: return True
        return False

    def to_list(self):
        lst = []
        current = self.first
        while current:
            value = current.get_value()
            lst.append(value)
            current = current.get_next()
        return lst

    def print_list(self):
        if self.is_empty():
            return
        node = self.first
        s = node.to_string()
        while node.has_next():
            node = node.get_next()
            s += f' => {node.to_string()} '
        print('\n\t', s, '\n')

    def remove(self, value):
        if not self.contains(value): raise IndexError()
        current = self.first
        if current.get_value() == value:
            self.first = self.last = None 
            return
        while current:
            if current.get_value() == value:
                prev= self.get_previous(current)
                nekst = current.get_next()
                prev.set_next(nekst)
                return
            current = current.get_next()

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.get_value()
            current = current.get_next()


def main():
    print()
    ll = LinkedList()
    for idx in range(1, 9):
        ll.add_last(idx)

    first = ll.first
    second = first.get_next() 
    third = second.get_next()
    last = ll.last

    first_val = first.get_value()
    second_val = second.get_value()
    third_val = third.get_value()
    last_val = last.get_value()

    print('first: ', first_val)
    print('second: ', second_val) 
    print('third: ', third_val) 
    print('last: ', last_val) 

    # create loop:
    #ll.last.set_next(ll.first)
    ll.print_list()
    print(' Iterate over the LL: ')
    for item in ll:
        print(item)
    #ll.print_middle()
    #print('\n\t has loop: ', ll.has_loop())
    print()
    quit()

    print('  reversing...')
    ll.reverse()
    ll.print_list()
    print('\t k = 5: ', ll.get_kth_from_end(5), '\n')

if __name__ == '__main__':
    main()

