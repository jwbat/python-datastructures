'''
Speed test of two Queues: deque vs numpy implementation.
 • assessment: np version is 2x slower due to circular
   array impl that performs modulo operations on every
   pass thru enqueue and dequeue.
 • a more straightforward use of np may well be as fast
   or faster than the deque queue.  See you next time ;)
'''


from time import perf_counter as pc

from queue import Queue
from npqueue import QueueNP


def main():
    QS = [Queue, QueueNP] 
    for Q in QS:
        q = Q()
        t0 = pc()
        for x in range(1, 10 ** 6 + 1):
            q.enqueue(x)
        for _ in range(1, 10 ** 6 + 1):
            q.dequeue()
        t = pc() - t0
        print('\n\t', Q.__name__, 'time: ', t)
                
main() 
