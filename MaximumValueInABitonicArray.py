import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sliding-Window', Difficult='Medium')


"""
Given an array of elements which is first increasing and then may be decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the maximum value.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, the size of array, the 
second line of each test case contains N integers which are the array elements.

Output:
Print the maximum element in the array.
"""

array = [1, 15, 25, 45, 42, 21, 17, 12, 11]
array = [1, 45, 47, 50, 5]


def bitonicArray(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            print(array[i - 1])
            break


bitonicArray(array)
