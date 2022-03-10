'''
Binary Tree.
'''
from math import sqrt

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    break
                current = current.right

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def traverse_preorder(self):
        def traverse(root):
            # Root, left, right
            if not root:
                return

            print(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)

    def contains(self, num):
        return self._contains(self.root, num)

    def _contains(self, root, num):
        if not root:
            return False

        if root.value == num:
            return True

        return self._contains(root.left, num) | \
                self._contains(root.right, num)

    def get_nodes_at_distance(self, k):
        lst = []
        def dist(root, k):
            if not root:
                return

            if not k:
                lst.append(root.value)

            return dist(root.left, k - 1), dist(root.right, k - 1)

        dist(self.root, k)
        return lst

    def traverse_levelorder(self):
        for k in range(self.height + 1):
            for value in self.get_nodes_at_distance(k):
                print(value, end=' ')
            print()

    def get_ancestors(self, n):
        lst = []
        def get(root, n):
            if not root:
                return False

            if root.value == n:
                return True

            if get(root.left, n) | get(root.right, n):
                lst.append(root.value)
                return True

            return False
        get(self.root, n)
        return lst

    def are_siblings(self, n1, n2):
        def _are_sibs(root, n1, n2):
            if not root:
                return False

            left, right = root.left, root.right
            if not left:
                return _are_sibs(right, n1, n2)
            if not right:
                return _are_sibs(left, n1, n2)
            return ({left.value,  right.value} == {n1, n2}) | \
                _are_sibs(left, n1, n2) | _are_sibs(right, n1, n2)
        return _are_sibs(self.root, n1, n2)

    def count_leaves(self):
        def countleaves(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            else:
                return countleaves(root.left) + countleaves(root.right)
        return countleaves(self.root)

    @property
    def size(self):
        f = lambda k: self.get_nodes_at_distance(k)
        return len([value for k in range(self.height + 1) for value in f(k)])

    @property
    def height(self):
        def _height(root):
            if not root: return -1
            if self.is_leaf(root):
                return 0
            else:
                return 1 + max(_height(root.left), _height(root.right))
        return _height(self.root)

    def is_bst(self):
        #self.swap_root()
        def validate(root, minval, maxval):
            if not root:
                return True
            else:
                return (minval < root.value < maxval) and \
                validate(root.left, minval, root.value) and \
                validate(root.right, root.value, maxval)

        return validate(self.root, float('-inf'), float('inf'))

    def swap_root(self):
        # test is_bst with a non-BST
        self.root.left, self.root.right = self.root.right, self.root.left

    def traverse_inorder(self):
        def traverse(root):
            # left, Root, right
            if not root:
                return

            traverse(root.left)
            print(root.value)
            traverse(root.right)
        traverse(self.root)

    def traverse_postorder(self):
        def traverse(root):
            # left, right, Root
            if not root: return

            traverse(root.left)
            traverse(root.right)
            print(root.value)
        traverse(self.root)

    def sort(self):
        '''Return the node values in ascending order'''
        # left, Root, right
        def _sort(root):
            if not root:
                return []

            else:
                return _sort(root.left) + [root.value] + _sort(root.right)
        return _sort(self.root)

    @property
    def max(self):
        def _max(root):
            if not root:
                return
            elif not root.right:
                return root.value
            else:
                return _max(root.right)
        return _max(self.root)

    # O(log n)
    @property
    def min(self): 
        current = self.root
        last = current
        while current:
            last = current
            current = current.left
        return last.value

    def equals(self, other):
        def eq(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2:
                return root1.value == root2.value and \
                    eq(root1.left, root2.left) and \
                    eq(root1.right, root2.right)
            return False
        return eq(self.root, other.root)

    #def min(self):
    #    return self._min(self.root)
    # O(n)
    def _min(self, root):
        if self.is_leaf(root):
            return root.value
        else:
            left = self._min(root.left) 
            right = self._min(root.right) 
            return min(left, right, root.value)

    def is_leaf(self, node):
        return not node.left and not node.right

    def __repr__(self):
        return f'{self.root}'


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.value})'


def main():
    def showtree(tree):
        print('\n\t', tree, '\n')


    def make(tree, nums):
        for num in nums:
            tree.insert(num)

    def find(tree, nums):
        for num in nums:
            print(f'\n   {num} can be found in the tree. ', tree.find(num))

    def traverse2(rootnode):
        space = 10
        count = 1
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print('  ' * space, n.value, end = '  ' * space)
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print('\n')
            count += 5
            space = int(space - sqrt(count))
            thislevel = nextlevel

    print()
    nums = [7, 4, 9, 6, 8, 1, 10]
    #nums = [7, 4, 9]
    nums2 = [7, 4, 9, 6, 8, 1]
    tree1= Tree()
    tree2 = Tree()
    tree3 = Tree()
    make(tree1, nums)

    tree1.traverse_levelorder()
    print('-' * 50)
    num = 6
    print(f'\t get ancestors of {num}: ', tree1.get_ancestors(num))
    print('\t tree size: ', tree1.size)
    print('\t leaf count: ', tree1.count_leaves())
    print('\t tree contains 8: ', tree1.contains(8))
    #print('\n\t min value in tree: ', tree1.min)
    #print('\t max value in tree: ', tree1.max)
    #sibs = (6, 1)
    #print(f'\n\t {sibs} are siblings: ', tree1.are_siblings(*sibs))
    print('\t nodes at k: ', tree1.get_nodes_at_distance(2))
    #print(tree1.is_bst())
    #make(tree2, nums)
    #make(tree3, nums2)

    #print(tree1.equals(tree2))
    #print(tree1.equals(tree3))

    #print('\n\t height of tree: ', tree.height)

    def traverse(tree):
        tree.traverse_preorder()
        print('-' * 50)
        tree.traverse_inorder()
        print('-' * 50)
        tree.traverse_postorder()

    #traverse(tree)

    #print('sorted list of node values: ', tree.sort())
    #print('\n\t', tree.root.value)
    #showtree(tree)
    #find(tree, nums[-3:])
    #traverse(tree.root)
    #print('\n\t', tree, '\n')
    print()

main()
