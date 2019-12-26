from typing import Any
from typing import TypeVar

BinaryLeafType = TypeVar('BinaryLeafType', bound='BinaryLeaf')


class BinaryLeaf(object):

    def __init__(self, info):
        self.__info = info
        self.__left = None
        self.__right = None

    def get_info(self) -> Any:
        """
        Function to get stored information
        :return: information
        """
        return self.__info

    def get_left(self) -> BinaryLeafType:
        """
        Function to get left child
        :return: left child node
        """
        return self.__left

    def set_left(self, leaf: BinaryLeafType) -> None:
        """
        Function to set left child
        :param leaf: new leaf node
        :return: None
        """
        self.__left = leaf

    def get_right(self) -> BinaryLeafType:
        """
        Function to get right child
        :return: right child node
        """
        return self.__right

    def set_right(self, leaf: BinaryLeafType) -> None:
        """
        Function to set right child
        :param leaf: new leaf node
        :return: None
        """
        self.__right = leaf
