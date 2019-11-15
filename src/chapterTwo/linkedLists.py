from src.collection.lists.node import Node
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


# Sum Lists: You have two numbers represented by a linked list,
# where each node contains a single digit.The digits are stored in
# reverse order, such that the 1 's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.Thatis,912.
def list_to_linked_list(arr: list) -> SinglyLinkedList:
    if len(arr) <= 0:
        raise Exception("list is too small!")
    result = SinglyLinkedList(arr[0])
    for index in range(1, len(arr)):
        result.add_link(info=arr[index])
    return result


def add(first: SinglyLinkedList, second: SinglyLinkedList) -> SinglyLinkedList:
    carry = 0
    first_current = first.head
    second_current = second.head
    result = list()

    while first_current is not None and second_current is not None:
        value = str((carry + first_current.get_info() + second_current.get_info()) / 10).split(".")
        if len(value) > 1:
            carry = int(value[0])
        result.append(int(value[1]))

        first_current = first_current.get_next()
        second_current = second_current.get_next()

    while first_current is not None:
        value = str((carry + first_current.get_info()) / 10).split(".")
        if len(value) > 1:
            carry = int(value[0])
        result.append(int(value[1]))
        first_current = first_current.get_next()

    while second_current is not None:
        value = str((carry + second_current.get_info()) / 10).split(".")
        if len(value) > 1:
            carry = int(value[0])
        result.append(int(value[1]))

    return list_to_linked_list(result)


# Palindrome: Implement a function to check if a linked list is a palindrome.

def is_palindrome(linked_list: SinglyLinkedList) -> bool:
    buffer = list()
    current = linked_list.head

    while current is not None:
        buffer.append(current.get_info())
        current = current.get_next()

    if buffer == list(reversed(buffer)):
        return True
    else:
        return False


# Intersection: Given two (singly) linked lists, determine if the two lists intersect.
# Return the inter­secting node. Note that the intersection is defined based on reference,
# not value.That is, if the kth node of the first linked list is the exact same node (by reference)
# as the jth node of the second linked list, then they are intersecting.

def intersection(first: SinglyLinkedList, second: SinglyLinkedList) -> bool:
    first_current = first.head

    while first_current is not None:
        second_current = second.head
        while second_current is not None:
            if second_current == first_current:
                return True
            second_current = second_current.get_next()
        first_current = first_current.get_next()

    return False


# Loop Detection: Given a circular linked list, implement an algorithm that returns
# the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points
# to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C[thesameCasearlier]
# Output: C

def loop_detection(head: Node) -> bool:
    visited = list()

    current = head
    while current is not None:
        if current in visited:
            return True

    return False


if __name__ == '__main__':
    first = SinglyLinkedList(info="r")
    first.add_link(info="a")
    first.add_link(info="c")
    first.add_link(info="e")
    first.add_link(info="c")
    first.add_link(info="a")
    first.add_link(info="r")
    first.print_links()
    print(loop_detection(""))
