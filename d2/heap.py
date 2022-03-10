'''
Heap.
'''
import numpy as np

class Heap:
    def __init__(self, capacity=15): # 2^n - 1
        self.array = np.empty(capacity, dtype=np.uint8)
        self.length = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.length

    def is_empty(self):
        return self.size == 0

    def expand(self):
        self.capacity = 2 * self.capacity + 1
        self.array.resize((self.capacity,), refcheck=False)

    def insert(self, value):
        if self.is_full():
            self.expand()
        self.array[self.size] = value
        self.size += 1
        self.bubble_up()

    def bubble_up(self):
        idx = self.size - 1
        while idx > 0 and self.array[idx] > self.array[self.parent(idx)]:
            self.swap_values(idx, self.parent(idx))
            idx = self.parent(idx)

    def remove(self):
        if self.is_empty(): raise ValueError()

        root = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.bubble_down()
        return root

    def bubble_down(self):
        idx = 0
        while idx <= self.size and not self.is_valid_parent(idx):
            larger_child_idx = self.larger_child_idx(idx)
            self.swap_values(idx, larger_child_idx)
            idx = larger_child_idx

    def larger_child_idx(self, idx):
        if not self.has_left_child(idx):
            return idx

        if not self.has_right_child(idx):
            return self.left_child_idx(idx)

        if self.left_child(idx) > self.right_child(idx):
            return self.left_child_idx(idx)

        return self.left_child_idx(idx) + 1

    def has_left_child(self, idx):
        return self.left_child_idx(idx) <= self.size

    def has_right_child(self, idx):
        return self.left_child_idx(idx) + 1 <= self.size

    def is_valid_parent(self, idx):
        if not self.has_left_child(idx):
            return True

        is_valid = self.array[idx] >= self.left_child(idx)

        if self.has_right_child(idx):
            is_valid &= self.array[idx] >= self.right_child(idx)

        return is_valid

    def left_child(self, idx):
        return self.array[self.left_child_idx(idx)]

    def right_child(self, idx):
        return self.array[self.left_child_idx(idx) + 1]

    def left_child_idx(self, idx):
        return idx * 2 + 1

    def parent(self, idx):
        return (idx - 1) // 2

    def swap_values(self, idx1, idx2):
        arr = self.array
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    def __str__(self):
        return f'{self.array[:self.size]}'


def main():
    heap = Heap()
    nums = [15, 10, 3, 8, 12, 9, 4, 1, 24]
    for num in nums:
        heap.insert(num)
    print('\n\t starting values: ', nums, '\n')
    print('\t the heap: ', heap, '\n')
    print('\t removing largest... \n')
    print('\t removed item: ', heap.remove(), '\n')
    print('\t the heap: ', heap, '\n')

if __name__ == '__main__':
    main()




