from typing import Optional, Any

from src.main.collection.linkedLists import SinglyLinkedList
from src.main.collection.node import Node


class Stack(object):

    def __init__(self):
        self.storage = SinglyLinkedList()

    def __str__(self) -> str:
        """
        Function to return string representation of stack
        :return: String
        """
        representation = ""
        if self.is_empty():
            return representation
        else:
            reversed_linked_list = self.__reverse(self.storage.head)

            current = reversed_linked_list.head
            while current is not None:
                representation += "|{}|\n".format(current.get_info())
                current = current.get_next()
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

    def pop(self) -> Optional:
        """
        Function to remove top element
        :return: Optional
        """
        if self.is_empty():
            return None
        else:
            prev = None
            current = self.storage.head
            while current.get_next() is not None:
                prev = current
                current = current.get_next()
            if prev is None:
                self.storage.head = None
                self.storage.tail = None
            else:
                prev.set_next(None)
                self.storage.tail = prev
                return current

    def push(self, info: Any) -> None:
        """
        Function to push an element to a stack
        :param info: Information to store
        :return:
        """
        self.storage.add_link(info=info)

    def peek(self) -> Optional:
        """
        Function to peek the top of the stack
        :return: None or Any
        """
        if self.is_empty():
            return None
        else:
            return self.storage.tail.get_info()

    def is_empty(self) -> bool:
        """
        Function to check if stack is empty or not
        :return:
        """
        return True if self.storage.head is None else False
