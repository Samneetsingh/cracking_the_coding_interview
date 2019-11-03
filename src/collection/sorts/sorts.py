def bubble_sort(unsorted_list: list) -> list:
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


def insertion_sort(unsorted_list: list) -> list:
    for i in range(len(unsorted_list)):
        smallest = unsorted_list[i]
        for j in range(i, len(unsorted_list)):
            if smallest > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


import time


def merge(first: list, second: list) -> list:
    index = 0
    sorted_list = list()

    while first or second:
        print(first, second)
        if first[index] < second[index]:
            sorted_list.append(first.pop(index))
            sorted_list.append(second.pop(index))
        else:
            sorted_list.append(second.pop(index))
            sorted_list.append(first.pop(index))

    if len(first) < len(second):
        sorted_list += second
    else:
        sorted_list += first
    time.sleep(2)

    return sorted_list


def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) == 1:
        return unsorted_list
    else:
        middle = int(len(unsorted_list) / 2)
        return merge(merge_sort(unsorted_list[:middle]), merge_sort(unsorted_list[middle:]))


if __name__ == '__main__':
    unsorted = [1, 3, 2, 5, 4]
    # print(merge_sort(unsorted))
    print(merge([1, 3], [2, 4, 5]))
