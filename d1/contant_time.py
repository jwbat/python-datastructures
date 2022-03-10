from time import perf_counter as pc

arr1 = list(range(1, 11))
arr2 = list(range(1, 10 ** 3 + 1))
arr3 = list(range(1, 10 ** 7 + 1))

'''
Constant time operation: access 1st el of lst.
 O(1)
'''
def timer(lsts):
    for lst in lsts:
        t0 = pc()
        item = lst[0]
        t = pc() - t0
        print('  time: ', t)
    print('----------------------------')

timer([arr1, arr2, arr3])

'''
Linear time operation: print els in 1st.
 O(n)
'''
def timer2(lsts):
    for lst in lsts:
        t0 = pc()
        for idx in range(len(lst)):
            item = lst[idx]
        t = pc() - t0
        length = str(len(lst)).rjust(10)
        t = str(t).rjust(10)
        print('  length of list: ' + length + '  time: ' + t)
    print('----------------------------')

timer2([arr1, arr2, arr3])


