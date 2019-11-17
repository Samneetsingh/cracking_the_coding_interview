import unittest

from src.main.chapterTwo.linkedLists import *
from src.main.collection.linkedLists import SinglyLinkedList


class TestLinkedLists(unittest.TestCase):

    def setUp(self) -> None:
        self.test_linked_list = SinglyLinkedList()
        self.test_linked_list.add_link(2)
        self.test_linked_list.add_link(1)
        self.test_linked_list.add_link(2)
        self.test_linked_list.add_link(3)
        self.test_linked_list.add_link(4)

    @staticmethod
    def create_loop(linked_list: SinglyLinkedList) -> SinglyLinkedList:
        count = 0
        loop_node = None
        current = linked_list.head
        while current.get_next() is not None:
            if count == 3:
                loop_node = current

            count += 1
            current = current.get_next()
        current.set_next(loop_node)
        return linked_list

    def test_deduplicate(self):
        expected_linked_list = SinglyLinkedList()
        expected_linked_list.add_link(2)
        expected_linked_list.add_link(1)
        expected_linked_list.add_link(3)
        expected_linked_list.add_link(4)

        actual_linked_list = deduplicate(linked_list=self.test_linked_list)
        self.assertEqual(expected_linked_list, actual_linked_list)

    def test_deduplicate_without_buffer(self):
        expected_linked_list = SinglyLinkedList()
        expected_linked_list.add_link(2)
        expected_linked_list.add_link(1)
        expected_linked_list.add_link(3)
        expected_linked_list.add_link(4)

        actual_linked_list = deduplicate(linked_list=self.test_linked_list)
        self.assertEqual(expected_linked_list, actual_linked_list)

    def test_kth(self):
        self.assertEqual(4, kth(0, self.test_linked_list))
        self.assertEqual(3, kth(1, self.test_linked_list))
        self.assertEqual(2, kth(2, self.test_linked_list))
        self.assertEqual(1, kth(3, self.test_linked_list))
        self.assertEqual(2, kth(4, self.test_linked_list))

    def test_add_numbers(self):
        first_number = SinglyLinkedList()
        first_number.add_link(7)
        first_number.add_link(1)
        first_number.add_link(6)

        second_number = SinglyLinkedList()
        second_number.add_link(5)
        second_number.add_link(9)
        second_number.add_link(2)

        expected = SinglyLinkedList()
        expected.add_link(2)
        expected.add_link(1)
        expected.add_link(9)

        self.assertEqual(add_numbers(first_number, second_number), expected)

    def test_is_palindrome(self):
        linked_list = SinglyLinkedList()
        linked_list.add_link(info="r")
        linked_list.add_link(info="a")
        linked_list.add_link(info="c")
        linked_list.add_link(info="e")
        linked_list.add_link(info="c")
        linked_list.add_link(info="a")
        linked_list.add_link(info="r")

        self.assertTrue(is_palindrome(linked_list))

    def test_intersection(self):
        pass

    def test_loop_detection(self):
        linked_list = SinglyLinkedList()
        linked_list.add_link("a")
        linked_list.add_link("b")
        linked_list.add_link("c")
        linked_list.add_link("d")
        linked_list.add_link("e")
        self.assertFalse(loop_detection(linked_list.head))

        looped_linked_list = self.create_loop(linked_list)
        self.assertTrue(loop_detection(looped_linked_list.head))


if __name__ == '__main__':
    unittest.main()
