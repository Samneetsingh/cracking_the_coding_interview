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


def merge_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        middle = int(len(unsorted_list) / 2)
        left = merge_sort(unsorted_list[:middle])
        right = merge_sort(unsorted_list[middle:])
        sorted_list = merge(left, right)
        return sorted_list


def merge(left: list, right: list) -> list:
    left_index = 0
    right_index = 0
    sorted_list = list()
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list
