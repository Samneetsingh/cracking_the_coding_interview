from typing import Any

from src.main.collection.linkedLists import SinglyLinkedList
from src.main.collection.node import Node


class Queue(object):

    def __init__(self):
        self.storage = SinglyLinkedList()

    def __str__(self):
        """
        Function to return string representation of queue
        :return: String
        """
        representation = ""
        if self.is_empty():
            return representation
        else:
            reversed_linked_list = self.__reverse(self.storage.head)
            current = reversed_linked_list.head
            while current.get_next() is not None:
                representation += "{}->".format(current.get_info())
                current = current.get_next()
            representation += "{}".format(current.get_info())
            return representation

    def __reverse(self, head: Node) -> SinglyLinkedList:
        """
        Function to get reverse of a linked list
        :param head: Node
        :return: SinglyLinkedList
        """
        if head.get_next() is None:
            linked_list = SinglyLinkedList()
            linked_list.add_link(head.get_info())
            return linked_list
        else:
            linked_list = self.__reverse(head.get_next())
            linked_list.add_link(info=head.get_info())
            return linked_list

    def add(self, info: Any) -> None:
        self.storage.add_link(info=info)

    def remove(self):
        if self.is_empty():
            return None
        else:
            current = self.storage.head
            self.storage.head = self.storage.head.get_next()
            return current

    def peek(self):
        return self.storage.head

    def is_empty(self):
        return True if self.storage.head is None else False


if __name__ == '__main__':
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()

    print(queue)
