# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique(value: str) -> bool:
    for i in range(0, len(value)):
        letter = value[i]
        for j in range(i + 1, len(value)):
            if letter == value[j]:
                return False
    return True


# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.

def permutations(letters: list) -> list:
    if len(letters) == 2:
        return [(letters[0], letters[1]), (letters[1], letters[0])]
    else:
        result = list()
        prefix = tuple(letters[:1])
        suffix = letters[1:]
        for perm in permutations(suffix):
            for i in range(len(perm) + 1):
                result.append(perm[:i] + prefix + perm[i:])
        return result


def is_permutation(first: list, second: list) -> bool:
    perms = permutations(first)
    return True if tuple(second) in perms else False


# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this operation in place.)

def urlify(sentence, length):
    result = ""
    for i in range(length):
        if sentence[i] == " ":
            result = result + "%20"
        else:
            result = result + sentence[i]
    return result


# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

def is_palindrome(values: list) -> bool:
    for i in range(len(values)):
        j = len(values) - 1 - i
        if values[i] != values[j]:
            return False
        if i == j:
            break
    return True


def is_palindrome_permutation(first: list) -> bool:
    perms = permutations(first)
    for perm in perms:
        if is_palindrome(perm):
            return True
    return False


# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(first: str, second: str) -> bool:
    if len(first) - len(second) > 1 or len(first) - len(second) < -1:
        return False
    if len(first) > len(second):
        length = len(first)
        difference = len(first) - len(second)
        second = [letter for letter in second]
        second = second + [" " for i in range(difference)]
    else:
        length = len(second)
        difference = len(second) - len(first)
        first = [letter for letter in first]
        first = first + [" " for i in range(difference)]
    edits = 0
    for i in range(length):
        if first[i] != second[i]:
            edits += 1
    return True if edits <= 1 else False


# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def compress(string: str) -> str:
    compress_string = ""
    count = 0
    for i in range(len(string) - 1):
        count += 1
        if string[i] != string[i + 1]:
            compress_string = compress_string + string[i] + str(count)
            count = 0
    return string if len(compress_string) >= len(string) else compress_string


# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.
# Can you do this in place?

def string_to_list(string: str) -> list:
    return [string[i] for i in range(len(string))]


def print_matrix(matrix: list) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print("\n")


def rotate_matrix(matrix: list, offset: int = 0) -> list:
    length = len(matrix)
    top = 0 + offset
    left = 0 + offset
    bottom = length - offset
    right = length - offset

    if top == bottom and left == right:
        return matrix
    else:

        row_one = list()
        row_two = list()
        row_three = list()
        row_four = list()

        for i in range(left, right):
            row_one.append(matrix[top][i])
            row_three.append(matrix[bottom - 1][i])

        for i in range(top, bottom):
            row_four.append(matrix[i][left])
            row_two.append(matrix[i][right - 1])

        for i in range(left, right):
            matrix[top][i] = list(reversed(row_four))[i - offset]
            matrix[bottom - 1][i] = list(reversed(row_two))[i - offset]

        for i in range(top, bottom):
            matrix[i][right - 1] = row_one[i - offset]
            matrix[i][left] = list(reversed(row_three))[i - offset]

        return rotate_matrix(matrix, offset=offset + 1)


# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

def zero(matrix: list) -> list:
    length = len(matrix)
    zero_mapping = list()
    for row in range(length):
        for col in range(length):
            if matrix[row][col] == 0:
                print("Marked: ({}, {})".format(row, col))
                zero_mapping.append((row, col))

    for element in zero_mapping:
        for i in range(length):
            matrix[element[0]][i] = 0
            matrix[i][element[0]] = 0

    return matrix


# String Rotation:Assume you have a method isSubstring which checks
# if one word is a substring of another. Given two strings, sl and s2,
# write code to check if s2 is a rotation of sl using only one call to
# isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

def is_substring(first: str, second: str) -> bool:
    return True if first in second else False


def is_rotation(first: str, second: str) -> bool:
    return is_substring(first, second + second)


if __name__ == '__main__':
    print(is_rotation("erbottlewat", "waterbottle"))
