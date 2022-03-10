'''
Algorithms using a Stack class.
'''
from collections import deque

leftbrackets = ['(', '{', '<', '[']
rightbrackets = [')', '}', '>', ']']
pairs = ['()', '{}', '<>', '[]']

def is_balanced(expr):
    '''
    Return True when the expression in the string of the argument
     contains only brackets that match and are in the proper order:
          "{[(2 + 3), <4 - 2>]}"
    Return False if a right occurs before a left
      or if there are unmatched or unpaired brackets:
          "[{}, ><]", "{(3 - 2), [4 + 5)}", "(5 - 2"
    '''
    stack = deque()
    for char in expr:
        if char in leftbrackets:
            stack.append(char)
        if char in rightbrackets:
            if len(stack) == 0: return False

            left = stack.pop()
            if left + char not in pairs:
                return False
    return True

expr = "{(1 + 2) + [3 - 2] * <5>}"
print(is_balanced(expr))
####################################################################################


def reverse(s):
    stack = deque()
    for ltr in s:
        stack.append(ltr)
    return ''.join([stack.pop() for _ in range(len(s))])

#s = 'abcdefg'
#print(f'\n\t{s} \n\t' + reverse(s) + '\n')
