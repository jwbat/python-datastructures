'''
Array class.
'''


class Array:
    def __init__(self):
        self._lst = []

    def insert(self, item):
        self._lst.append(item)

    def remove_at(self, index):
        del self._lst[index]

    def index_of(self, index):
        try:
            return self._lst.index(index)
        except:
            return -1

    def insert_at(self, item, index):
        self._lst.insert(index, item)

    def max(self):
        return max(self._lst)

    def intersect(self, other):
        return list(set(self._lst) & set(other._lst))

    def reverse(self):
        self._lst.reverse()

    def __str__(self):
        return str(self._lst)
        #return '\n'.join([str(item) for item in self._lst])



nums = Array()
nums.insert(3)
nums.insert(37)
nums.insert(219)
print(nums)
nums.reverse()
print(nums)
nums.insert_at(55, 0)
print(nums)


other = Array()
other.insert(37)
other.insert(45)
print(nums.intersect(other))


