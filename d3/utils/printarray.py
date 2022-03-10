'''
Pretty prints an array.
'''
from time import sleep

def print_array(t):

    def pretty_print(t, nap_time = 0.01):
        print()
        for idx in range(len(t)):
            sleep(nap_time)
            end = '\n' if (idx + 1) % 10 == 0 else ''
            num = str(t[idx]).rjust(8)
            print(num, end=end, flush=True)

    pretty_print(t)
    pretty_print([' • '] * 10 + ['\n'], nap_time=0.1)
