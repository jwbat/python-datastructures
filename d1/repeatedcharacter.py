'''
One fcn returns the first nonrepeated character from string, s.
The other returns the first repeated character from the string.
'''

def print_dict(d):
    for k, v in d.items():
        print('\t', k, '=> ', v)

def char_count_dict(s):
    d = dict()
    for char in s:
        count = d.get(char, 0)
        d[char] = count + 1
    return d


def first_nonrepeated_char(s, d):
    for char in s:
        if d[char] == 1:
            return char
    return None

def first_repeated_char(s):
    st = set()
    for char in s:
        if char in st:
            return char
        st.add(char)
    return None

#s = 'Where have I heard that?'
#s = 'Wherefore art thou Romeo?'
s = 'Grilled cheeses are great with mustard.'

s = s.lower()
d = char_count_dict(s)
print('\n string:  ', s)
print('\n\t 1st nonrepeated char: ', first_nonrepeated_char(s, d))
print('\t 1st repeated char: ', first_repeated_char(s), '\n')



