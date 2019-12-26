from typing import Any

from src.main.collection.trees.binaryTree import BinaryTree
from src.main.collection.trees.binaryLeaf import BinaryLeaf


class AVLTree(BinaryTree):

    def __init__(self, info: Any):
        super(AVLTree, self).__init__(info=info)
        self.__level = 0

    def get_level(self):
        return self.__level

    def __rotate_left(self):
        pass

    def __rotate_right(self):
        pass


def calculate_height(root: BinaryLeaf) -> int:
    pass


if __name__ == '__main__':
    tree = AVLTree(info=12)
    tree.insert(info=8)
    tree.insert(info=18)
    tree.insert(info=5)
    tree.insert(info=11)
    tree.insert(info=4)
    tree.insert(info=17)
    # tree.traverse()

    print(calculate_height(root=tree.get_root()))
