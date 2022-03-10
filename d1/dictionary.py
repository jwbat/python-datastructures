



hm = dict()
hm.update([(2, 'James')])
print(hm)
hm.update([(1, 'Monica'), (3, 'Tree Monkey')])
print(hm)
hm.pop(3)
print(hm)
print(hm.get(1))
print('key of 1 in hm? ', 1 in hm)
print('Monica in values? ', 'Monica' in hm.values())

print('list of key, value pairs: ')
for k, v in hm.items():
    print('\t', k, ':  ', v)
