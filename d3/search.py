from random import shuffle

class Search:
    def linear_search(self, lst, item):
        for idx in range(len(lst)):
            if lst[idx] == item:
                return idx
        return -1

    # iterative
    def binary_search1(self, lst, item):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid= (left + right) // 2

            if item == lst[mid]:
                return mid
            if item > lst[mid]:
                left = mid + 1
            if item < lst[mid]:
                right = mid - 1
        return -1

    # recursive
    def binary_search2(self, lst, item):

        def binarysearch(left, right):
            if right < left:
                return -1

            mid = (left + right) // 2

            if lst[mid] == item:
                return mid
            elif item > lst[mid]:
                return binarysearch(mid + 1, right)
            else:
                return binarysearch(left, mid - 1)

        return binarysearch(0, len(lst) - 1)

    def ternary_search(self, lst, item):

        def ternarysearch(left, right):
            if right < left:
                return -1

            partition_size = (right - left) // 3
            mid1 = left + partition_size
            mid2 = right - partition_size

            if item == lst[mid1]:
                return mid1
            if item == lst[mid2]:
                return mid2

            if item > lst[mid2]:
                return ternarysearch(mid2 + 1, right)
            elif item > lst[mid1]:
                return ternarysearch(mid1 + 1, mid2 - 1)
            return ternarysearch(left, mid1 - 1)

        return ternarysearch(0, len(lst) - 1)

    def jump_search(self, lst, item):
        length = len(lst)
        block_size = int(length ** (1 / 2))
        start, nxt = 0, block_size

        while start < length and item > lst[nxt - 1]:
            start = nxt
            nxt += block_size
            if nxt > length:
                nxt = length

        for idx in range(start, nxt):
            if lst[idx] == item:
                return idx

        return -1

    def exponential_search(self, lst, item):
        bound = 1
        while bound < len(lst) and item >= lst[bound]:
            bound *= 2

        left, right = bound // 2, min(bound, len(lst))
        idx = self.binary_search2(lst[left : right], item)
        if idx > -1:
            return idx + bound // 2
        return -1


def main():
    #t = [4, 7, 23]
    t = list(range(5, 37))
    #t = []
    print('list: ', t)

    s = Search()
    item = 11
    print(f'\n\t index of {item}: ', s.exponential_search(t, item))
    print()


if __name__ == '__main__':
    main()
