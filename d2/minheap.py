'''
MinHeap minheapifies an array of nodes, key-value pairs, by their integer keys.
'''


class Node:
    def __init__(self, key=None, value=None):
        self.key = key # int
        self.value = value # str

    def __repr__(self):
        return f'({self.key}, {self.value})'

class MinHeap:

    def minheapify(self, arr):

        def _minheapify(arr, idx):
            left = 2 * idx + 1
            right = 2 * idx + 2

            smallest = idx

            if left < n and arr[left].key < arr[idx].key:
                smallest = left

            if right < n and arr[right].key < arr[smallest].key:
                smallest = right

            if smallest != idx:
                arr[idx], arr[smallest] = arr[smallest], arr[idx]
                _minheapify(arr, smallest)

        n = len(arr)
        for idx in range(n // 2 - 1, -1, -1):
            _minheapify(arr, idx)


def main():
    arr = [Node(8, 'ox'), Node(9, 'bird'), Node(5, 'dog'), Node(1, 'lion'), Node(2, 'fish')]
    mh = MinHeap()
    mh.minheapify(arr)
    print('\n\t', arr, '\n')

if __name__ == '__main__':
    main()
