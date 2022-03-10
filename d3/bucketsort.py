from random import shuffle

from utils.printarray import print_array
from quicksort import quick_sort
from linked_list import LinkedList, Node

def bucket_sort(array, k=3):

    buckets = [LinkedList() for _ in range(k)]

    maxval = max(array)

    for value in array:
        idx = (k * value) // (maxval + 1)
        buckets[idx].add_last(value)

    idx = 0
    for bucket in buckets:
        sublist = bucket.to_list()
        quick_sort(sublist)
        for num in sublist:
            array[idx] = num
            idx += 1


t = [6, 2, 5, 4, 3, 7]
t = list(range(1, 101))
shuffle(t)

print_array(t)
bucket_sort(t)
print_array(t)
