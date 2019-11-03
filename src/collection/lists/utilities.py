import time
from src.collection.lists.singlyLinkedList import SinglyLinkedList


def sort(linked_list: SinglyLinkedList) -> SinglyLinkedList:
    for i in range(linked_list.size):
        print("Round: {}".format(i))
        prev_link = None
        current_link = linked_list.head
        for j in range(linked_list.size - 2 - i):
            print(j, j + 1)
            if current_link.get_info() > current_link.get_next().get_info():
                print("Swapping: {} -> {}".format(current_link, current_link.get_next()))
                if prev_link is None:
                    next_link = current_link.get_next()
                    current_link.set_next(next_link.get_next())
                    current_link = next_link

                # else:
                #     first = prev_link
                #     second = next_link
                #     third = next_link.get_next()
                #     forth = next_link.get_next().get_next()
                #     first.set_next(third)
                #     third.set_next(second)
                #     second.set_next(forth)
                pass
            linked_list.print_links()
            print("\n")
            prev_link = current_link
            current_link = current_link.get_next()
            time.sleep(3)

    return linked_list


if __name__ == '__main__':
    test_list = SinglyLinkedList(info=10)
    test_list.add_link(info=2)
    test_list.add_link(info=4)
    test_list.add_link(info=3)
    test_list.add_link(info=2)
    test_list.add_link(info=1)
    # test_list.print_links()
    sorted_linked_list = sort(test_list)
    # sorted_linked_list.print_links()
    # print(test_list.size)
