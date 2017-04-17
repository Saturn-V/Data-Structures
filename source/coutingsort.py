def counting_sort(iterable):
    # create
    # create list of size items that stores sum of occurences
    # place each item in histogram in new position that matches # occurences

    minimum = iterable[0]
    maximum = iterable[0]

    for key in iterable:
        if key < minimum:
            minimum = key
        elif key > maximum:
            maximum = key

    hist = [0]*(maximum+1)

    for index in range(len(hist)):
        hist[index] += iterable.count(index)

    previous = 0
    sumCount = [0]*(maximum+1)
    for index in range(minimum, len(sumCount)):
        # if previous is not None:
        sumCount[index] = hist[index] + previous
        previous = sumCount[index]

    sorted_input = [None]*(len(iterable)+1)
    for value_index in iterable:
        sorted_index = sumCount[value_index]
        sumCount[value_index] -= 1
        sorted_input[sorted_index] = value_index

    del sorted_input[0]



    print('hist: ', hist)
    print('sumCount', sumCount)
    print('sortedInput', sorted_input)
    print('min: ', minimum)
    print('max: ', maximum)


    # hist = {}
    # minimum = iterable[0]
    # maximum = iterable[0]

    # calculate the histogram of key frequencies:
    # for key in iterable:
    #     if key < minimum:
    #         minimum = key
    #     elif key > maximum:
    #         maximum = key
    #     hist[key] = hist.get(key, 0) + 1

    # calculate the starting index for each key:
    # total = 0
    # sumCount = []
    # for i in range(len(hist)):   # i = 0, 1, ... k-1
    #     oldCount = count[i]
    #     count[i] = total
    #     total += oldCount
    #
    # # copy to output array, preserving order of inputs with equal keys:
    # for x in input:
    #     output[count[key(x)]] = x
    #     count[key(x)] += 1
    #
    # return output

    # print('sums: ', sums)

if __name__ == '__main__':
    data = [3, 5, 6, 8, 6, 3, 2, 2, 5, 6, 5, 5, 1]
    counting_sort(data)
