import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Searching', Difficult='Medium')


'''
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index (0 based indexing).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer N. Then in the next line are N space separated values of the array.

Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.

User Task:
You don't have to take any input. Just complete the provided function peakElement() and return the valid index.
'''

array = [1, 2, 3]


def peakElement(arr, n):
    # Code here
    if n is 1:
        return 0
    for i in range(n):

        # if element at first index is greater than next
        if i == 0 and arr[1] < arr[0]:
            return 0

        # if element is at last index and it is greater than
        # its prev one
        elif i == n - 1 and arr[n - 2] < arr[n - 1]:
            return n - 1

        # case, when element is at any other index
        # then you need to check both of its neighbour
        elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            return i


print(peakElement(array, len(array)))
