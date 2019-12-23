class BinaryLeaf(object):

    def __init__(self, info):
        self.__info = info
        self.__left = None
        self.__right = None

    def get_info(self):
        return self.__info

    def get_left(self):
        return self.__left

    def set_left(self, leaf):
        self.__left = leaf

    def get_right(self):
        return self.__right

    def set_right(self, leaf):
        self.__right = leaf
