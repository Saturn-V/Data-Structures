#!python

import string

def find(string, pattern):
    """True if the provided string contains the entire pattern at least once"""
    # implement find_iterative and find_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return find_iterative(string, pattern)
    # return is_palindrome_recursive(text)


def find_iterative(string, pattern):
    # TODO: implement the find_iterative function iteratively here
    # once implemented, change find to call find_iterative
    # to verify that your iterative implementation passes all tests
    # string = string.lower()
    print('start')
    position = 0
    index = 0
    while index < len(string):
        print(position)
        print(index, string[index], pattern[position])
        if string[index] is pattern[position]:
            if position is len(pattern)-1:
                return True
            position += 1
        else:
            position = 0
            index -= position
        index += 1
    return False


def find_recursive():
    # TODO: implement the find function recursively here
    pass
    # once implemented, change find to call find_recursive
    # to verify that your recursive implementation passes all tests




def find_index(string, pattern):
    """Returns the starting index of the first occurrence of pattern in string"""
    # implement find_index_iterative and find_index_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return find_index_iterative(string, pattern)
    # return is_palindrome_recursive(text)

def find_index_iterative(string, pattern):
    string = string.lower()
    position = 0
    for char in enumerate(string):
        print(char, pattern[position])
        if char[1] is pattern[position]:
            if position is len(pattern)-1:
                return string.index(pattern)
            position += 1
        else:
            position = 0
    return 'Pattern does not exist in provided string.'


def main():
    # print(find('Thisis Some VERy obsCURE SaMPLetext', 'sample'))
    print(find_index('Thisis Some VERy obsCURE SaMPLetext', 'sample'))

if __name__ == '__main__':
    main()
