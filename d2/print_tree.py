'''
A few recursive functions.
'''
# except for this one, for now.
# to be worked on "later"...
def printree():
    lst1 = [7]
    lst2 = [4, 9]
    lst3 = [1, 6, 8, 10]

    f = lambda s, n: s.rjust(space)

    s = ''.join(f(str(n)) for n in lst)

def reverse(s):
    '''Reverse string, s.'''
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def addup(*args):
    '''Recursively add up numbers in args.'''
    if len(args) == 1:
        return args[0]
    else:
        return  addup(*args[1:]) + args[0]

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(16))
#print(addup(7, 7, 7, 7, 7))
#print(reverse('abcdefghij'))







