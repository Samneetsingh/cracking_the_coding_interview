import unittest

from src.main.collection.trees import BinaryLeaf
from src.main.collection.trees import BinaryTree
from src.main.collection.trees import TreeTraversal


class TestTreeTraversal(unittest.TestCase):

    def setUp(self) -> None:
        self.root = BinaryLeaf(info=10)
        left = BinaryLeaf(info=5)
        right = BinaryLeaf(info=15)
        self.root.set_left(left=left)
        self.root.set_right(right=right)

        left_left = BinaryLeaf(info=3)
        left_right = BinaryLeaf(info=7)

        left.set_left(left=left_left)
        left.set_right(right=left_right)

    def test_pre_order(self):
        self.assertEqual(TreeTraversal.pre_order(root=self.root), [10, 5, 3, 7, 15])

    def test_in_order(self):
        TreeTraversal.in_order(root=self.root), [3, 5, 7, 10, 15]

    def test_post_order(self):
        self.assertEqual(TreeTraversal.post_order(root=self.root), [3, 7, 5, 15, 10])


class TestBinaryTrees(unittest.TestCase):

    def test_add(self):
        tree = BinaryTree(info=10)
        tree.add(info=2)
        tree.add(info=12)
        tree.add(info=15)
        tree.traverse()
        pass

    def test_remove(self):
        pass


if __name__ == '__main__':
    unittest.main()
