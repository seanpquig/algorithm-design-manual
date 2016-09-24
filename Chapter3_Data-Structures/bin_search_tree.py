from __future__ import print_function


class BinaryTree:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def search(self, x):
        if not self.item:
            return None

        if self.item == x:
            return self
        if x < self.item:
            if self.left:
                return self.left.search(x)
        elif self.right:
            return self.right.search(x)

        return None

    def minimum(self):
        if not self.item:
            return None

        if not self.left:
            return self
        else:
            return self.left.minimum()

    def maximum(self):
        if not self.item:
            return None

        if not self.right:
            return self
        else:
            return self.right.maximum()

    def traverse(self, func=None):
        if self.left:
            self.left.traverse(func)
        if func:
            func(self.item)
        if self.right:
            self.right.traverse(func)

    def insert(self, x):
        if not self.item:
            self = BinaryTree(x)

        if x < self.item:
            if self.left:
                self.left.insert(x)
            else:
                self.left = BinaryTree(x)
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = BinaryTree(x)


tree = BinaryTree(5)
for i in [3, 7, 1, 2, 4, 5, 6, 8, 9]:
    tree.insert(i)

print("Traversing tree in order...")
tree.traverse(lambda x: print("  {}!".format(x)))

# Test searching
assert(tree.search(0) is None)
assert(tree.search(1).item == 1)
assert(tree.search(5).item == 5)
assert(tree.search(9).item == 9)

# Test min and max
assert(tree.minimum().item == 1)
assert(tree.maximum().item == 9)
