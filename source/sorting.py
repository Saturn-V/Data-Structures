from bst import BinarySearchTree

def bubble_sort(items):
    # print(is_sorted(items))
    while not is_sorted(items):
        for current in range(1, len(items)):
            previous = current - 1
            # print('previous: ', items[previous])
            if items[previous] > items[current]:
                tmp = items[previous]
                items[previous] = items[current]
                items[current] = tmp

    return items

# Time Complexity |
# Worst Case:

# Best Case:

def selection_sort(items):
    smallest = 0
    offset = 0
    # is_sorted = False
    while not is_sorted(items):
        for current in range(offset+1, len(items)):
            if items[current] < items[smallest]:
                smallest = current
        tmp = items[offset]
        items[offset] = items[smallest]
        items[smallest] = tmp
        offset += 1
    return items

# Time Complexity |
# Worst Case:
# O(n^2) because we have to iterate over the entire list n times,
# and n- times to move an item to its appropriate position
# Best Case:
# O(n) because if our list is already sorted, we have to visit
# each item at least once
def insertion_sort(items):
    for current in range(1, len(items)):
        print(items)
        previous = current - 1
        tmp_previous = previous
        tmp_current = current
        while tmp_current is not 0 and items[tmp_previous] > items[tmp_current]:
            tmp = items[tmp_previous]
            items[tmp_previous] = items[tmp_current]
            items[tmp_current] = tmp
            tmp_previous -= 1
            tmp_current -= 1
    return items

def tree_sort(items):
    bst = BinarySearchTree(items)
    return bst.items_in_order()

def cocktail_shaker_sort(items):
    swapped = False
    init = True
    while swapped or init:
        init = False
        swapped = False
        for current in range(1, len(items)):
            previous = current - 1
            if items[previous] > items[current]:
                tmp = items[previous]
                items[previous] = items[current]
                items[current] = tmp
                swapped = True

        if not swapped:
            return items

        for current in range(len(items)-2, -1, -1):
            previous = current + 1
            if items[previous] < items[current]:
                tmp = items[previous]
                items[previous] = items[current]
                items[current] = tmp
                swapped = True
    return items





# Helper Method
def is_sorted(items):
    for current in range(1, len(items)):
        previous = current - 1
        # print('previous: ', items[previous], 'current: ', items[current])
        if items[previous] > items[current]:
            return False
    return True

if __name__ == '__main__':
    data = [5, 7, 9, 1, 0, 6]
    cocktail_shaker_sort(data)
