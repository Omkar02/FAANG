import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

'''
Given a binary array A[] of size N. The task is to arrange the array in increasing order.

Note: The binary array contains only 0  and 1.

Input:
The first line of input contains an integer T, denoting the test cases. 
Every test case contains two lines, the first line is N(size of the array) 
and the second line is space-separated elements of the array.

Output:
Space-separated elements of sorted arrays. There should be a new line between the output of every test case.

Your Task:
Complete the function SortBinaryArray() which takes given array as input and returns the sorted array. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''


def sortBinarryArr(array):
    leftIdx = 0
    rightIdx = leftIdx + 1
    while rightIdx < len(array):
        if array[leftIdx] == 1 and array[rightIdx] == 0:
            swap(array, leftIdx, rightIdx)
            leftIdx += 1
        rightIdx += 1
    print(array)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


array = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
sortBinarryArr(array)
