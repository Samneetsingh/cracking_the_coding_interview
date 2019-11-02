from src.collection.lists.node import Node


class SinglyLinkedList(object):

    def __init__(self, info):
        self.head = Node(info)
        self.tail = self.head

    def add_link(self, info):
        new_node = Node(info)
        self.tail.set_next(new_node)
        self.tail = new_node

    def remove_link(self, info):
        prev_node = None
        next_node = self.head
        while next_node is not None:
            if next_node.get_info() == info:
                if prev_node is None:
                    self.head = self.head.get_next()
                else:
                    prev_node.set_next(next_node.get_next())
            prev_node = next_node
            next_node = next_node.get_next()

    def print_links(self):
        next_node = self.head
        print("[", end="\t")
        while next_node is not None:
            print("{},".format(next_node.get_info()), end="\t")
            next_node = next_node.get_next()
        print("]", end="\t")


if __name__ == '__main__':
    test_list = SinglyLinkedList("1")
    test_list.add_link(info="2")
    test_list.add_link(info="3")
    test_list.add_link(info="4")
    test_list.remove_link(info="1")
    test_list.remove_link(info="3")
    test_list.remove_link(info="4")
    test_list.print_links()
