from typing import Any, Callable

from src.main.collection.trees.baseTree import BaseTree
from src.main.collection.trees.binaryLeaf import BinaryLeaf


class BinaryTree(BaseTree):

    def __init__(self, info: Any) -> None:
        self.__root = BinaryLeaf(info=info)
        self.__functions = {
            'pre_order': self.__pre_order,
            'in_order': self.__in_order,
            'post_order': self.__post_order
        }

    def get_root(self) -> BinaryLeaf:
        """
        Function to return root leaf
        :return: root leaf
        """
        return self.__root

    def __in_order(self, func: Callable[[BinaryLeaf, int], None], root: BinaryLeaf, level: int = 0) -> None:
        """
        Function to traverse tree in in-order fashion
        :param func: function to execute on the node
        :param root: root node
        :param level: base level of the tree
        :return: None
        """
        if root is not None:
            new_level = level + 1
            self.__in_order(func=func, root=root.get_left(), level=new_level)
            func(root, level)
            self.__in_order(func=func, root=root.get_right(), level=new_level)

    def __pre_order(self, func: Callable[[BinaryLeaf, int], None], root: BinaryLeaf, level: int = 0) -> None:
        """
        Function to traverse tree in pre-order fashion
        :param func: function to execute on the node
        :param root: root node
        :param level: base level of the tree
        :return: None
        """
        if root is not None:
            new_level = level + 1
            func(root, level)
            self.__pre_order(func=func, root=root.get_left(), level=new_level)
            self.__pre_order(func=func, root=root.get_right(), level=new_level)

    def __post_order(self, func: Callable[[BinaryLeaf, int], None], root: BinaryLeaf, level: int = 0) -> None:
        """
        Function to traverse tree in post-order fashion
        :param func: function to execute on the node
        :param root: root node
        :param level: base level of the tree
        :return: None
        """
        if root is not None:
            new_level = level + 1
            self.__post_order(func=func, root=root.get_left(), level=new_level)
            self.__post_order(func=func, root=root.get_right(), level=new_level)
            func(root, level)

    def __insert_helper(self, root: BinaryLeaf, info: Any) -> None:
        """
        Function to recursively insert node
        :param root: root node
        :param info: value to be added to the tree
        :return: None
        """
        if info <= root.get_info():
            if root.get_left() is None:
                root.set_left(leaf=BinaryLeaf(info=info))
            else:
                self.__insert_helper(root=root.get_left(), info=info)
        else:
            if root.get_right() is None:
                root.set_right(leaf=BinaryLeaf(info=info))
            else:
                self.__insert_helper(root=root.get_right(), info=info)

    def insert(self, info: Any) -> None:
        """
        Function to add new node
        :param info: value to add to the tree
        :return: None
        """
        self.__insert_helper(root=self.__root, info=info)

    def remove(self, info: Any) -> None:
        """
        Function to remove information from the tree
        :param info: value to be removed from the tree
        :return: None
        """
        pass

    def traverse(self, name='in_order') -> None:
        """
        Function to traverse the tree
        :param name: name of the order to traverse the tree
        :return: None
        """
        self.__functions[name](func=lambda leaf, level: print(leaf.get_info()), root=self.__root)

    def to_list(self, name='in_order') -> list:
        """
        Function to convert tree to a list
        :param name: name of the order to traverse the tree
        :return: None
        """
        elements = list()
        self.__functions[name](func=lambda leaf, level: elements.append(leaf.get_info()), root=self.__root)
        return elements


if __name__ == '__main__':
    tree = BinaryTree(info=10)
    tree.insert(info=5)
    tree.insert(info=15)
    tree.insert(info=20)
    tree.traverse()
