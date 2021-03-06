from random import randint
from sorting import bubble_sort, selection_sort, insertion_sort, tree_sort, cocktail_shaker_sort

def merge(list1, list2):
    # merged_array = [0]*(len(list1)+len(lsit2))
    merged_array = []
    left_index = 0
    right_index = 0

    while left_index < len(list1) and right_index < len(list2):
        if list1[left_index] < list2[right_index]:
            merged_array.append(list1[left_index])
            left_index += 1
        else:
            merged_array.append(list2[right_index])
            right_index += 1

    merged_array.extend(list1[left_index:])
    merged_array.extend(list2[right_index:])
    return merged_array

def merge_sort_basic(items):
    list1 = cocktail_shaker_sort(items[:len(items)/2])
    list2 = cocktail_shaker_sort(items[len(items)/2:])
    return merge(list1, list2)

def merge_sort_recursive(items):
    if len(items) <= 1:
        return items

    list1 = merge_sort_recursive(items[:len(items)/2])
    list2 = merge_sort_recursive(items[len(items)/2:])
    return merge(list1, list2)

def merge_sort_basic_random(items):
    alg = randint(1, 5)
    if alg is 1:
        print('Using Bubble Sort.')
        print('Running Times:')
        print('Worst Case:')
        list1 = bubble_sort(items[:len(items)/2])
        list2 = bubble_sort(items[len(items)/2:])
    elif alg is 2:
        print('Using Selection Sort.')
        print('Running Times:')
        print('Worst Case:')
        list1 = selection_sort(items[:len(items)/2])
        list2 = selection_sort(items[len(items)/2:])
    elif alg is 3:
        print('Using Insertion Sort.')
        print('Running Times:')
        print('Worst Case:')
        list1 = insertion_sort(items[:len(items)/2])
        list2 = insertion_sort(items[len(items)/2:])
    elif alg is 4:
        print('Using Tree Sort.')
        print('Running Times:')
        print('Worst Case:')
        list1 = tree_sort(items[:len(items)/2])
        list2 = tree_sort(items[len(items)/2:])
    elif alg is 5:
        print('Using Cocktail Shaker Sort.')
        print('Running Times:')
        print('Worst Case:')
        list1 = cocktail_shaker_sort(items[:len(items)/2])
        list2 = cocktail_shaker_sort(items[len(items)/2:])

    return merge(list1, list2)

if __name__ == '__main__':
    data = [3, 5, 6, 8, 6, 3, 2, 2, 5, 6, 5, 5, 1]
    data_sorted = [1, 2, 2, 3, 3, 5, 5, 5, 5, 6, 6, 6, 8]
    list1 = data_sorted[:len(data_sorted)/2]
    list2 = data_sorted[len(data_sorted)/2:]
    # merge(list1, list2)
    # print(merge_sort_basic(data))
    print(merge_sort_recursive(data))
