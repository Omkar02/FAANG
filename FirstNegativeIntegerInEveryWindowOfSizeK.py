import __main__ as main
from Helper.TimerLogger import CodeTimeLogging
fileName = main.__file__
fileName = fileName.split('\\')[-1]

CodeTimeLogging(Flag='F', filename=fileName, Tag='Sliding-Window', Difficult='Medium')
"""
Given an array and a positive integer k, find the first negative integer for each and every 
window(contiguous subarray) of size k.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer n denoting the size of the array. 
The next line contains n space separated integers forming the array. The last line contains the window size k.

Output:
Print the space separated negative integer starting from the first till the end for every window size k. 
If a window does not contain a negative integer , then print 0 for that window.
"""
array = [-8, 2, 3, -6, 10]
k = 2

array = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3


def fistNegative(array, k):
    outNegative = []
    for i in range(len(array) - k + 1):
        currFrame = array[i:i + k]
        print(currFrame)
        if currFrame[0] < 0:
            outNegative.append(currFrame[0])
        elif currFrame[1] < 0:
            outNegative.append(currFrame[1])
        else:
            outNegative.append(0)

    print(outNegative)


fistNegative(array, k)
