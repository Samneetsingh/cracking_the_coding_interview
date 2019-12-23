from typing import Any
from typing import TypeVar

BL = TypeVar('BL', bound='BinaryLeaf')


class BinaryLeaf(object):

    def __init__(self, info):
        self.__info = info
        self.__left = None
        self.__right = None

    def get_info(self) -> Any:
        """
        Function to get information
        """
        return self.__info

    def get_left(self) -> BL:
        """
        Function to get left child node
        """
        return self.__left

    def set_left(self, leaf: BL) -> None:
        """
        Function to set left child node
        """
        self.__left = leaf

    def get_right(self) -> BL:
        """
        Function to get right child node
        """
        return self.__right

    def set_right(self, leaf: BL) -> None:
        """
        Function to set right child node
        """
        self.__right = leaf
