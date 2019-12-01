import abc


class BinaryLeaf(object):

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def get_info(self):
        return self.info

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right


class Tree(abc.ABC):

    @abc.abstractmethod
    def add(self, info):
        pass

    @abc.abstractmethod
    def remove(self, info):
        pass


class TreeTraversal(object):
    @staticmethod
    def pre_order(root: BinaryLeaf):
        if root is None:
            return []
        else:
            return [root.get_info()] + \
                   TreeTraversal.pre_order(root.get_left()) + \
                   TreeTraversal.pre_order(root.get_right())

    @staticmethod
    def in_order(root: BinaryLeaf):
        if root is None:
            return []
        else:
            return TreeTraversal.in_order(root.get_left()) + \
                   [root.get_info()] + \
                   TreeTraversal.in_order(root.get_right())

    @staticmethod
    def post_order(root: BinaryLeaf):
        if root is None:
            return []
        else:
            return TreeTraversal.post_order(root.get_left()) + \
                   TreeTraversal.post_order(root.get_right()) + \
                   [root.get_info()]


class BinaryTree(Tree):

    def __init__(self, info):
        self.root = BinaryLeaf(info=info)

    def __add_helper(self, root, info):
        if info <= root.get_info():
            left = root.get_left()
            if left is None:
                root.set_left(BinaryLeaf(info=info))
            else:
                self.__add_helper(left, info)
        elif info > root.get_info():
            right = root.get_right()
            if right is None:
                root.set_right(BinaryLeaf(info=info))
            else:
                self.__add_helper(right, info)

    def add(self, info):
        self.__add_helper(root=self.root, info=info)

    def remove(self, info):
        pass

    def traverse(self, order="preorder"):
        methods = {
            "preorder": TreeTraversal.pre_order,
            "inorder": TreeTraversal.in_order,
            "postorder": TreeTraversal.post_order,
        }
        print(methods[order](root=self.root))
