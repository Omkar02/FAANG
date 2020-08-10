import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Medium')

cn = [0]


def quickSort(array):
    low = 0
    high = len(array) - 1
    quickSortHelper(array, low, high)


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    low = startIdx
    high = endIdx

    piviot = (low + high) // 2

    while low < high:
        cn[0] += 1
        if array[low] > array[piviot] and array[high] < array[piviot]:
            swap(array, low, high)

        if array[low] <= array[piviot]:
            low += 1

        if array[high] >= array[piviot]:
            high -= 1
    swap(array, piviot, high)
    leftSubArryIsSmaller = high - 1 - startIdx < endIdx - (high + 1)
    # if leftSubArryIsSmaller:
    quickSortHelper(array, startIdx, high - 1)
    quickSortHelper(array, high + 1, endIdx)
    # else:
    #     quickSortHelper(array, high + 1, endIdx)
    #     quickSortHelper(array, startIdx, high - 1)


def swap(array, l, r):
    array[l], array[r] = array[r], array[l]


# array = [7, 6, 5, 4, 3, 2, 1]
# n = 10
# array = [i for i in reversed(range(1, n))]
array = [4, 2, 6, 9, 2]
# print(array)
# array = [5, 4, 3, 2, 1]
quickSort(array)
print(array)
print(cn)
