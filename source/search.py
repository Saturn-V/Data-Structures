#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below

    if index > len(array) - 1:
        return None
    elif item is array[index]:
        return index # found
    else:
        return linear_search_recursive(array, item, index+1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below

    # mid_index = len(array)/2 + (len(array) % 2)
    left = array[:len(array)/2]
    right = array[len(array)/2:]
    center = right[0] # Set center point

    print('left: ', left)
    print('right: ', right)
    print('center: ', center)

    if not item < array[0] and not item > array[-1]: # if item isn't smaller than smallest value and isn't larger than largest value
        found_item = None
        while found_item is None:
            if item is center or item is array[0] or item is array[-1]: # Early exit if we get lucky
                print('running is')
                found_item = array.index(item)
            elif item < center: # Check out left branch
                print('running <')
                if len(left) is 1: # Check if its value matches our search term, and exit.
                    if left[0] is item:
                        found_item = array.index(item)
                    return None
                else:
                    right = left[len(left)/2:]
                    left = left[:len(left)/2]
                    center = right[0]
                    print('left: ', left)
                    print('right: ', right)
                    print('center: ', center)
            elif item >= center: # Check out left branch
                print('running >')
                if len(right) is 1: # Check if its value matches our search term, and exit.
                    if right[0] is item:
                        found_item = array.index(item)
                    return None
                else:
                    left = right[:len(right)/2]
                    right = right[len(right)/2:]
                    center = right[0]
        return found_item
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below

    if not left and not right: # If left and right aren't set, set them (1st run only)
        left = array[:len(array)/2]
        right = array[len(array)/2:]

    if not item < left[0] and not item > right[-1]: # if item isn't smaller than smallest value and isn't larger than largest value
        recursed_array = left + right # Create temporary array of left and right branches
        center = right[0] # Set center point
        if item is center: # Early exit if we get lucky
            return array.index(item)
        elif item < center: # Check out left branch
            if len(left) is 1: # Check if its value matches our search term, and exit.
                if left[0] is item:
                    return array.index(item)
                return None
            else:
                # array = array[:len(array)/2]
                l = left[:len(left)/2]
                r = left[len(left)/2:]
            return binary_search_recursive(array, item, l, r)
        elif item >= center: # Check out left branch
            if len(right) is 1: # Check if its value matches our search term, and exit.
                if right[0] is item:
                    return array.index(item)
                return None
            else:
                # array = array[len(array)/2:]
                l = right[:len(right)/2]
                r = right[len(right)/2:]
            return binary_search_recursive(array, item, l, r)
    else:
        return None
