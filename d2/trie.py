'''Trie.'''

class Trie:
    def __init__(self):
        self.root = _Node(None)

    def insert(self, word):
        current = self.root
        for char in word:
            if not current.has_child(char):
                current.add_child(char)
            current = current.get_child(char)
        current.is_end_of_word = True

    def contains(self, word):
        if word is None: return False

        current = self.root
        for char in word:
            if not current.has_child(char):
                return False
            current = current.get_child(char)
        return current.is_end_of_word

    def contains_recursive(self, word):
        def _contains(node, word):
            if len(word) == 1:
                return node.has_child(word[0])
            if not node.has_child(word[0]):
                return False
            return _contains(node.get_child(word[0]), word[1:])
        return _contains(self.root, word)

    def remove(self, word):
        def _remove(node, word):
            child = node.get_child(word[0])
            if child is None: return

            if len(word) == 1:
                child.is_end_of_word = False
            else:
                _remove(child, word[1:])
                if not child.is_end_of_word and not child.has_children():
                    node.remove_child(child.value)

        _remove(self.root, word)

    def traverse(self):
        def _traverse(node):
            if node.value is not None:
                print(node.value)
            for child in node.get_children():
                _traverse(child)
        _traverse(self.root)

    def count_words(self):
        def _count(node):
            total = 0
            if node.is_end_of_word:
                total += 1
            for child in node.get_children():
                total += _count(child)
            return total
        return _count(self.root)

    def longest_common_prefix(self, lst):
        maxlength = len(self.get_shortest(lst))
        trie = Trie()
        for word in lst:
            trie.insert(word)

        prefix = ''
        node = trie.root
        while len(prefix) <= maxlength:
            children = node.get_children()
            if len(children) != 1:
                return prefix
            node = children[0]
            prefix += node.value

    def get_shortest(self, lst):
        from functools import reduce
        f = lambda s1, s2: s1 if len(s1) < len(s2) else s2
        return reduce(f, lst)

    def autocomplete(self, word):
        lastnode = self.get_last_node(word)
        def _auto(node, word, lst):

            if node is None:
                return []

            if node.is_end_of_word:
                lst.append(word)

            for child in list(node.get_children()):
                _auto(child, word + child.value, lst)

            return lst

        return _auto(lastnode, word, lst=[])

    def get_last_node(self, word):
        if word is None:
            return
        node = self.root
        for char in word:
            node = node.get_child(char)
            if node is None:
                return
        return node

    def __repr__(self):
        pass


class _Node:

    def __init__(self, value=None):
        self.value = value  # char
        self.children = {}  # {char: Node}
        self.is_end_of_word = False

    def has_child(self, char):
        return char in self.children

    def add_child(self, char):
        self.children[char] = _Node(char)

    def remove_child(self, char):
        del self.children[char]

    def get_child(self, char):
        return self.children.get(char)

    def has_children(self):
        return len(self.children) > 0

    def get_children(self):
        return list(self.children.values())

    def __repr__(self):
        return f'{self.value}'


def main():
    print()
    words = ['car']
    words = ['canada', 'canadian']
    words = ['card', 'care', 'careful', 'carefree']
    words = ['dog', 'egg']

    trie = Trie()
    longest = trie.longest_common_prefix(words)
    print(f'\n\t longest common prefix in the trie: {longest} \n')
    quit()

    #####################################################################
    #words = ['a', 'ask', 'asked', 'asker', 'asking']
    print('\n\t the words inserted into the trie: ')
    print('\t', words)
    trie = Trie()
    for word in words:
        trie.insert(word)


    #####################################################################
    print(f'\n\t trie contains {trie.count_words()} words! \n')

    wd = 'eggs'
    print(f'\n\t trie contains {wd}: ', trie.contains_recursive(wd), '\n')

    lst = trie.autocomplete(wd)
    print(f' \n\t autocompleting {wd}: \t {lst}')
    print()

    #trie.traverse()
    #quit()
    #word1 = 'asked'
    #print(f'\n\t  removing ** {word1} ** ..\n')
    #trie.remove(word1)
    #for w in ['a', 'ask', 'aske', 'asked', 'asker', 'asking']:
    #    print(f'trie contains {w}: '.rjust(25), trie.contains(w))

    #print()


if __name__ == '__main__':
    main()

