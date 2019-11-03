from src.collection.lists.singlyLinkedList import SinglyLinkedList

# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?


def deduplicate(linkedlist: object) -> object:
    pass


if __name__ == '__main__':
    linked_list = SinglyLinkedList(info=1)
    linked_list.add_link(info=2)
    linked_list.add_link(info=4)
    linked_list.add_link(info=3)
    linked_list.add_link(info=2)
    linked_list.add_link(info=4)
    linked_list.print_links()
