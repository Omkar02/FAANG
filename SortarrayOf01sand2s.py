import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')
'''
Given an array of size N containing 0s, 1s, and 2s; sort the array in ascending order.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines, first of which will 
contain N. The second lines contains the elements of the array.

Output: 
Print sorted array.

Your Task:
Complete the function sort012() that takes array and n and sorts the array in place. 
'''


def bSort(array):
    j = len(array) - 1
    for i in range(len(array)):
        if array[i] == 1 and array[j] == 0:
            swap(array, i, j)
            j = -1
        if array[i] == 2 and array[j] == 0:
            swap(array, i, j)
            j -= 1
    print(array)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


array = [0, 2, 1, 2, 0]
# array = [0, 1, 0]
bSort(array)
