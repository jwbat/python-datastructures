from random import shuffle

def insertion_sort(lst):
    if len(lst) < 2:
        return

    for idx in range(1, len(lst)):
        current = lst[idx]
        jdx = idx - 1

        while jdx >= 0 and lst[jdx] > current:
            lst[jdx + 1] = lst[jdx]
            jdx -= 1
        lst[jdx + 1] = current


t = list(range(1, 101))
shuffle(t)
print(t, '\n')
insertion_sort(t)
print(t)
