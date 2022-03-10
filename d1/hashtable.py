'''
HashTable with chaining via LinkedList.
'''
from linked_list import Node, LinkedList

class HashTable:

    def __init__(self, size=10):
        self.array = [None] * size
        self.size = size

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        entry = self.get_entry(key)
        if entry:
            entry.value = value
            return

        bucket = self.get_or_create_bucket(key)
        bucket.add_last(Entry(key, value))

    def get(self, key):
        entry = self.get_entry(key)
        return entry.value if entry.key == key else None

    def remove(self, key):
        entry = self.get_entry(key)
        if not entry: raise IndexError()
        self.get_bucket(key).remove(entry)

    def get_entry(self, key):
        bucket = self.get_bucket(key)
        if bucket:
            for entry in bucket:
                if entry and (entry.key == key):
                    return entry
        return None

    def get_bucket(self, key):
        return self.array[self.hash(key)]

    def get_or_create_bucket(self, key):
        idx = self.hash(key)
        bucket = self.array[idx]
        if not bucket:
            bucket = self.array[idx] = LinkedList()
        return bucket

    def print_table(self):
        print('-' * 50)
        for idx in range(self.size):
            bucket = self.array[idx]
            if bucket:
                bucket.print_list()
        print('-' * 50)
        

class Entry:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 

    def __str__(self):
        return f'({self.key}, {self.value})'

def main():
    ht = HashTable()
    ht.put(3, 'wind')
    ht.put(4, 'space')
    ht.put(5, 'water')
    ht.put(6, 'mind')
    ht.put(15, 'fire')
    ht.put(7, 'stone')
    ht.put(8, 'wood')
    ht.put(18, 'moon')
    ht.put(9, 'sun')
    ht.put(25, 'ice')
    ht.put(17, 'earth')
    ht.print_table()


    def main2():
        print('\n\t getting key=3..', ht.get(3))
        print('\t getting key=5..', ht.get(5))
        print('\t getting key=15..', ht.get(15))
        print('\t getting key=25..', ht.get(25))
        print('\n\t removing keys 3 and 15..')
        ht.remove(3)
        #print('\t remove key=3 and try to get..', ht.get(3))
        ht.remove(15)
        #print('\t remove key=15 and try to get..', ht.get(15))
        ht.print_table()
        print()

    #main2()

if __name__ == '__main__':
    main()

