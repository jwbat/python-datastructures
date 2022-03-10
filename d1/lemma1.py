'''
Computational check of the lemma:
  If 0 <= x <= 2, then -x^3 + 4x + 1 > 0.
 (It can also easily be proven algebraically.)
'''
import numpy as np

def f(x):
    return -x ** 3 + 4 * x + 1

def main():
    gen = (x for x in np.arange(0, 2, 0.0001))
    while True:
        try:
            x = next(gen)
            ans = f(x)
            if ans <= 0:
                print(f'for x = {x}, f(x) is {ans}')
            #print(round(x, 2), ':  ',  round(ans, 2))
        except:
            print('Done.')
            break
    print('The lemma')
    print('  If 0 <= x <= 2, then -x^3 + 4x + 1 > 0.')
    print(' is true for all values tested.')

main()

