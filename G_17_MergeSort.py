import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Medium')


def mergeSort(array):
    if len(array) == 1:
        return
    piviot = len(array) // 2

    left = array[:piviot]
    right = array[piviot:]

    mergeSort(left)
    mergeSort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

        k += 1
    while i < len(left):
        array[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


array = [5, 4, 3, 2, 1]
mergeSort(array)
print(array)
