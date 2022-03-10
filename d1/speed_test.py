'''
Run your speed tests here.
'''



from time import perf_counter as pc
from collections import deque
import numpy as np


Ns =[10, 10 ** 3, 10 ** 6]
arrs = [np.array, deque]


def main():
    '''testing len() on np.array & deque.'''
    print('\nFirst, len(np.array)')
    print('Second, len(deque)')
    lsts = []
    for N in Ns:
        lsts.append([x for x in range(1, N)])
    for arr in arrs:
        print('\n------------------------------------------')
        for lst in lsts:
            t0 = pc()
            a = arr(lst)
            length = len(a)
            t = pc() - t0
            print('\t time: ', t)
        print('------------------------------------------\n')


main()
