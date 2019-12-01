from src.main.collection.nodes import SingleChildNode


class SinglyLinkedList(object):

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __eq__(self, other):
        if self.size != other.size:
            return False

        current = self.head
        expected_current = other.head
        while current is not None and expected_current is not None:
            if current.get_info() != expected_current.get_info():
                return False

            current = current.get_next()
            expected_current = expected_current.get_next()

        return True

    def __str__(self):
        next_node = self.head
        representation = "[ "
        while next_node.get_next() is not None:
            representation += "{}, ".format(next_node.get_info())
            next_node = next_node.get_next()
        representation += "{} ]".format(next_node.get_info())
        return representation

    def add_link(self, info) -> None:
        """
        Function to add a new link to linkedlist
        :param info: data
        :return: None
        """
        new_node = SingleChildNode(info)
        if self.head is None:
            self.head = new_node
        else:
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


if __name__ == '__main__':
    test_list = SinglyLinkedList()
    test_list.add_link(info=1)
    test_list.add_link(info=2)
    test_list.add_link(info=3)
    test_list.add_link(info=4)
    test_list.remove_link(info=5)
    test_list.remove_link(info=1)
    test_list.remove_link(info=7)
