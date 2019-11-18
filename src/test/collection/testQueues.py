import unittest
from src.main.collection.queues import Queue


class TestQueues(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def test_add(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        expected = self.queue.peek()
        self.assertEqual(expected, 1)

    def test_remove(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        actual = self.queue.remove().get_info()
        self.assertEqual(actual, 1)

    def test_peek(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.queue.remove()
        expected = self.queue.peek()
        self.assertEqual(expected, 2)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())


if __name__ == '__main__':
    unittest.main()
