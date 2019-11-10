from src.collection.lists.singlyLinkedList import SinglyLinkedList


# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?


def deduplicate(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    unique = set()
    current = linked_list.head
    unique.add(current.get_info())
    new_linked_list = SinglyLinkedList(current.get_info())
    while current.get_next() is not None:
        info = current.get_info()
        if info not in unique:
            unique.add(info)
            new_linked_list.add_link(info)
        current = current.get_next()
    return new_linked_list


def deduplicate_without_buffer(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    outer_current = linked_list.head
    while outer_current.get_next() is not None:
        inner_prev = None
        inner_current = outer_current.get_next()
        while inner_current is not None:
            if outer_current.get_info() == inner_current.get_info():
                inner_prev.set_next(inner_current.get_next())
            inner_prev = inner_current
            inner_current = inner_current.get_next()
        outer_current = outer_current.get_next()
    return linked_list


# Return Kth to Last: Implement an algorithm to find the kth to
# last element of a singly linked list.

def kth(index, linked_list: SinglyLinkedList) -> int:
    current = linked_list.head
    length = 0
    buffer = list()
    while current is not None:
        buffer.append(current.get_info())
        length += 1
        current = current.get_next()

    return buffer[length - 1 - index]


# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the
# exact middle) of a singly linked list, given only access to that node.
# EXAMPLE
# Input:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks likea->b->d->e- >f

def delete_middle(linked_list: SinglyLinkedList, info: int) -> SinglyLinkedList:
    prev = linked_list.head
    current = linked_list.head.get_next()
    while current.get_next() is not None:
        if current.get_info() == info:
            prev.set_next(current.get_next())
        prev = current
        current = current.get_next()
    return linked_list


# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or
# equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x
# can appear anywhere in the "right partition"; it does not need to appear
# between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


if __name__ == '__main__':
    test_linked_list = SinglyLinkedList(info=1)
    test_linked_list.add_link(info=2)
    test_linked_list.add_link(info=4)
    test_linked_list.add_link(info=3)
    test_linked_list.add_link(info=2)
    test_linked_list.add_link(info=4)
    test_linked_list.print_links()
    delete_middle(test_linked_list, 4).print_links()
    delete_middle(test_linked_list, 2).print_links()
