import abc
from typing import Any


class BaseTree(abc.ABC):

    @abc.abstractmethod
    def insert(self, info: Any) -> None:
        """
        Abstract function to insert node into a tree
        """
        pass

    @abc.abstractmethod
    def remove(self, info: Any) -> None:
        """
        Abstract function to remove node from a tree
        """
        pass

    @abc.abstractmethod
    def traverse(self, name: str) -> None:
        """
        Abstract function to traverse a tree
        """
        pass
