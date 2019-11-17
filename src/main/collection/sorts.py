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
    right_index, left_index = 0, 0
    sorted_list = list()
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    if left:
        sorted_list += left[left_index:]

    if right:
        sorted_list += right[right_index:]

    return sorted_list


if __name__ == '__main__':
    # ls = [1, 4, 2, 3]
    # print(merge_sort(ls))
    print(merge([1, 4], [2, 3]))
