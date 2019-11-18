import unittest
from src.main.collection.stacks import Stack


class TestStacks(unittest.TestCase):

    def setUp(self) -> None:
        self.stk = Stack()

    def test_push(self):
        self.stk.push(1)
        self.stk.push(2)
        self.stk.push(3)
        expected = self.stk.peek()
        self.assertEqual(expected, 3)

    def test_pop(self):
        self.stk.push(1)
        self.stk.push(2)
        self.stk.push(3)
        actual = self.stk.pop().get_info()
        self.assertEqual(actual, 3)

    def test_peek(self):
        self.stk.push(1)
        self.stk.push(2)
        self.stk.push(3)
        actual = self.stk.peek()
        self.assertEqual(actual, 3)

    def test_is_empty(self):
        self.assertTrue(self.stk.is_empty())


if __name__ == '__main__':
    unittest.main()
