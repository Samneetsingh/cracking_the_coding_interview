class Node(object):

    def __init__(self, info) -> None:
        self.__info = info
        self.__next = None

    def get_next(self) -> object:
        return self.__next

    def get_info(self) -> int:
        return self.__info

    def set_next(self, link: object) -> None:
        self.__next = link

    def set_info(self, info: int) -> None:
        self.__info = info
