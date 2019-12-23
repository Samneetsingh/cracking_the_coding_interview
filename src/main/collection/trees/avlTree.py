from typing import Any

from src.main.collection.trees.binaryTree import BinaryTree


class AVLTree(BinaryTree):

    def __init__(self, info: Any):
        super(AVLTree, self).__init__(info=info)

    def __calculate_height(self):
        pass

    def __rotate_left(self):
        pass

    def __rotate_right(self):
        pass


if __name__ == '__main__':
    tree = AVLTree(info=4)
