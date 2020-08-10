import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Medium')


def kMinNumber(array, k):
    postion = k - 1
    return kMinNumberHelper(array, 0, len(array) - 1, postion)


def kMinNumberHelper(array, startIdx, endIdx, postion):
    while True:
        if startIdx > endIdx:
            return None

        piviot = startIdx
        leftIndex = startIdx + 1
        rightIdx = endIdx

        while leftIndex <= rightIdx:
            if array[leftIndex] > array[piviot] and array[rightIdx] < array[piviot]:
                swap(array, leftIndex, rightIdx)

            if array[leftIndex] <= array[piviot]:
                leftIndex += 1

            if array[rightIdx] >= array[piviot]:
                rightIdx -= 1
        swap(array, rightIdx, piviot)

        if rightIdx == postion:
            return array[rightIdx]

        elif rightIdx < postion:
            startIdx = rightIdx + 1

        else:
            endIdx = rightIdx - 1


def swap(a, o, c):
    a[o], a[c] = a[c], a[o]


array = [1, 55, 345, 43, 54, 32, 4]
k = 2
print(kMinNumber(array, k))
print(array)
