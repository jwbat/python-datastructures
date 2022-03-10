
def bubble_sort(t):
    if len(t) < 2:
        return

    for idx in range(len(t)):
        done = True
        for jdx in range(1, len(t) - idx):
            if t[jdx] < t[jdx - 1]:
                t[jdx], t[jdx - 1] = t[jdx - 1], t[jdx]
                done = False
        if done:
            return


t = [8, 2, 4, 1, 3]
#t = [4, 3]
bubble_sort(t)
print(t)

