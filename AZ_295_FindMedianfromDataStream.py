# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Heap', Difficult='Hard')
from Datastruct.masterHeap import maxHeap, minHeap


lower = maxHeap([])
greater = minHeap([])
median = None
va = [lower, greater, median]


def addNumber(number):
    if not va[0].length or number < va[0].peek():
        va[0].length += 1
        va[0].insert(number)
    else:
        va[1].length += 1
        va[1].insert(number)

    rebalanceHeap()
    updateMedium()


def rebalanceHeap():
    if va[0].length - va[1].length == 2:
        va[1].insert(va[0].remove())
        va[0].length -= 1
        va[1].length += 1
    elif va[1].length - va[0].length == 2:
        va[0].insert(va[1].remove())
        va[0].length += 1
        va[1].length -= 1


def updateMedium():
    if va[0].length == va[1].length:
        va[2] = (va[0].peek() + va[1].peek()) / 2

    elif va[0].length > va[1].length:
        va[2] = va[0].peek()

    else:
        va[2] = va[1].peek()


arr = [5, 10, 100, 200, 6, 13, 14]
for i in arr:
    addNumber(i)
    print(va[2], end=', ')

print()
# [5, 7.5, 10, 55.0, 10, 11.5, 13]
