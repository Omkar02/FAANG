import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Heap', Difficult='Hard')

# O(NK*log(NK)) time | O(NK*log(NK))

import heapq


def mergeSortedArray(array):
    # [firstElement, fromWhichList, currIndex]
    mergedList = []
    elementsArray = [(lst[0], idx, 0) for idx, lst in enumerate(array) if lst]
    heapq.heapify(elementsArray)

    while elementsArray:
        element, fromWhichList, currIndex = heapq.heappop(elementsArray)
        mergedList.append(element)

        if currIndex + 1 < len(array[fromWhichList]):
            nextElement = (array[fromWhichList][currIndex + 1],
                           fromWhichList,
                           currIndex + 1)

            heapq.heappush(elementsArray, nextElement)

    return mergedList


array = [[10, 15, 30],
         [12, 20],
         [17, 20, 32]]
print(mergeSortedArray(array))
