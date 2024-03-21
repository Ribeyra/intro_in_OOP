""" Построение двоичного дерева """


class Node():
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, new_value):
        if self.key is None:
            self.key = new_value
        elif new_value > self.key and self.right is None:
            self.right = type(self)(new_value)
        elif new_value > self.key:
            self.right.insert(new_value)
        elif new_value < self.key and self.left is None:
            self.left = type(self)(new_value)
        elif new_value < self.key:
            self.left.insert(new_value)


tree = Node()
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)
print(tree.key)  # 9
print(tree.left.key)  # 4
print(tree.right.key)  # 17
print(tree.left.left.key)  # 3
print(tree.left.right.key)  # 6


class NewNode(Node):
    """A simple subclass of Node."""


def test_liskov_substitution():

    tree = NewNode()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    print(type(tree.left))      # "Sibling should be NewNode too"
    print(type(tree.right))     # "Sibling should be NewNode too"


test_liskov_substitution()
