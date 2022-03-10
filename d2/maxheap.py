def maxheapify(arr):

    def _maxheapify(arr, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2

        largest = idx

        if left < n and arr[left] > arr[idx]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            _maxheapify(arr, largest)

    n = len(arr) 
    for idx in range(n // 2 - 1, -1, -1):
        _maxheapify(arr, idx)

##################################################################


#nrs = [3, 4, 5, 99]
nrs = [15, 10, 3, 8, 12, 9, 4, 1, 24]
#nrs = [5, 3, 8, 4, 1, 2]
maxheapify(nrs)
print('\n\t', nrs,'\n')

##################################################################

def is_max_heap(arr):
    n = len(arr)
    for idx in range(0, n // 2):
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and arr[left] > arr[idx]:
            return False
        if right < n and arr[right] > arr[idx]:
            return False
    return True

#nrs = [7, 3, 13]
print('\n\t', is_max_heap(nrs),'\n')



