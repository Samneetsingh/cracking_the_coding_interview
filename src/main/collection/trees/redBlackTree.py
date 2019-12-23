from typing import Any

from src.main.collection.trees.binaryTree import BinaryTree


class RedBlackTree(BinaryTree):

    def __init__(self, info: Any):
        super(RedBlackTree, self).__init__(info=info)

    def __get_height(self):
        """
        Function to calculate height
        """
        pass

    def __rotate_left(self):
        pass

    def __rotate_right(self):
        pass


if __name__ == '__main__':
    tree = RedBlackTree(info=4)
