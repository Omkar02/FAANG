import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sorting', Difficult='Hard')


def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(len(array) - 1)):
        swap(array, endIdx, 0)
        heapify(array, endIdx, 0)


def buildMaxHeap(array):
    n = len(array) // 2
    for idx in reversed(range(n - 1)):
        heapify(array, n, idx)


def heapify(array, heapLength, currIdx):
    largest = currIdx
    leftChild = 2 * currIdx + 1
    rightChild = 2 * currIdx + 2

    if leftChild < heapLength and array[largest] < array[leftChild]:
        largest = leftChild

    if rightChild < heapLength and array[largest] < array[rightChild]:
        largest = rightChild

    if largest != currIdx:
        swap(array, currIdx, largest)
        heapify(array, heapLength, largest)


def swap(array, eleOne, eleTwo):
    array[eleTwo], array[eleOne] = array[eleOne], array[eleTwo]


array = [41, 421, 41, 41, 2, 415, 436, 7, 6, 5, 4, 5, 64, 534]
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array1 = array
heapSort(array)
print(array)
print(array == sorted(array1))
