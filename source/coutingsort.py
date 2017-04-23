from __future__ import print_function

def counting_sort(iterable):
    if len(iterable) == 0:
        return iterable
        
    minimum = iterable[0] # min(iterable)
    maximum = iterable[0] # max(iterable)

    # Finding min and max
    for key in iterable:
        if key < minimum:
            minimum = key
        elif key > maximum:
            maximum = key

    # Creating a histogram
    hist = [0]*(maximum-minimum+1)
    # for index in range(len(hist)):
    #     hist[index] += iterable.count(index)
    for item in iterable:
        index = item - minimum
        hist[index] += 1

    print('input: ', iterable)
    print('hist: ', hist)

    sorted_output = []
    for index, count in enumerate(hist):
        value = index + minimum
        for _ in range(count):
            sorted_output.append(value)

    #
    # previous = 0
    # sumCount = [0]*(maximum+1)
    # for index in range(minimum, maximum+1):
    #     # if previous is not None:
    #     sumCount[index] = hist[index] + previous
    #     previous = sumCount[index]

    # print('sumCount', sumCount)

    # sorted_input = [None]*(len(iterable)+1)
    # for value_index in iterable:
    #     sorted_index = sumCount[value_index]
    #     sumCount[value_index] -= 1
    #     sorted_input[sorted_index] = value_index
    #
    # del sorted_input[0]

    # print('input: ', iterable)
    # print('hist: ', hist)
    # print('sumCount', sumCount)
    print('sorted output', sorted_output)
    print('min: ', minimum)
    print('max: ', maximum)

if __name__ == '__main__':
    data = [3, 5, 6, 8, 6, 3, 2, 2, 5, 6, 5, 5, 1]
    counting_sort(data)
