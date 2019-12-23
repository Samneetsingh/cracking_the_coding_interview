import unittest

from src.main.collection.trees.binaryTree import BinaryTree
from src.main.collection.trees.avlTree import AVLTree


class TestBinaryTrees(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BinaryTree(info=10)
        self.tree.insert(info=2)
        self.tree.insert(info=12)
        self.tree.insert(info=15)
        # self.tree.traverse()

    def test_insert(self):
        elements = self.tree.to_list(name='pre_order')
        self.assertIn(2, elements)
        self.assertIn(10, elements)
        self.assertIn(12, elements)
        self.assertIn(15, elements)

    def test_remove(self):
        pass

    def test_pre_order(self):
        actual = self.tree.to_list(name='pre_order')
        expected = [10, 2, 12, 15]
        self.assertEqual(actual, expected)

    def test_in_order(self):
        actual = self.tree.to_list(name='in_order')
        expected = [2, 10, 12, 15]
        self.assertEqual(actual, expected)

    def test_post_order(self):
        actual = self.tree.to_list(name='post_order')
        expected = [2, 12, 15, 10]
        self.assertEqual(actual, expected)


class TestAVLTrees(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = AVLTree(info=10)
        self.tree.insert(info=2)
        self.tree.insert(info=12)
        self.tree.insert(info=15)
        # self.tree.traverse()

    def test_insert(self):
        elements = self.tree.to_list(name='pre_order')
        self.assertIn(2, elements)
        self.assertIn(10, elements)
        self.assertIn(12, elements)
        self.assertIn(15, elements)

    def test_remove(self):
        pass

    def test_pre_order(self):
        actual = self.tree.to_list(name='pre_order')
        expected = [10, 2, 12, 15]
        self.assertEqual(actual, expected)

    def test_in_order(self):
        actual = self.tree.to_list(name='in_order')
        expected = [2, 10, 12, 15]
        self.assertEqual(actual, expected)

    def test_post_order(self):
        actual = self.tree.to_list(name='post_order')
        expected = [2, 12, 15, 10]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
