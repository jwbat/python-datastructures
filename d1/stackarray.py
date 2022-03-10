

from array import array

class Stack2:
    def __init__(self):
        # 'L' -> 4-byte unsigned int
        self.items = array('L')
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

    def __str__(self):
        lst = self.items.tolist()
        return f'{lst}'


def main():
    stack = Stack2()
    for idx in range(1, 11):
        stack.push(idx)
    print(stack)
    while not stack.is_empty():
        print(str(stack.pop()).rjust(6))

if __name__ == '__main__':
    main()
