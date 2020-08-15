import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Tree', Difficult='Hard')

from Datastruct.masterTree import BST

cnt = [0]


def sameBst(arr1, arr2):
    cnt[0] += 1
    if len(arr1) != len(arr2):
        return False

    if len(arr1) == 0 and len(arr2) == 0:
        return True

    if arr1[0] != arr2[0]:
        return False

    oneLeft = getSmaller(arr1)
    twoLeft = getSmaller(arr2)

    oneRight = getBiggerOrEqualto(arr1)
    twoRight = getBiggerOrEqualto(arr2)

    return sameBst(oneLeft, twoLeft) and sameBst(oneRight, twoRight)


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])

    return smaller


def getBiggerOrEqualto(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])

    return bigger


arr1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arr2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(f'isSame  = {sameBst(arr1,arr2)}')
print(cnt)
