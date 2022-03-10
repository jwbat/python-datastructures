'''
AVLTree
'''
from time import sleep

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return AVLNode(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        self.set_height(root)

        return self.balance(root)

    def balance(self, root):
        if self.is_left_heavy(root):
            if self.balance_factor(root.left) < 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if self.is_right_heavy(root):
            if self.balance_factor(root.right) > 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        self.set_height(root)
        self.set_height(new_root)
        return new_root

    def set_height(self, node):
        node.height = max(self.height(node.left),
                          self.height(node.right)) + 1

    def is_balanced(self):
        def _is_balanced(root):
            if root is None:
                return True
            return not self.is_left_heavy(root) and \
                   not self.is_right_heavy(root) and \
                       _is_balanced(root.left) and \
                       _is_balanced(root.right)
        return _is_balanced(self.root)

    def is_left_heavy(self, root):
        return self.balance_factor(root) > 1

    def is_right_heavy(self, root):
        return self.balance_factor(root) < -1

    def balance_factor(self, root):
        return 0 if root is None else self.height(root.left) - self.height(root.right) 

    def height(self, root):
        return -1 if root is None else root.height

    @property
    def size(self):
        def _size(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            else:
                return 1 + _size(root.left) + _size(root.right)
        return _size(self.root)

    def is_perfect(self):
        height = self.root.height
        size = self.size
        return size == 2 ** (height + 1) - 1

    def __str__(self):
        return f'{self.root}'

class AVLNode:
     def __init__(self, value=None):
         self.value = value
         self.left = None
         self.right = None
         self.height = 0

     def __repr__(self):
         return f'Node({self.value}, {self.left}, {self.right}, height={self.height})'


def main():
    tree = AVLTree()
    #nums = [4, 5, 6, 7]
    nums = [30, 10, 20, 2, 12, 25, 35]
    #nums = nums[::-1]
    #nums = [4, 5, 3, 9, 2, 6]
    for num in nums:
        tree.insert(num)

    print('tree: ', tree)
    print('-' * 30)
    print('size of tree: ', tree.size)
    print('-' * 30)
    print('tree is perfect: ', tree.is_perfect())
    print('-' * 30)
    print('tree is balanced: ', tree.is_balanced())
    print('height of tree: ', tree.root.height)

main()
