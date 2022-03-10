from random import shuffle

from utils.printarray import print_array


def merge_sort(array):
    length = len(array)
    if length > 1:
        mid = length // 2
        left, right = array[ : mid], array[mid: ]

        merge_sort(left)
        merge_sort(right)

        merge(array, left, right)

def merge(array, left, right):
    left += [float('inf')]
    right += [float('inf')]
    idx, jdx = 0, 0
    for kdx in range(len(array)):
        if left[idx] < right[jdx]:
            array[kdx] = left[idx]
            idx += 1
        else:
            array[kdx] = right[jdx]
            jdx += 1


t = list(range(1, 101))
shuffle(t)

print_array(t)
merge_sort(t)
print_array(t)
