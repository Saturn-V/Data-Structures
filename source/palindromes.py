#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    if len(text) <= 1:
        return True
    else:
        first_half = text[:len(text)/2]
        if len(text) % 2 is 0:
            second_half = text[len(text)/2:]
        else:
            second_half = text[len(text)/2 + 1:]
        second_half = list(second_half)
        second_half.reverse()
        second_half = ''.join(second_half)
        if first_half == second_half:
            return True
        return False



def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if left is None and right is None:
        left = 0
        right = -1

        if len(text) <= 1:
            return True
        return is_palindrome_recursive(text, left, right)
    else:
        if text[left] is text[right]:
            if left is len(text)/2:
                return True
            left += 1
            right -= 1
            return True and is_palindrome_recursive(text, left, right)
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    print(is_palindrome_iterative('racecar'))
