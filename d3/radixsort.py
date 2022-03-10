from collections import deque as queue

def radix_sort(t):
    length = len(t)
    maxlen = len(str(max(t)))
    bins = [queue() for _ in range(10)]

    # get digit of x at position n from right
    f = lambda x, n: (x // 10 ** n) % 10

    def empty(bins):
        for q in bins:
            while len(q):
                yield q.popleft()

    for n in range(maxlen):
        for x in t:
            bins[f(x, n)].append(x)

        idx = 0
        for x in empty(bins):
            t[idx] = x
            idx += 1

t = [462, 273, 12, 1465, 722, 5, 383]

print('\n\t', t)
radix_sort(t)
print('\n\t', t, '\n\t')
