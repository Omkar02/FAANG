import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


'''
Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.

Input:
The first line of input contains the number of test cases, then T test cases follow.
Each test case will contain an integer K denoting the number of sorted arrays(each with size K).
Then in the next line contains all the elements of the array separated by space.

Output:
The output will be the sorted merged array.

User Task:
You need to complete mergeKArrays() function which takes 2 arguments,
an arr[k][k] 2D Matrix containing k sorted arrays and an integer k denoting the number of
sorted arrays. The function should return a pointer to the merged sorted arrays.

Expected Time Complexity: O(nk Logk)
Expected Auxiliary Space: O(k)
'''

arrays = [[1, 2, 2, 2],
          [3, 3, 4, 4],
          [5, 5, 6, 6],
          [7, 8, 9, 9]]

import heapq


def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in range(len(arrays)):
        smallestItems.append({"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty():
        smallestItem = minHeap.remove()
        arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"]
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue
        minHeap.insert(
            {"arrayIdx": arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]}
        )
    return sortedList
