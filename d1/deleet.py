'''
Deleting the first element of an array is O(n).
'''

from time import perf_counter as pc

arr1 = list(range(1, 1001))
arr2 = list(range(1, 10 ** 7 + 1))

def timethatmother(arrs):
    print('\n###############################################\n')
    for arr in arrs:
        t0 = pc()
        del arr[0]
        time = pc() - t0
        print('del arr[0] time: ', time)
        print('-----------------------------------------------')
        t0 = pc()
        arr.pop() 
        time = pc() - t0
        print('pop() time: ', time)
        print('\n###############################################\n')

timethatmother([arr1, arr2])

