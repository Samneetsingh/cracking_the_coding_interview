# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique(value):
    for i in range(0, len(value)):
        letter = value[i]
        for j in range(i + 1, len(value)):
            if letter == value[j]:
                return False
    return True


# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.

def is_permutation(first, second):
    pass


if __name__ == '__main__':
    print(is_unique("qwertyuioasdfghjkl"))
    print(is_unique("bad"))
