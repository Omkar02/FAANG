import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='BinarySearch', Difficult='Medium')


# Given a sorted array of n elements, possibly with duplicates, find the
# number of occurrences of the target element.

# Example 1:

# Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
# Output: 3


def countFinder(array, k):
    pos = [-1, -1]
    piviot = (0 + len(array)) // 2
    _ = modBinarySearch(array, k, 0, piviot, pos, True)
    val = modBinarySearch(array, k, piviot, len(array) - 1, pos, False)

    return val


def modBinarySearch(array, k, left, right, pos, isLeft):
    if left == right:
        return -1
    piviot = (left + right) // 2
    # print(array[piviot], array[left], array[right])

    if isLeft:
        if k == array[piviot] and array[piviot] != array[piviot - 1]:
            pos[0] = piviot
            return -1
    else:
        if k == array[piviot] and array[piviot] != array[piviot + 1]:
            pos[1] = piviot
            return (pos[1] - pos[0]) + 1

    return modBinarySearch(array, k, left, piviot, pos, isLeft)


array = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
k = 8

array = [3, 5, 5, 5, 5, 7, 8, 8]
k = 5
print(countFinder(array, k))
