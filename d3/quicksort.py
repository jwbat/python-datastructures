from random import shuffle

from utils.printarray import print_array


def quick_sort(array):
    def sort(array, start, end):
        if start < end:

            boundary = partition(array, start, end)

            sort(array, start, boundary - 1)
            sort(array, boundary + 1, end)

    def partition(array, start, end):
        pivot = array[end]
        b = start - 1
        for idx in range(start, end):
            if array[idx] <= pivot:
                b += 1
                array[b], array[idx] = array[idx], array[b]

        b += 1
        array[b], array[end] = array[end], array[b]
        return b

    sort(array, 0, len(array) - 1)




def main():
    #t = [8, 2, 4, 1, 3]
    t = list(range(1, 51))
    shuffle(t)

    print_array(t)
    quick_sort(t)
    print_array(t)

if __name__ == '__main__':
    main()
