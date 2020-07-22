import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')

'''
You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. 
The transition point is a point where "0" ends and "1" begins (0 based indexing).
Note that, if there is no "1" exists, print -1.
Note that, in case of all 1s print 0.

Input:
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output:
Your function should return transition point.
'''


def transitionPoint(array):
    idxOne = 0
    idxTwo = idxOne + 1
    while idxTwo < len(array):
        if array[idxOne] != array[idxTwo]:
            return idxTwo
        idxOne += 1
        idxTwo += 1
    return -1


array = [0, 0, 0, 1, 1]
print(transitionPoint(array))
