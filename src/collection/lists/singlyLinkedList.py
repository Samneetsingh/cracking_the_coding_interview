from src.collection.lists.node import Node


class SinglyLinkedList(object):

    def __init__(self, info) -> None:
        self.head = Node(info)
        self.tail = self.head
        self.size = 1

    def add_link(self, info) -> None:
        """
        Function to add a new link to linkedlist
        :param info: data
        :return: None
        """
        new_node = Node(info)
        self.tail.set_next(new_node)
        self.tail = new_node
        self.size += 1

    def remove_link(self, info) -> None:
        """
        Function to remove a new link from linkedlist
        :param info: data
        :return: None
        """
        prev_node = None
        next_node = self.head
        while next_node is not None:
            if next_node.get_info() == info:
                if prev_node is None:
                    self.head = self.head.get_next()
                else:
                    prev_node.set_next(next_node.get_next())
                self.size -= 1
            prev_node = next_node
            next_node = next_node.get_next()

    def print_links(self) -> None:
        """
        Function to print linkedlist
        :return: None
        """
        next_node = self.head
        print("[", end="")
        while next_node.get_next() is not None:
            print("{}".format(next_node.get_info()), end=", ")
            next_node = next_node.get_next()
        print("{}]".format(next_node.get_info()))


if __name__ == '__main__':
    test_list = SinglyLinkedList(1)
    test_list.add_link(info=2)
    test_list.add_link(info=3)
    test_list.add_link(info=4)
    test_list.remove_link(info=5)
    test_list.remove_link(info=1)
    test_list.remove_link(info=7)
    test_list.print_links()
