import abc
from typing import Any


class BaseTree(abc.ABC):

    @abc.abstractmethod
    def insert(self, info: Any) -> None:
        pass

    @abc.abstractmethod
    def remove(self, info: Any) -> None:
        pass

    @abc.abstractmethod
    def traverse(self, name: str) -> None:
        pass
