""" Поиск в двоичном дереве """


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def search(self, value):
        current_key = self.key
        if current_key == value:
            return self
        elif current_key > value:
            if self.left is None:
                return None
            return self.left.search(value)
        elif current_key < value:
            if self.right is None:
                return None
            return self.right.search(value)


node5 = Node(5)
node22 = Node(22, left=Node(20))
tree = Node(
    9,
    Node(
        4,
        Node(3),
        Node(
            6,
            node5,
            Node(7),
        ),
    ),
    Node(
        17,
        right=node22,
    ),
)
print(tree.search(6).key)  # 6
print(tree.search(10))  # None
print(tree.search(6).left.key)  # 5
print(tree.search(6).right.key)  # 7
print(tree.search(5) is node5)  # True
print(tree.left.left.key)  # 3
