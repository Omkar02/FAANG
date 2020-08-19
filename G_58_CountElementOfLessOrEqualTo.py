# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


def countLessThan(array1, array2):
    result = []
    array2.sort()
    for i in range(len(array1)):
        binarySearch(array2, 0, len(array2) - 1, array1[i], result)
    return result


def binarySearch(array, low, high, x, rs):
    while low <= high:
        mid = (low + high) // 2
        if array[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1

    rs.append(high + 1)


array1 = [1, 2, 3, 4, 7, 9]
array2 = [0, 1, 2, 1, 1, 4]
print(f'the count = {countLessThan(array1,array2)}')
