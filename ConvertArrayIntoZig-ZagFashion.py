import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Two-Pointer', Difficult='Medium')


'''
Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. 
The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in 
the output i.e you have to iterate on the original array only.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases 
follow. Each testcase contains two lines of input. The first line contains a single integer N denoting the size of array.
The second line contains N space-separated integers denoting the elements of the array.

Output:
For each testcase, print the array in Zig-Zag fashion.
'''
array = [4, 3, 7, 8, 6, 2, 1]

# out = 3 7 4 8 2 6 1


def zigZag(array):
    k = 3
    for i in range(1, len(array) - 1, 2):
        if array[i - 1] > array[i]:
            swap(array, i - 1, i)
        if array[i] < array[i + 1]:
            swap(array, i, i + 1)
    print(array)


def swap(a, i, j):

    a[i], a[j] = a[j], a[i]


zigZag(array)
