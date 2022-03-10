from random import shuffle


def get_min_index(t):
    min_idx = 0
    for idx in range(len(t)):
        if t[idx] < t[min_idx]:
            min_idx = idx
    return min_idx

def selection_sort(t):
    if len(t) < 2:
        return
    for idx in range(len(t)):
        min_idx = get_min_index(t[idx : ]) + idx
        t[idx], t[min_idx] = t[min_idx], t[idx]


t = list(range(1, 101))
shuffle(t)
print(t)
print()
selection_sort(t)
print(t)
print()
