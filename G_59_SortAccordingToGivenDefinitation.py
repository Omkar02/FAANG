import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def theOrder(array, order):
    currPoint = 0
    array.sort()
    for j in order:
        currPoint = binarySearch(array, 0, len(array) - 1, j, currPoint)
    return array


def binarySearch(array, low, high, x, currPoint):
    while currPoint < len(array) - 1:
        print(x, '-------------------------------', currPoint)
        while low <= high:
            # print(low, high, x, array)
            mid = (low + high) // 2
            if x > array[mid]:
                low = mid + 1
            elif x < array[mid]:
                high = mid - 1
            else:
                swap(array, currPoint, mid)
                currPoint += 1
                break
        if low > high:
            return currPoint


def swap(array, o, m):
    array[o], array[m] = array[m], array[o]


array = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
order = [2, 1, 8, 3, 5, 6, 7, 9]
# output = [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]
# output = [2, 2, 7, 1, 1, 8, 8, 3, 5, 6, 9]
print(f'the order = {theOrder(array,order)}')
