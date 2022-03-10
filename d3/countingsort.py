

def counting_sort(array):
    if len(array) < 2:
        return
    maxval = max(array)
    counts = [0] * (maxval + 1)
    for num in array:
        counts[num] += 1

    jdx = 0
    for idx in range(len(counts)):
        while counts[idx]:
            array[jdx] = idx
            jdx += 1
            counts[idx] -= 1



t = [5, 3, 2, 5, 4, 4, 5]
counting_sort(t)
print(t)
