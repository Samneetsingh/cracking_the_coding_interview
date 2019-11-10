class Node(object):

    def __init__(self, info: int) -> None:
        self.__info = info
        self.__next = None

    def __str__(self):
        return "{}".format(self.__info)

    def get_next(self) -> object:
        """
        Function to get next node
        :return: Node
        """
        return self.__next

    def get_info(self) -> int:
        """
        Function to get info
        :return: info
        """
        return self.__info

    def set_next(self, link: object) -> None:
        """
        Function to set next node
        :param link: node
        :return: None
        """
        self.__next = link

    def set_info(self, info: int) -> None:
        """
        Function to set info
        :param info: info
        :return: None
        """
        self.__info = info
