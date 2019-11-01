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

def permute(letters: list) -> list:
    if len(letters) == 2:
        return ["{}{}".format(letters[0], letters[1]), "{}{}".format(letters[1], letters[0])]
    else:
        p = list()
        prefix = letters[:1]
        suffix = letters[1:]
        for element in permute(suffix):
            p.append("{}{}".format(prefix[0], element))
            p.append("{}{}".format(element, prefix[0]))
        print(p)
        return p


def permutations(letters: list) -> list:
    p = list()
    for i in range(len(letters) + 1):
        print(letters)
        p = p + permute(letters)
        letters = letters[1:] + letters[:1]
    return list(set(p))


def is_permutation(first: list) -> bool:
    p = list()
    for i in range(len(first)):
        p.append(permutations(first))
        p = p[1:] + p[:1]
    print(p)
    return True


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

def is_palindrome(string):
    pass


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

def rotate(matrix: list) -> list:
    pass


# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

def zero(matrix: list) -> list:
    pass


# String Rotation:Assume you have a method isSubstring which checks
# if one word is a substring of another. Given two strings, sl and s2,
# write code to check if s2 is a rotation of sl using only one call to
# isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").

def is_substring_rotation(string: str) -> bool:
    pass


if __name__ == '__main__':
    print(compress("aabbcccccdddddAAAAeeef"))
    print(compress("abcd"))
